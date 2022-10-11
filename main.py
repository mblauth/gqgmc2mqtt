#! /usr/bin/env python

import signal
import time
import paho.mqtt.client

import serial

global con


def interrupt(sig, frame):
    print("execution interrupted, quitting")
    con.close()
    exit()


def main():
    global con
    con = serial.Serial("/dev/ttyUSB0", 57600)
    con.write("<GETVER>>".encode())
    version = con.read(14)
    print(version.decode())
    signal.signal(getattr(signal, 'SIGINT'), interrupt)

    mqtt = paho.mqtt.client.Client("mqtt")
    mqtt.connect("10.0.138.117", 1883)

    while True:
        con.write("<GETCPM>>".encode())
        value = ord(con.read(1))+ord(con.read(1))
        print(value)
        mqtt.publish("radiation/arbeitszimmer", value)
        time.sleep(60)


if __name__ == "__main__":
    main()
