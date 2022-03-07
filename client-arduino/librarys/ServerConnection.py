
import requests

class ServerConnection:
    def __init__(self, url) -> None:
        self.cleanDataServer();
        self.url = url
        pass

    def sendToServer(self, value, type):
        payLoad = {
            "value": value,
            "type": type
        }
        # print(f"{type}:\nSimples: {ploadSimple}\t Normalized: {ploadNormalized}")
        responseSimple = requests.post(
            self.url, data=payLoad)
        pass
    def cleanDataServer(self):
        pload = {
        }
        temperatureResponse = requests.post(
            'http://localhost:8081/clean', data=pload)
        pass;