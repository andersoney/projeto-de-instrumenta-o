import time
from random import seed
from random import randint
from random import random
from librarys import NormalizerDigitalFilter, NormalizeLastNumber, ProcessData, WithOutFilter, ServerConnection, SerialConnection
# from librarys import NormalizeLastNNumber

temperature = randint(10, 60)
pressure = randint(10, 60)

withOutFilterTemperature = WithOutFilter()
normalizeDigitalFilterTemperature = NormalizerDigitalFilter(0.6, 0.5)
normalizeAVGTemperature = NormalizeLastNumber(3)

withOutFilter = WithOutFilter()
normalizeDigitalFilter = NormalizerDigitalFilter(0.8, 0.5)
normalizeAVG = NormalizeLastNumber(3)

arrayFilterTemperature = [withOutFilterTemperature,
                          normalizeDigitalFilterTemperature, normalizeAVGTemperature]
arrayFilter = [withOutFilter, normalizeDigitalFilter, normalizeAVG]

serverTemperature = ServerConnection('http://localhost:8081/'+'temperature')
dataProcessorTemperature = ProcessData(
    serverTemperature, arrayFilterTemperature)
serverPressure = ServerConnection('http://localhost:8081/'+'pressure')
dataProcessorPressure = ProcessData(
    serverPressure, arrayFilter)
serialConection = SerialConnection('COM3', 9600)
while True:
    temperature
    number = random()
    number2 = random()
    changeValue = 0.1
    temperature, pressure = serialConection.readTemperaturePressure()
    print(f"temperatura: {temperature} \tpressão: {pressure}")
    # break;
    if(number2 > 0.9):
        print("*******************Adicionando Ruido")
        dataProcessorTemperature.sendData(temperature+60)
        number3 = randint(0, 1)
        dataProcessorPressure.sendData(pressure+(-1**number3)*80)
        continue
    # if(number > 0.5):
    #     temperature = temperature+changeValue
    # else:
    #     temperature = temperature-changeValue
    # if(temperature > 1):
    #     temperature = 1
    # elif(temperature < 0):
    #     temperature = 0
    dataProcessorTemperature.sendData(temperature)
    dataProcessorPressure.sendData(pressure)
    time.sleep(0.3)
