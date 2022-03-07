class ProcessData:
    def __init__(self, serverConection, arrayFilter) -> None:
        self.serverConection = serverConection
        self.arrayFilter = arrayFilter
        pass

    def sendData(self, value):
        for a in self.arrayFilter:
            value = a.processNewData(value)
            type = a.getType()
            # print(f"value:{value}\ttype:{type}")
            self.serverConection.sendToServer(value, type)
    pass
