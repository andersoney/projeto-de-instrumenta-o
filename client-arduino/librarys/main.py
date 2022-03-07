

class NormalizerDigitalFilter:
    def __init__(self, a, b) -> None:
        self.x0 = 0
        self.x1 = 0
        self.y0 = 0
        self.y1 = 0
        self.a = a
        self.b = b
        self.i = 0

    def processNewData(self, data):
        self.x1 = self.x0
        self.x0 = data
        self.y = 0
        if(self.i == 0):
            self.y = 0
        elif(self.i == 0):
            self.y = (self.a+self.b)*self.y0
        else:
            self.y = (self.a+self.b)*self.y0-self.a*self.b * \
                self.y1+(1-self.a-self.b+self.a*self.b)*self.x1
        self.y1 = self.y0
        self.y0 = self.y
        self.i = self.i+1
        return self.y
    def getType(self):
        return "Normalized"
    pass


class NormalizeLastNumber:
    def __init__(self, qty) -> None:
        self.arrValueX = []
        self.qty = qty

    def processNewData(self, data):
        self.arrValueX.append(data)
        self.arrValueX = self.arrValueX[-self.qty:]
        return sum(self.arrValueX)/len(self.arrValueX)

    def getType(self):
        return "AVG"
    pass


class WithOutFilter:
    def __init__(self) -> None:
        pass

    def processNewData(self, data):
        return data

    def getType(self):
        return "Simple"
    pass
