#!/usr/bin/env python3

import argparse
from distutils.core import run_setup
import os
import pip
import subprocess
import sys

# TODO: redo as a bootstrap script
#       https://virtualenv.readthedocs.org/en/latest/reference.html#extending-virtualenv

parser = argparse.ArgumentParser()
parser.add_argument('--pyqt5')
parser.add_argument('--pyqt5-plugins')
parser.add_argument('--bin')
parser.add_argument('--activate')
parser.add_argument('--virtualenv', '--venv', default='venv')
parser.add_argument('--in-virtual', action='store_true', default=False)

args = parser.parse_args()

# TODO: let this be the actual working directory
myfile = os.path.realpath(__file__)
mydir = os.path.dirname(myfile)

if not args.in_virtual:
    try:
        os.mkdir(args.virtualenv)
    except FileExistsError:
        print('')
        print('')
        print('    Directory already exists and must be deleted to create the virtual environment')
        print('')
        print('        {args.virtualenv}'.format(**locals()))
        print('')

        sys.exit(1)

    if sys.platform not in ['win32', 'linux']:
        raise Exception("Unsupported sys.platform: {}".format(sys.platform))

    if sys.platform == 'win32':
        bin = os.path.join(args.virtualenv, 'Scripts')
    else:
        bin = os.path.join(args.virtualenv, 'bin')

    activate = os.path.join(bin, 'activate')

    pip.main(['install', '--user', 'virtualenv'])

    virtualenv_command = [sys.executable, '-m', 'virtualenv', '--system-site-packages', args.virtualenv]
    returncode = subprocess.call(virtualenv_command)

    if returncode != 0:
        raise Exception("Received return code {} when running {}"
                        .format(result.returncode, virtualenv_command))

    virtualenv_python = os.path.realpath(os.path.join(bin, 'python'))
    virtualenv_python_command = [virtualenv_python,
                                 myfile,
                                 '--bin', bin,
                                 '--activate', activate,
                                 '--in-virtual']
    returncode = subprocess.call(virtualenv_python_command)

    sys.exit(returncode)
else:
    def setup(path):
        backup = os.getcwd()
        os.chdir(path)
        run_setup(os.path.join(path, 'setup.py'), script_args=['develop'])
        os.chdir(backup)

    src = os.path.join(mydir, args.virtualenv, 'src')
    os.makedirs(src, exist_ok=True)

    # Install Git dependencies
    git_repos = {
#        'canmatrix': 'https://github.com/ebroecker/canmatrix.git',
#        'bitstruct': 'https://github.com/altendky/bitstruct.git'
    }

    if len(git_repos) > 0:
        pip.main(['install', 'gitpython'])
        import git

        for name, url in git_repos.items():
            dir = os.path.join(src, name)
            git.Repo.clone_from(url, dir)
            setup(dir)

    # Install Zip dependencies
    zip_repos = {
#        'bitstruct': 'https://github.com/altendky/bitstruct/archive/'
#                     'a1dff1f96e8b113fefb7296e637c010654e1a6a6.zip'
    }

    if len(zip_repos) > 0:
        pip.main(['install', 'requests'])
        import requests
        import zipfile
        import io
        import shutil
        for name, url in zip_repos.items():
            response = requests.get(url)
            zip_data = io.BytesIO()
            zip_data.write(response.content)
            zip_file = zipfile.ZipFile(zip_data)
            zip_dir = os.path.split(zip_file.namelist()[0])[0]
            zip_file.extractall(path=src)
            shutil.move(os.path.join(src, zip_dir),
                        os.path.join(src, name))
            setup(os.path.join(src, name))

    # TODO: Figure out why this can't be moved before other installs
    #       Dependencies maybe?
    try:
        setup(mydir)
    except FileNotFoundError:
        pass

    activate = args.activate
    if sys.platform == 'win32':
        with open(os.path.join(mydir, 'activate.bat'), 'w') as f:
            activate = activate.replace('\\', '/')
            f.write('{}\n'.format(activate))

    with open(os.path.join(mydir, 'activate'), 'w', newline='') as f:
        f.write('source {}\n'.format(activate))

    print('')
    print('')
    print('    To use the new virtualenv:')
    print('')
    print('        posix: source activate')
    if sys.platform == 'win32':
        print('        win32: activate')
    print('')

    sys.exit(0)
