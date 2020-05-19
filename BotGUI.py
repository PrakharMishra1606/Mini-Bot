from FinalBot import Ui_BotMainWindow
from PyQt5.QtWidgets import * #QApplication, QMainWindow, QLabel
from PyQt5.QtCore import * #Qt 
from PyQt5.QtGui import *
import sys
import pickle as pk

#gui=QApplication(sys.argv)

class Worker(QRunnable):

    def __init__(self,fn,x):
        super(Worker,self).__init__()
        self.Fn=fn
        self.x=x

    def run(self):
        self.Fn(self.x)

            

class BotGui(QMainWindow,Ui_BotMainWindow):

    def __init__(self,*args,**kwargs):

        super(BotGui,self).__init__()
        self.setupUi(self)

        toolbar=QToolBar("Main Toolbar")
        self.addToolBar(toolbar)


        self.threadpool=QThreadPool()

        self.show()


    def Update(self,val):
        if (val[0]==2 and val[1]==2 and val[2]==2 and val[3]==2):
            self.Movement.setText("FORWARDS")
        elif (val[0]==2 and val[1]==0 and val[2]==0 and val[3]==2):
            self.Movement.setText("FORWARD RIGHT DIAGONAL")
        elif (val[0]==2 and val[1]==1 and val[2]==1 and val[3]==2):
            self.Movement.setText("RIGHT")
        elif (val[0]==0 and val[1]==1 and val[2]==1 and val[3]==0):
            self.Movement.setText("BACKWARD RIGHT DIAGONAL")
        elif (val[0]==1 and val[1]==1 and val[2]==1 and val[3]==1):
            self.Movement.setText("BACKWARDS")
        elif (val[0]==1 and val[1]==0 and val[2]==0 and val[3]==1):
            self.Movement.setText("BACKWARD LEFT DIAGONAL")
        elif (val[0]==1 and val[1]==2 and val[2]==2 and val[3]==1) :
            self.Movement.setText("LEFT")
        elif (val[0]==0 and val[1]==2 and val[2]==2 and val[3]==0):
            self.Movement.setText("FORWARD LEFT DIAGONAL")
        elif (val[0]==1 and val[1]==2 and val[2]==1 and val[3]==2):
            self.Movement.setText("ROTATING TOWARDS LEFT")
        elif (val[0]==2 and val[1]==1 and val[2]==2 and val[3]==1):
            self.Movement.setText("ROTATING TOWARDS RIGHT")    
        else:
            self.Movement.setText("NOT MOVING")    
        self.FrontLeft.setText(str(val[4]))
        self.FrontRight.setText(str(val[5]))
        self.RearLeft.setText(str(val[6]))
        self.RearRight.setText(str(val[7]))   
                        
                

    def AcceptValues(self):
        try:
            QApplication.processEvents()
            fp=open("guidata.pkl")
            val=pk.load(fp)
            fp.close()
            worker=Worker(self.Update,val)     
            self.threadpool.start(worker)
        except:
            pass

        


# window=BotGui()
# window.show()
# window.AcceptValues()
# gui.exec_()