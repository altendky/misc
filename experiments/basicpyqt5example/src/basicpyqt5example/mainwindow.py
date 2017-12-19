import pathlib

import PyQt5.uic

import basicpyqt5example.systeminfo


class MainWindow:
    def __init__(self):
        self.ui = PyQt5.uic.loadUi(
            pathlib.Path(__file__).parents[0] / 'mainwindow.ui',
        )

        self.ui.actionSystem_Info.triggered.connect(
            lambda: self.open_system_info(),
        )
        self.system_info_dialogs = []

    def open_system_info(self):
        dialog = basicpyqt5example.systeminfo.SystemInfoDialog()
        dialog.ui.finished.connect(lambda: self.close_system_info(dialog))
        dialog.ui.show()
        self.system_info_dialogs.append(dialog)

    def close_system_info(self, dialog):
        self.system_info_dialogs.remove(dialog)
        print(
            'removed {}, still have {}'.format(dialog, self.system_info_dialogs)
        )
