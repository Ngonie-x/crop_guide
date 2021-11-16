from PyQt5 import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


from mainwindow import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.submitbtn.clicked.connect(self.submit)
        
        # add items to season combo box
        self.season_combobox.addItem("Summer")
        self.season_combobox.addItem("Autumn")
        self.season_combobox.addItem("Winter")
        
        # add items to state combo box
        self.state_combobox.addItem("Harare")
        self.state_combobox.addItem("Bulawayo")
        self.state_combobox.addItem("Manicaland")
        self.state_combobox.addItem("MashEast")
        self.state_combobox.addItem("Mash West")
        self.state_combobox.addItem("Matebeleland")
        
        
        
    def submit(self):
        print("Clicked")
        season = self.season_combobox.currentText()
        state = self.state_combobox.currentText()
        money = int(self.budget_lineedit.text())
        acres = int(self.acres_lineedit.text())   
        
        print("Season: ", season)
        print("State: ", state)     
        print("Budget: ", money)     
        print("Acres: ", acres)     
             
        
app = QApplication([])
window = MainWindow()
window.show()
app.exec_()