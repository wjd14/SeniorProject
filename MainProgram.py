import math
import numpy as np
import signal
import sys
import time
import serial

#serial connections for the sensors
compass = serial.Serial('')
gps = serial.Serial('')
lidar = serial.Serial('')

#serial connection to the arduino controlling the robot
controlArduino = serial.Serial('COM3')

#"neutral" values that tell the robot to do nothing.
jsx_center = 127
jsy_center = 127


#gps location variables for determining where we want to go
location = 5

desired_location = 7

#Handy for breaking out of loops manually using CTRL-C on Mac, or CTRL-Pause on Windows
def sigint_handler(signal, frame):
    print ('KeyboardInterrupt is caught')
    lidar.stop()
    lidar.stop_motor()
    lidar.disconnect()
    sys.exit(0)


#use pyserial to read the GPS
def readGPSData():


    return data

#use pyserial to read the Compass

def readCompassData():

    return data

#use pyserial to read the Lidar

def readLidarData():
    scans = []
    for i, scan in enumerate(lidar.iter_scans()):
       scans.append(scan)
       if i > 2:
           break
    return scans

#analyze the lidar data to see if we are clear, blocked by a post, wall, or maze
def identifyObstacles(input_data):
    
    # lots of math

    return result

#this likely needs to be hashed out better. compute course the robot should take
def computeCourse(inputs):

    #lots of math and logic

    return x_val, y_val


#convert numbers into bytes, send to the arduino
def sendCommand(x_val, y_val):
    x = jsx_center + x_val
    y = jsy_center + y_val

    command = 256 * x + y

    controlArduino.write(bytes(str(command), 'utf-8'))

#if off by > 5 degrees and we're not on a path to avoid an obstacle, stop
# giong forward and turn ourselves until we are aligned with desired direction
def computeTurn(inputs):

    while(not on course):
        turn
    return


def checkIfThere(current_location):

    if current_location = desired_location:
        return True
    else:
        return False
    


signal.signal(signal.SIGINT, sigint_handler)


while True:

    #main body of the program
