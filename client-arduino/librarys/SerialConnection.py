import time
import serial


class SerialConnection:
    def __init__(self, port, bround) -> None:
        self.comport = serial.Serial(port, bround)
        pass

    def readSerialPort(self, entrada: str) -> str:
        PARAM_CARACTER = bytes(entrada, 'UTF-8')
        # Time entre a conexao serial e o tempo para escrever (enviar algo)
        time.sleep(1.8)  # Entre 1.5s a 2s
        self.comport.write(PARAM_CARACTER)
        # comport.write(PARAM_ASCII)
        VALUE_SERIAL = self.comport.readline()
        VALUE_SERIAL = VALUE_SERIAL.decode("utf-8")
        return VALUE_SERIAL

    def readTemperaturePressure(self):
        leitura1 = self.readSerialPort("TP")
        leitura1 = leitura1.split(":")[1]
        temperatura = float(leitura1.split("-")[0])
        pressao = float(leitura1.split("-")[1])
        # print(
        #     f"Retorno da serial: {leitura1}temperatura: {temperatura} \tpressão: {pressao}")
        return temperatura, pressao
    pass
