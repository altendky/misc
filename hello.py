from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
import sys

app = QApplication(sys.argv)

widget = QWidget()
layout = QVBoxLayout()
widget.setLayout(layout)
button = QPushButton()
button.setText("Hello EPC")
layout.addWidget(button)
button = QPushButton()
button.setText("The Middle")
layout.addWidget(button)
button = QPushButton()
button.setText("Goodbye EPC")
layout.addWidget(button)

widget.showFullScreen()
widget.show()
app.exec_()