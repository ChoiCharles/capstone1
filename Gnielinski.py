import numpy as np
from CoolProp.CoolProp import PropsSI
import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5 import uic
import hxlib.group as cv
from hxlib import group
from moody import moody


UI = 'C:/파이썬/UI/Gnielinski.ui'




class Gnielinski(QDialog):
  
    def __init__(self):
        super().__init__()
        uic.loadUi(UI, self)
        self.setting()
        
    def setting(self):
        self.check.clicked.connect(self.Gnielinski)

    def Gnielinski(self):
        # fluid, Tm, Ts, D, V, P=101325
        fluid = self.fluid_2.currentText()
        Tm = float(self.Tm.text())
        Ts = float(self.Ts.text())
        D=float(self.D.text())
        P = float(self.P.text())
        V = float(self.V.text())
        epsilon = float(self.epsilon.text())
        Re,Pr,k = group.Reynolds(fluid, Tm, V, D, P=P)
        

   
    
        
        RR = epsilon/D
        f = moody(Re, RR=RR)
        a1 = (f/8)*(Re - 1000)*Pr
        a2 = 1 + 12.7*(f/8)**(1/2)*(Pr**(2/3) - 1)
        Nu = a1/a2
        h = k*Nu/D
        
      
    
        self.Result.setText(str(Nu))
        self.Result2.setText(str(Re))
        self.Result3.setText(str(h))
        
        

app = QApplication(sys.argv)
ex = Gnielinski()
ex.show()
sys.exit(app.exec_())

