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
x0 = 0
x1 = 0
y0 = 0
y1 = 0
a = 0.6
b = 0.5
i = 0
while True:
    estadoBotao1 = valD7.read()
    if(estadoBotao1 == None):
        continue
    x1 = x0
    x0 = estadoBotao1
    y = 0
    if(i == 0):
        y = 0
    elif(i == 0):
        y = (a+b)*y0
    else:
        y = (a+b)*y0-a*b*y1+(1-a-b+a*b)*x1
    y1 = y0
    y0 = y
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
