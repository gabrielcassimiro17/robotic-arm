from gpiozero import Servo
from time import sleep
import sys,tty,termios

S1 = Servo(23)
S2 = Servo(24)             

if __name__=='__main__':
    S1.value = 0
    S2.value = 0
    while True:

        print("enter value for servo 1")
        S1.value = input()
        print("enter value for servo 2")
        S2.value = input()