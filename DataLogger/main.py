from datetime import *
from serialApp import *
from writeFiles import *
import keyboard

file = f'{date.today()}.txt'

# Create the Serial object
serial = serialApp()

# Create the .txt file
create(file)

# Check and Update Serial Ports
update = serial.updatePort()

# Define baudrate and Serial Port
serial.serialPort.port = update[0]
serial.serialPort.baudrate = 9600

# Open the Serial Port
serial.connectSerial()

# Receive and write to Serial information
while True:
    # Colect the Serial information and write in .txt file
    write(file, str(serial.readSerial()))

    # Check "esc" button to break while
    if keyboard.is_pressed("esc"):
        while True:
            # Wait for confirmation or not
            o = str(input("Stop? [Y/N]: ")).strip().upper()

            if o in "YN":
                break
            else:
                print("ERROR! Only Y or N!")

        if o == "Y":
            print("Exiting...")
            break
        else:
            print("Resuming...")

# Ended the Serial
serial.closeSerial()
print("Finished the program")
