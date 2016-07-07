import functools
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton

app = QApplication(sys.argv)

red = "background-color:red;"
green = "background-color:green;"
blue = "background-color:blue;"
widget = QWidget()
layout = QVBoxLayout()
widget.setLayout(layout)

button = QPushButton()
button.setText("Red")
button.clicked.connect(functools.partial(
    widget.setStyleSheet, red))
layout.addWidget(button)

button = QPushButton()
button.setText("Green")
button.clicked.connect(functools.partial(
    widget.setStyleSheet, green))
layout.addWidget(button)

button = QPushButton()
button.setText("Blue")
button.clicked.connect(functools.partial(
    widget.setStyleSheet, blue))
layout.addWidget(button)

widget.showFullScreen()
widget.show()
app.exec_()
