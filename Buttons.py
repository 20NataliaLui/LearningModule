from time import sleep
import board
from digitalio import DigitalInOut
from RPi import GPIO


# Touch Module Setup
pad_pin = board.D23
 
pad = DigitalInOut(pad_pin)
 
already_pressed = False

# Rotary Encoder Setup
clk = 17
dt = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

counter = 0
clkLastState = GPIO.input(clk)
finalClk = False

# Greeting Statement
print("Hello. Thank you for using Team251's Learning Module.\n");

# Infinite loop to run the program
mode = 0
print("Menu:\n1: Words\n2: Letters\n3: Numbers")

while True:
    while finalClk == False:
        clkState = GPIO.input(clk)
        dtState = GPIO.input(dt)
        if clkState != clkLastState:
            if dtState != clkState:
                mode += 1
                if mode == 1:
                    print("You are on mode " + str(mode) + ". Click the Touch Module to Continue")
                    if pad.value and not already_pressed:
                        print("Mode 1: Words")
                        sleep(3)
                        print("Cat")
                        sleep(3)
                        print("Bat")
                        sleep(3)
                        print("Dog")
                        already_pressed = pad.value
                elif mode == 2:
                    print("You are on mode " + str(mode) + ". Click the Touch Module to Continue")
                    if pad.value and not already_pressed:
                        print("Mode 2: Letters")
                        sleep(3)
                        print("A")
                        sleep(3)
                        print("B")
                        sleep(3)
                        print("C")
                        already_pressed = pad.value
                elif mode == 3:
                    print("You are on mode " + str(mode) + ". Click the Touch Module to Continue")
                    if pad.value and not already_pressed:
                        print("Mode 3: Numbers")
                        sleep(3)
                        print("1")
                        sleep(3)
                        print("2")
                        sleep(3)
                        print("3")
                        already_pressed = pad.value
                else:
                    print("Please go back, none of these modes exist")
            else:
                mode -= 1
                if mode == 1:
                    print("You are on mode " + str(mode) + ". Click the Touch Module to Continue")
                    if pad.value and not already_pressed:
                        print("Mode 1: Words")
                        sleep(3)
                        print("Cat")
                        sleep(3)
                        print("Bat")
                        sleep(3)
                        print("Dog")
                        pad.value = False
                elif mode == 2:
                    print("You are on mode " + str(mode) + ". Click the Touch Module to Continue")
                    if pad.value and not already_pressed:
                        print("Mode 2: Letters")
                        sleep(3)
                        print("A")
                        sleep(3)
                        print("B")
                        sleep(3)
                        print("C")
                        already_pressed = pad.value
                elif mode == 3:
                    print("You are on mode s" + str(mode) + ". Click the Touch Module to Continue")
                    if pad.value and not already_pressed:
                        print("Mode 3: Numbers")
                        sleep(3)
                        print("1")
                        sleep(3)
                        print("2")
                        sleep(3)
                        print("3")
                        already_pressed = pad.value
                else:
                    print("Please go back, none of these modes exist")

clkLastState = clkState


