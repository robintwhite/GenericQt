# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
import sys
import os
import gui
import random
from PIL import Image
import pandas as pd
import time

#All functions defined in App class
class AnalysisApp(QtWidgets.QDialog, gui.Ui_Dialog):
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        self.setupUi(self)
        
        #Initialize click objects
        self.pushButton.clicked.connect(self.analysis)
        self.pushButton_2.clicked.connect(self.quitClicked)
        self.toolButton.clicked.connect(self.HelpApp) #See code below for popup
        
        #Default text box values
        self.lineEdit.setText(os.getcwd())
        self.lineEdit_2.setText(os.getcwd())
        self.lineEdit_3.setText(time.strftime("%Y%m%d-%H%M%S")+'output.csv')
    
    #Save file function to handle seperate exception
    def save_file_toCSV(self, data, filename):
        try:
            data.to_csv(filename)
            print(filename)
        except(PermissionError, AttributeError, FileNotFoundError):
            self.output.setText("{0}".format('Please input a valid save location'))
            
    
    def analysis(self):
        #Analysis to be run when start analysis button pressed
        option = self.checkBox.isChecked()
        num = self.spinBox.value()
        input_image_file = self.lineEdit.text()
        save_loc = self.lineEdit_2.text()
        save_name = self.lineEdit_3.text()
        #Will need some check if the image can be found and if all inputs are satisfied
        #Can use
        try:
            img = Image.open(input_image_file)
            #img=mpimg.imread('stinkbug.png')
            self.widget_2.canvas.ax = self.widget_2.canvas.fig.add_subplot(111)
            self.widget_2.canvas.ax.imshow(img)
            self.widget_2.canvas.draw()
            
            #Plot data
            data = [random.random() for i in range(25)]
            self.widget.canvas.ax = self.widget.canvas.fig.add_subplot(211)
            self.widget.canvas.ax.cla() #clear axes for each plot
            self.widget.canvas.ax.plot(data, 'r-')
            self.widget.canvas.ax.set_title('Example')
            self.widget.canvas.ax = self.widget.canvas.fig.add_subplot(212)
            self.widget.canvas.ax.cla()
            self.widget.canvas.ax.plot(data, 'r-')
            self.widget.canvas.ax.set_title('Example')
            self.widget.canvas.draw()
            
            #Output to console
            #Must be string type
            self.textBrowser.setText("{0}{1}\n{2}".format('This is an example output: ', num, 'New line'))
            
            df = pd.DataFrame(({'col':data}))
            if option:
                self.save_file_toCSV(df, os.path.join(save_loc,save_name))
    
        
        #Errors for image input       
        except (PermissionError, AttributeError, FileNotFoundError):
            self.textBrowser.setText("{0}".format('Please input a valid image'))
            
    def HelpApp(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle(self.tr("Help"))
        msgBox.setText("<br>"+
                       "<b>{0}</b><br><br>".format('This is some bold text') +
                       "{0}<br>".format('This is some normal text')+
                       "{0}<br>{1}<br><br>".format('This is some more normal text','new line')+
                       "&copy;2017<br><br>")
        msgBox.setInformativeText("This is additional information")

        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)

        msgBox.exec_()
        
    def quitClicked(self):
        sys.exit()
        

def main():
    app = QtWidgets.QApplication(sys.argv)
    form = AnalysisApp()
    form.show()
    app.exec_()
    
if __name__ == '__main__':
    main()