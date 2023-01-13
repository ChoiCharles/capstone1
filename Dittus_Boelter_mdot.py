import numpy as np
from CoolProp.CoolProp import PropsSI
import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5 import uic
import hxlib.group as cv
from hxlib import group


UI = 'C:/파이썬/UI/Dittus_Boelter_mdot.ui'




class Dittus_Boelter_mdot(QDialog):
  
    def __init__(self):
        super().__init__()
        uic.loadUi(UI, self)
        self.setting()
        
    def setting(self):
        self.check.clicked.connect(self.Dittus_Boelter_mdot)

    def Dittus_Boelter_mdot(self):
        # fluid, T, V, D, x, P=101325
        fluid = self.fluid_2.currentText()
        Tm = float(self.Tm.text())
        Ts = float(self.Ts.text())
        Dh=float(self.Dh.text())
        Ac = float(self.Ac.text())
        mdot = float(self.mdot.text())
        P= float(self.P.text())
        rho = PropsSI('D', 'T', Tm, 'P', P, fluid)
        V = mdot/(rho*Ac)
        Re,Pr,k = group.Reynolds(fluid, Tm, V, Dh, P=P)
        
        
        
        n = 0.4 if Ts > Tm else 0.3
        Nu = 0.023*Re**(4/5)*Pr**n
        h = k*Nu/Dh
        

       
    
    
    
        self.Result.setText(str(Nu))
        self.Result2.setText(str(Re))
        self.Result3.setText(str(h))
       
        

app = QApplication(sys.argv)
ex = Dittus_Boelter_mdot()
ex.show()
sys.exit(app.exec_())