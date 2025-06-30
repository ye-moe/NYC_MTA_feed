# HelloWorld PyQt
import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget

app = QApplication(sys.argv)
window = QWidget()
label = QLabel('Hello World', window)
window.setWindowTitle('HelloGUI with Qt')
window.resize(320, 240)
window.show()
app.exec()