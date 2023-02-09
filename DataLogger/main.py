from serialApp import *
from writeFiles import *
from datetime import *

file = f'{date.today()}.txt'

# Cria o objeto para classe serialclearApp
serial = serialApp()

# Cria o arquivo .txt
create(file)

# Realiza um update das portas seriais
update = serial.updatePort()

# Definir baudrate e porta serial
serial.serialPort.port = update[0]
serial.serialPort.baudrate = 9600

# Conexão
serial.connectSerial()

# Recebe e escreve às informações da serial
while True:
    write(file, str(serial.readSerial()))

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
# serial.closeSerial()
