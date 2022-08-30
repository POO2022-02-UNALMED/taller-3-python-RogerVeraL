
class TV:
    numTV=0
    def __init__(self,marca,estado) :
        self.marca=marca
        self.estado=estado
        self.control=None
        self.canal=1
        self.precio=500
        self.volumen=1
        TV.numTV+=1

    def getMarca (self):
        return self.marca
    def setMarca (self,marca):
        self.marca=marca
    
    def getEstado (self):
        return self.estado
    def setEstado (self,estado):
        self.estado=estado
    
    def getControl (self):
        return self.control
    def setControl (self,control):
        self.control=control

    def getCanal (self):
        return self.canal
    def setCanal (self,canal):
        if 0<=canal<=120 and self.getEstado()==True:
            self.canal=canal

    def getPrecio (self):
        return self.precio
    def setPrecio (self,precio):
        self.precio=precio

    def getNumTV(self):
        return self.numTV
    def setNumTV(self,numTV):
        self.numTV=numTV

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
        