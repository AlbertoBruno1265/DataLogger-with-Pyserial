import serial
import serial.tools.list_ports

class serialApp():
    def __init__(self):
        self.serialPort = serial.Serial()
        self.baudrate = [9600]
        self.portlist = []

    # Opdate of Serial Ports
    def updatePort(self):
        ports = [port.device for port in serial.tools.list_ports.comports()]
        self.portlist = ports
        print(ports)
        return ports

    # Connection
    def connectSerial(self):
        try:
            self.serialPort.open()
        except:
            print('An error occurred while opening the Serial!')

    # Receive information of Serial
    def readSerial(self):
        from datetime import datetime
        try:
            dataRead = self.serialPort.readline().decode('utf-8')
        except UnicodeDecodeError:
            print(f'{str(datetime.today())[0:str(datetime.today()).find(".")]} -> ERROR! Skipped line!')
            msg = 'Message in unreadable format!'
        else:
            msg = str(dataRead)
            print(f'{str(datetime.today())[0:str(datetime.today()).find(".")]} -> {msg}')

        return msg

    # Close Serial
    def closeSerial(self):
        self.serialPort.close()
