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


def light_on():
    GPIO.output(7, 0)
    print("Light on")


def light_off():
    GPIO.output(7, 1)
    print("Light off")


def fanOn():
    GPIO.output(5, 0)
    print("Fan on")


def fanOff():
    GPIO.output(5, 1)
    print("Fan off")


def istimeright():
    the_time_is = datetime.datetime.now().strftime("%H%M")
    return the_time_is


def start_up_test():
    light_off()
    fanOff()
    time.sleep(2)
    light_on()
    fanOn()


def instansiate_dht11():
    instance = dht11.DHT11(pin=3)
    return instance


def light_set_time(start_time, end_time, start_time2, end_time2):
    instance = instansiate_dht11()
    start_time = start_time * 100
    end_time = end_time * 100
    start_time2 = start_time2 * 100
    end_time2 = end_time2 * 100

    the_time_is = int(istimeright())
    result = instance.read()
    print("Start")
    print(the_time_is)
    print("Current Time:" + str(the_time_is))
    # print(datetime.datetime.now().strftime("%H:%M"))
    print("Start time 1: " + str(start_time))
    print("End time 1: " + str(end_time))
    print("Start time 2: " + str(start_time2))
    print("End time 2: " + str(end_time2))
    if ((the_time_is >= start_time) and (the_time_is <= end_time)) or (
            (the_time_is >= start_time2) and (the_time_is <= end_time2)):
        light_on()
        print("Last valid input: " + str(datetime.datetime.now()))
        print("Temperature: %d C" % result.temperature)
        print("Temperature: %d F" % ((result.temperature * 9 / 5) + 32))
        print("Humidity: %d %%" % result.humidity)

    else:
        light_off()
        print("Pi is in sleep mode.")

    # run fan every set time
    # if the_time_is >= 1255 and the_time_is <= 1300:
    #     fanOn()
    # elif the_time_is >= 1355 and the_time_is <= 1400:
    #     fanOn()
    # elif the_time_is >= 1455 and the_time_is <= 1500:
    #     fanOn()
    # elif the_time_is >= 1555 and the_time_is <= 1600:
    #     fanOn()
    # elif the_time_is >= 1655 and the_time_is <= 1700:
    #     fanOn()
    # elif the_time_is >= 1755 and the_time_is <= 1800:
    #     fanOn()
    # elif the_time_is >= 1855 and the_time_is <= 1900:
    #     fanOn()
    # elif the_time_is >= 1955 and the_time_is <= 2000:
    #     fanOn()
    # elif the_time_is >= 2050 and the_time_is <= 2100:
    #     fanOn()
    #     print("fanOn")
    # else:
    #     fanOff()
    # print("End")

    time.sleep(10)


def main():
    initialization()
    start_up_test()
    time.sleep(10)

    # run this line forever
    while True:
        light_set_time(6, 10, 11, 12)


if __name__ == "__main__":
    main()
