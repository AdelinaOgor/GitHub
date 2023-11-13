#importing modules and widgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout,QHBoxLayout, QPushButton, QLabel, QLineEdit, QListWidget
 
#declaring constants
win_width, win_height = 800, 300
win_x, win_y = 200, 200
txt_title = "Sending text"
txt_line = "Entry field"
 
class MainWindow(QWidget):
    value = 0
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        # creating and customizing the graphical elements:
        self.initUI()
        #connects the elements
        self.connects()
 
        #determines how the window will look (text, size, location)
        self.set_appear()
 
        # start:
        self.show()
 
    def initUI(self):
        ''' creates graphical elements '''
        self.my_list = QListWidget()
        self.lable_intrebare = QLabel("Intrebare 1")
        self.lable_raspunsC = QLabel('Intrebare 2')
        self.lable_raspunsG1 = QLabel('Intrebare 3')
        self.lable_raspunsG2 = QLabel('Intrebare 4')
        self.lable_raspunsG3 = QLabel('Intrebare 5')

        self.lable_intrebareC = QLineEdit()
        self.lable_intrebareG1 = QLineEdit()
        self.lable_intrebareG2 = QLineEdit()
        self.lable_intrebareG3 = QLineEdit()
        self.lable_intrebareG4 = QLineEdit()
        self.lable_intrebareG5 = QLineEdit()

        self.btn_question = QPushButton("New Question", self)
        self.btn_delet = QPushButton("Delete Question", self)
        self.btn_begin = QPushButton("Begin practice", self)
        self.layout_main = QVBoxLayout()
 
        self.layout_main.addWidget(self.my_list, alignment = Qt.AlignLeft)
        self.layout_main.addWidget(self.btn_question, alignment = Qt.AlignCenter)

        self.layout_main.addWidget(self.lable_intrebareC, alignment = Qt.AlignRight)
        self.layout_main.addWidget(self.lable_intrebareG1, alignment = Qt.AlignRight)
        self.layout_main.addWidget(self.lable_intrebareG2, alignment = Qt.AlignRight)
        self.layout_main.addWidget(self.lable_intrebareG3, alignment = Qt.AlignRight)
        self.layout_main.addWidget(self.lable_intrebareG4, alignment = Qt.AlignRight)
        self.layout_main.addWidget(self.lable_intrebareG5, alignment = Qt.AlignRight)

        layoutHB = QHBoxLayout()
        layoutHB.addWidget(self.btn_delet, alignment = Qt.AlignCenter) 
        layoutHB.addWidget(self.btn_begin, alignment = Qt.AlignCenter)  
 
        self.layout_main.addLayout(layoutHB)
        layoutH = QHBoxLayout()
        layoutV1 = QVBoxLayout()

        my_elements = [self.lable_intrebare, self.lable_raspunsC, self.lable_raspunsG1, self.lable_raspunsG2, self.lable_raspunsG3]
        for elemet in my_elements:
            layoutV1.addWidget(elemet, alignment = Qt.AlignRight)

        layoutH.addLayout(layoutV1)



        self.layout_main.addLayout(layoutH)
 
               
        self.setLayout(self.layout_main)
 
 
    def connects(self):
        # Nu need for the buttons to do something in this exercise/nothing to add here 
        pass
 
    ''' determines how the window will look (text, size, location) '''
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
 
 
def main():
    app = QApplication([])
    mw = MainWindow()
    app.exec_()
 
main()