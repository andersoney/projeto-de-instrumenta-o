import requests
import time
from random import seed
from random import randint
from random import random

temperature = randint(10, 60)
pressure = randint(10, 60)
while True:
    pload = {
        "temperature": temperature
    }
    number = random()
    if(number > 0.5):
        temperature = temperature+1
    else:
        temperature = temperature-1
    pressureResponse = requests.post('http://localhost:8081/temperature', data=pload)
    print(pressureResponse.text)
    pload = {
        "pressure": pressure
    }
    number = random()
    if(number > 0.5):
        pressure = pressure+1
    else:
        pressure = pressure-1
    temperatureResponse = requests.post('http://localhost:8081/pressure', data=pload)
    print(temperatureResponse.text)
    time.sleep(1)
