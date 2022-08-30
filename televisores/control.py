#from marca import Marca
#from tv import TV

class Control():
    #tv=TV()
    def __init__(self):
        self._tv = None
        
    def getTv(self):
        return self.tv
    def setTv(self,tv):
        self.tv=tv
    
    def turnOn(self):
        self.turnOn()
    def turnOff(self):
        self.turnOff()

    def setCanal(self,canal):
        self.canal=canal
    def canalUp(self):
        self.canalUp()
    def canalDown(self):
        self.canalDown()

    def volumenUp(self):
        self.volumenUp()
    def volumenDown(self):
        self.volumenDown()
    
    def enlazar(self,tv):
        self.tv=tv
        tv.setControl(self)
