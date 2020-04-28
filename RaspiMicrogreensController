import RPi.GPIO as GPIO
import time
import schedule
import pygame
import math
import datetime
import dht11

def initialization():
    GPIO.setmode(GPIO.BOARD)

    # remember to add dht11.py to the folder for this program.

    GPIO.setup(7, GPIO.OUT)  # this is the light
    GPIO.setup(5, GPIO.OUT)  # this is the fan
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)

    GPIO.output(7, 1)
    GPIO.output(5, 1)
    GPIO.output(11, 1)

def lightOn():
    GPIO.output(7, 0)
    print("Light on")

def lightOff():
    GPIO.output(7, 1)
    print("Light off")

def fanOn():
    GPIO.output(5, 0)
    print("Fan on")

def fanOff():
    GPIO.output(5, 1)
    print("Fan off")

def istimeright():
    thetimeis = datetime.datetime.now().strftime("%H%M")
    return (thetimeis)
def start_up_test():
    lightOff()
    fanOff()
    time.sleep(2)
    lightOn()
    fanOn()


def instansiate_dht11():
    instance = dht11.DHT11(pin=3)
    return instance

def lightSetTime(startTime, endTime, startTime2, endTime2):
    instance = instansiate_dht11()
    startTime = startTime * 100
    endTime = endTime * 100
    
    theTimeIs = int(istimeright())
    result = instance.read()
    print("Start")
    print(theTimeIs)
    print(datetime.datetime.now().strftime("%H:%M"))
    if (theTimeIs >= startTime and theTimeIs <= endTime) or (theTimeIs >= startTime2 and theTimeIs <= endTime2):
	lightOn()
	print("Last valid input: " + str(datetime.datetime.now()))
	print("Temperature: %d C" % result.temperature)
	print("Temperature: %d F" % ((result.temperature * 9 / 5) + 32))
	print("Humidity: %d %%" % result.humidity)
    
    else:
	lightOff()
	print("Pi is in sleep mode.")

    # run fan every set time
    # if theTimeIs >= 1255 and theTimeIs <= 1300:
    #     fanOn()
    # elif theTimeIs >= 1355 and theTimeIs <= 1400:
    #     fanOn()
    # elif theTimeIs >= 1455 and theTimeIs <= 1500:
    #     fanOn()
    # elif theTimeIs >= 1555 and theTimeIs <= 1600:
    #     fanOn()
    # elif theTimeIs >= 1655 and theTimeIs <= 1700:
    #     fanOn()
    # elif theTimeIs >= 1755 and theTimeIs <= 1800:
    #     fanOn()
    # elif theTimeIs >= 1855 and theTimeIs <= 1900:
    #     fanOn()
    # elif theTimeIs >= 1955 and theTimeIs <= 2000:
    #     fanOn()
    # elif theTimeIs >= 2050 and theTimeIs <= 2100:
    #     fanOn()
    #     print("fanOn")
    # else:
    #     fanOff()
    # print("End")

    time.sleep(5)
	

def main():
    initialization()
    start_up_test()
    time.sleep(5)
    
    # run this line forever
    while True:
	lightSetTime(6,11,19,23)
	
        

if __name__ == "__main__":
    main()
