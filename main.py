import sys
from PySide6.QtWidgets import  QApplication, QWidget, QLabel, QInputDialog, QVBoxLayout, QPushButton


#set main Application using Pythons Sys arguments
app = QApplication(sys.argv)

#set window to object of QWidget
window = QWidget()
window.setWindowTitle("My First GUI App")
window.resize(300, 200)

#create label and pushbutton
label = QLabel(window)
label.setText("Hello")
button = QPushButton("text", window)

#create vertical layout, add our label and button to it
layout = QVBoxLayout(window)
layout.addWidget(label)
layout.addWidget(button)
window.show()

app.exec()




