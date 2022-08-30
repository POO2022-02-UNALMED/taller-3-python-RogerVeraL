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
        self._tv.turnOn()
    def turnOff(self):
        self._tv.turnOff()

    def setCanal(self,canal):
        self._tv.setCanal(canal)
    def canalUp(self):
        self._tv.canalUp()
    def canalDown(self):
        self._tv.canalDown()

    def volumenUp(self):
        self._tv.volumenUp()
    def volumenDown(self):
        self._tv.volumenDown()
    
    def enlazar(self,tv):
        self._tv=tv
        tv.setControl(self)
