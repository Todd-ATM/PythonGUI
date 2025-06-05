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
button = QPushButton("text")

#create vertical layout, add our label and button to it
layout = QVBoxLayout(window)
layout.addWidget(label)
layout.addWidget(button)
#setup layout
layout.setSpacing(100)

#function that sets the label to a different text
def changeText():
    label.setText("Changed the Text of the label")

#setup our buttons connect signal to call changeText() function
button.clicked.connect(changeText)


window.show()

app.exec()




