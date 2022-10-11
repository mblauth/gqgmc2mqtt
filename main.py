#! /usr/bin/env python

import signal
import time
import paho.mqtt.client
import argparse
import serial


def interrupt(sig, frame):
    print("execution interrupted, quitting")
    con.close()
    exit()


def main():
    parser = argparse.ArgumentParser(description="send GQ GMC events to MQTT")
    parser.add_argument("-broker", type=str, nargs=1, required=True,
                        help="the hostname or IP address of the MQTT broker")
    parser.add_argument("-port", type=int, nargs=1, default=1883,
                        help="the port of the MQTT broker (default: 1883)")
    parser.add_argument("-topic", type=str, nargs=1, required=True,
                        help="the MQTT topic on which to publish")
    parser.add_argument("-baudrate", type=int, nargs=1, default=57600,
                        help="the baudrate of the serial interface (default: 57600)")
    parser.add_argument("-serial", type=str, nargs=1, default="/dev/ttyUSB0",
                        help="the serial interface to the GQ GMC Geiger Counter (default: /dev/ttyUSB0)")
    args = parser.parse_args()
    con = serial.Serial(args.serial, args.baudrate)
    con.write("<GETVER>>".encode())
    version = con.read(14)
    print(version.decode())
    signal.signal(getattr(signal, "SIGINT"), interrupt)

    mqtt = paho.mqtt.client.Client("mqtt")
    mqtt.connect(args.broker[0], args.port)

    while True:
        con.write("<GETCPM>>".encode())
        value = ord(con.read(1))+ord(con.read(1))
        print(value)
        mqtt.publish(parser.topic[0], value)
        time.sleep(60)


if __name__ == "__main__":
    main()
