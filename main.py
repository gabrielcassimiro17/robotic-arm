from gpiozero import Servo
from time import sleep
import sys,tty,termios

S1 = Servo(23)
S2 = Servo(24)
class _Getch:
    def __call__(self):
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                ch = sys.stdin.read(3)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return ch

def get():
    inkey = _Getch()
    while(1):
        k=inkey()
        if k!='':break
    if k=='\x1b[A':
        return 'up'
    elif k=='\x1b[B':
        return "down"
    elif k=='\x1b[C':
        return "right"
    elif k=='\x1b[D':
        return "left"
    else:
        print("not an arrow key!")
                

if __name__=='__main__':
    S1.value = 0
    S2.value = 0
    while True:

        key_entry = get()
        if key_entry == 'up':
            S1.value =+ 0.2
            sleep(1)
            S2.value =+ 0.1
            sleep(1)
        elif key_entry == 'down':
            S1.value =- 0.2
            sleep(1)
            S2.value =- 0.1
            sleep(1)
        
