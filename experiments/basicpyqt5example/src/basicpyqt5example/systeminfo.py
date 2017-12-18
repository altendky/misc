import pathlib
import sys

import PyQt5.QtCore
import PyQt5.uic
import sip


system_info = f'''\
sys.version: {sys.version}
sys.platform: {sys.platform}
QT_VERSION_STR: {PyQt5.QtCore.QT_VERSION_STR}
PYQT_VERSION_STR: {PyQt5.QtCore.PYQT_VERSION_STR}
SIP_VERSION_STR: {sip.SIP_VERSION_STR}'''


class SystemInfoDialog:
    def __init__(self):
        self.ui = PyQt5.uic.loadUi(
            pathlib.Path(__file__).parents[0] / 'systeminfo.ui',
        )

        self.ui.label.setText(system_info)
