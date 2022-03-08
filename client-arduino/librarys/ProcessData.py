class ProcessData:
    def __init__(self, serverConection, arrayFilter) -> None:
        self.serverConection = serverConection
        self.arrayFilter = arrayFilter
        pass

    def sendData(self, value):
        for a in self.arrayFilter:
            new_value=value
            new_value = a.processNewData(new_value)
            type = a.getType()
            # print(f"value:{value}\ttype:{type}")
            self.serverConection.sendToServer(new_value, type)
    pass
