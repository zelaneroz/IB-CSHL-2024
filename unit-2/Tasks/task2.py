from pyfirmata import Arduino
import time

board = Arduino('/dev/cu.usbserial-110')
print("Communication Successfully started")

while True:
    board.digital[2].write(1)