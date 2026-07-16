""" this is a pytthon script to test the drv8833 motor driver
to test 2 dc motors with gpiozero
"""
from gpiozero import Robot, Motor
from time import sleep
in1 = 14 # input 1
in2 = 15 # input 2
in3 = 18 # input 3
in4 = 23 # input 4
robot = Robot(left=Motor(in3, in4), right=Motor(in2, in1))
while True:
    robot.forward()
    print("motor moving forward")
    sleep(1)
    robot.right()
    print("motor moving rightwards")
    sleep(1)