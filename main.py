import sys
from PySide6.QtWidgets import  QApplication, QWidget, QLabel, QInputDialog


#set main Application using Pythons Sys arguments
app = QApplication(sys.argv)

#set window to object of QWidget
window = QWidget()
window.setWindowTitle("My First GUI App")
window.resize(300, 200)
label = QLabel(window)
label.setText("Hello")
label.alignment()
text,ok = QInputDialog.getText(window, "Question", "Do you like fries?")
window.show()

app.exec()




