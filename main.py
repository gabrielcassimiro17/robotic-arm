from gpiozero import Servo
from time import sleep
import sys,tty,termios
import numpy as np

S1 = Servo(23)
S2 = Servo(24)             

def calculate_angles(distance_horizontal):
    """ Calculate angles for inverse kinematics"""
    dist_a = 8.5
    dist_b = 12
    dist_c = np.sqrt(dist_a**2 + dist_b**2)

    angle_a = np.arccos((dist_b**2 + dist_c**2 - dist_a**2)/(2*dist_b*dist_c))
    angle_b = np.arccos((dist_a**2 + dist_c**2 - dist_b**2)/(2*dist_a*dist_c))
    angle_c = np.arccos((dist_a**2 + dist_b**2 - dist_c**2)/(2*dist_a*dist_b))

    angle_a = np.rad2deg(angle_a)
    angle_b = np.rad2deg(angle_b)
    angle_c = np.rad2deg(angle_c)

    # scale angles to fit servos between -1 and 1
    angle_a = (angle_a - 90) / 180 # not needed
    angle_b = (angle_b - 90) / 180
    angle_c = (angle_c - 90) / 180
    
    return angle_b, angle_c


if __name__=='__main__':
    S1.value = 0
    S2.value = 0
    # while True:
    movment = [16.7, 14.7, 12.7, 11.7, 12.7, 14.7]
    
    print("enter number of iterations")

    iteration = range(0, int(input()))
    
    for i in iteration:
        for distance in movment:
            angle1, angle2 = calculate_angles(distance)
    
            S1.value = angle1
            S2.value = angle2

