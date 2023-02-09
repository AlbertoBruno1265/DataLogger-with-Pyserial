from datetime import *
from serialApp import *
from writeFiles import *
import keyboard

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

    if keyboard.is_pressed("esc"):
        while True:
            o = str(input("Tem certeza que quer sair? [Y/N]: ")).strip().upper()

            if o in "YN":
                break
            else:
                print("Tecla errada, apenas Y ou N!")

        if o == "Y":
            print("Saindo...")
            break
        else:
            print("Continuando...")

# Finaliza a serial
serial.closeSerial()
print("Finalizado o programa")
