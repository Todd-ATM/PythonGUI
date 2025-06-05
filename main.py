import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QFrame

#set main Application using Pythons Sys arguments
app = QApplication(sys.argv)

#set window to object of QWidget
window = QWidget()
window.setWindowTitle("My First GUI App")
window.resize(300, 200)
label = QLabel(window)
label.setText("Hello")
window.show()

app.exec()




