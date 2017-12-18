import sys

import PyQt5.QtWidgets

import basicpyqt5example.mainwindow


def main():
    app = PyQt5.QtWidgets.QApplication(sys.argv)

    main_window = basicpyqt5example.mainwindow.MainWindow()
    main_window.ui.show()

    app.exec()

    return 0


if __name__ == '__main__':
    sys.exit(main())
