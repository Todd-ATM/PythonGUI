import sys
from PySide6.QtWidgets import  QApplication, QWidget, QLabel, QInputDialog, QVBoxLayout


#set main Application using Pythons Sys arguments
app = QApplication(sys.argv)

#set window to object of QWidget
window = QWidget()
window.setWindowTitle("My First GUI App")
window.resize(300, 200)
label = QLabel(window)
label.setText("Hello")
label.alignment()
#create vertical layout, add our label to it
layout = QVBoxLayout(window)
layout.addWidget(label)
window.show()

app.exec()




