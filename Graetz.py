import numpy as np
from CoolProp.CoolProp import PropsSI
import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5 import uic
import hxlib.group as cv
from hxlib import group


UI = 'C:/파이썬/UI/Graetz.ui'




class Graetz(QDialog):
  
    def __init__(self):
        super().__init__()
        uic.loadUi(UI, self)
        self.setting()
        
    def setting(self):
        self.check.clicked.connect(self.Graetz)

    def Graetz(self):
        # fluid, T, V, D, x, P=101325
        fluid = self.fluid_2.currentText()
        T = float(self.T.text())
        V = float(self.V.text())
        D=float(self.D.text())
        P = float(self.P.text())
        x = float(self.x.text())
        Re,Pr,k = group.Reynolds(fluid, T, V, D, P=P)
        Pr = group.Reynolds(fluid, T, V, D, P=P)
      
        
        
        Gz = (D/x)*Re*Pr
        
    
    
    
        self.Result.setText(str(Gz))
        self.Result2.setText(str(Re))
        self.Result3.setText(str(Pr))
        self.Result4.setText(str(k))
        

app = QApplication(sys.argv)
ex = Graetz()
ex.show()
sys.exit(app.exec_())


