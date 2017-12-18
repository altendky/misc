import setuptools

setuptools.setup(
    name='basicpyqt5example',
    author="Kyle Altendorf",
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
    ],
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'},
    entry_points={
        'gui_scripts': [
            'basicpyqt5example = basicpyqt5example.__main__:main',
        ],
    },
    install_requires=[
        'pyqt5',
    ],
)
