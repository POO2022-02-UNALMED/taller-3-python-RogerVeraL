from televisores.control import Control
from televisores.marca import Marca
class TV:
    _numTV=0
    def __init__(self,marca,estado) :
        self._marca=marca
        self._estado=estado
        self._control=None
        self._canal=1
        self._precio=500
        self._volumen=1
        TV._numTV+=1

    def getMarca (self):
        return self._marca
    def setMarca (self,marca):
        self._marca=marca
    
    def getEstado (self):
        return self._estado
    def setEstado (self,estado):
        self._estado=estado
    
    def getControl (self):
        return self._control
    def setControl (self,control):
        if isinstance(control, Control):
            self._control = control

    def getCanal (self):
        return self._canal
    def setCanal (self,canal):
        if 0<=canal<=120 and self.getEstado()==True:
            self._canal=canal

    def getPrecio (self):
        return self._precio
    def setPrecio (self,precio):
        self._precio=precio

    @classmethod
    def getNumTV(cls):
        return cls._numTV
    @classmethod
    def setNumTV(cls,numTV):
        cls._numTV=numTV

    def getVolumen(self):
        return self._volumen
    def setVolumen(self, volumen):
        if self.getEstado()==True and 0<=volumen<=7:
            self._volumen = volumen
    
    def turnOn(self):
        self.setEstado(True)
    def turnOff(self):
        self.setEstado(False)

    def canalUp(self):
        if 0<=self.getCanal()<120 and self.getEstado()==True:
            self.setCanal(self.getCanal()+1)
    def canalDown(self):
        if 0<self.getCanal()<=120 and self.getEstado()==True:
            self.setCanal(self.getCanal()-1)
        
    def volumenUp(self):
        if 0<=self.getVolumen()<7 and self.getEstado()==True:
            self.setVolumen(self.getVolumen()+1)
    def volumenDown(self):
        if 0<self.getVolumen()<=7 and self.getEstado()==True:
            self.setVolumen(self.getVolumen()-1)
        