import serial
import serial.tools.list_ports

class serialApp():
    def __init__(self):
        self.serialPort = serial.Serial()
        self.baudrate = [9600]
        self.portlist = []

    # Metodo de update de portas seriais
    def updatePort(self):
        ports = [port.device for port in serial.tools.list_ports.comports()]
        self.portlist = ports
        print(ports)
        return ports

    # Conexão
    def connectSerial(self):
        try:
            self.serialPort.open()
        except:
            print('Ocorreu um erro ao abrir o serial!')

    # Receber dados
    def readSerial(self):
        from datetime import datetime
        try:
            dataRead = self.serialPort.readline().decode('utf-8')
        except UnicodeDecodeError:
            print(f'{str(datetime.today())[0:str(datetime.today()).find(".")]} -> ERRO! Linha ignorada!')
            msg = 'Mensagem com formato ilegível!'
            return msg
        else:
            msg = str(dataRead)
            print(f'{str(datetime.today())[0:str(datetime.today()).find(".")]} -> {msg}')
            return msg

    # Fechar conexão
    def closeSerial(self):
        self.serialPort.close()
