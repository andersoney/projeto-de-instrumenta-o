from pyfirmata import Arduino, util
import time
import requests

Uno = Arduino('COM3')
it = util.Iterator(Uno)
it.start()
pload = {
}
temperatureResponse = requests.post(
    'http://localhost:8081/clean', data=pload)
valD7 = Uno.get_pin('a:0:i')
a = [x for x in range(2, 14)]
# out=Uno.get_pin(f'd:13:o');
output = [Uno.get_pin(f'd:{x}:o') for x in a]
estadoBt1Ant = True
contador = 0
class Normalizer:
    def __init__(self) -> None:
        self.x0 = 0
        self.x1 = 0
        self.y0 = 0
        self.y1 = 0
        self.a = 0.6
        self.b = 0.5
        self.i = 0
    def processNewData(self,data):
        self.x1 = self.x0
        self.x0 = data
        self.y = 0
        if(self.i == 0):
            self.y = 0
        elif(self.i == 0):
            self.y = (self.a+self.b)*self.y0
        else:
            self.y = (self.a+self.b)*self.y0-self.a*self.b*self.y1+(1-self.a-self.b+self.a*self.b)*self.x1
        self.y1 = self.y0
        self.y0 = self.y
        return self.y;
        pass;
    pass;

while True:
    estadoBotao1 = valD7.read()
    if(estadoBotao1 == None):
        continue
    
    print(f"Y:{y:.4f}\tX:{x0:.4f}")
    # for out in output:
    #     out.write(1)

    # out.write(1)
    # time.sleep(estadoBotao1)
    # for out in output:
    #     out.write(0)
    # out.write(0)

    # number = random()
    # if(number > 0.5):
    #     temperature = temperature+1
    # else:
    #     temperature = temperature-1
    pload = {
        "temperature": f"{y0:.4f}"
    }
    temperatureResponse = requests.post(
        'http://localhost:8081/temperature', data=pload)
    pload = {
        "pressure": f"{x0:.4f}"
    }
    pressureResponse = requests.post(
        'http://localhost:8081/pressure', data=pload)
    i = i+1
    time.sleep(0.5)
