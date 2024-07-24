LED = board.digital[2]
LED.write(0)

while not button_state:
    time.sleep(0.01)
    print("waiting for the button to be pressed")
    button_state = buttonA.read()

print()