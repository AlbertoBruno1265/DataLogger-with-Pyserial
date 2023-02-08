from serialApp import *
from arquivo import *
from datetime import *
from time import sleep

arq = f'{date.today()}.txt'
# Cria o objeto para classe serialclearApp
ser = serialApp()

# Cria o arquivo .txt
criar(arq)

# Realiza um update das portas seriais
u = ser.updatePort()

print(u)

# Definir baudrate e porta serial
ser.serialPort.port = 'COM5'
ser.serialPort.baudrate = 9600

# Conexão
ser.connectSerial()

# Recebe e escreve às informações da serial
while True:
    escrever(arq, str(ser.readSerial()))

    # #Envio de msg UDP
    #
    # escrever(arq, "UDP Send")
    # print(f'{str(datetime.today())[0:str(datetime.today()).find(".")]} -> UDP Send')
    #
    # client_socket.sendto(bytesToSend, serverAddressPort)  # Send the data request
    # sleep(3)
    # try:
    #     rec_data1, addr = client_socket.recvfrom(2048)  # Read response from arduino
    #
    #     if (rec_data1 != " "):
    #         escrever(arq, str(rec_data1))
    #         print(f'{str(datetime.today())[0:str(datetime.today()).find(".")]} -> {rec_data1}')
    #
    # except:
    #     print(f'{str(datetime.today())[0:str(datetime.today()).find(".")]} -> Erro na recepcao')
    #     pass

# Finaliza a serial
# ser.closeSerial()
