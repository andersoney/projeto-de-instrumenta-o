import time
import serial
# import serial.tools.list_ports as port_list
# ports = list(port_list.comports())

comport = serial.Serial('COM6', 9600)
time.sleep(1.8)  # Entre 1.5s a 2s


def writeSerialPort(entrada: str) -> str:
    PARAM_CARACTER = bytes(entrada, 'UTF-8')
    # Time entre a conexao serial e o tempo para escrever (enviar algo)
    print(PARAM_CARACTER)
    comport.write(PARAM_CARACTER)


def readSerialPort() -> str:
    # comport.write(PARAM_ASCII)
    VALUE_SERIAL = comport.readline()
    VALUE_SERIAL = VALUE_SERIAL.decode("utf-8")
    return VALUE_SERIAL


for a in range(1000):
    # leitura1 = readSerialPort()
    # print(leitura1)
    writeSerialPort("100")
    # leitura1=leitura1.split(":")[1]
    # temperatura=float(leitura1.split("-")[0]);
    # pressao=float(leitura1.split("-")[1]);
    # print(f"Retorno da serial: {leitura1}\ttemperatura: {temperatura} \tpressão: {pressao}")
comport.close()
