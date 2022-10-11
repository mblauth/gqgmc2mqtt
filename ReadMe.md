# GQ GMC 2 MQTT

This script takes Geiger counter readings from GQ's GMC models and publishes
them to an MQTT broker. This was only tested using a GQ GMC-300E plus.

## Usage

```
main.py [-h] -broker BROKER [-port PORT] -topic TOPIC [-baudrate BAUDRATE] [-serial SERIAL]

send GQ GMC events to MQTT

options:
  -h, --help          show this help message and exit
  -broker BROKER      the hostname or IP address of the MQTT broker
  -port PORT          the port of the MQTT broker (default: 1883)
  -topic TOPIC        the MQTT topic on which to publish
  -baudrate BAUDRATE  the baudrate of the serial interface (default: 57600)
  -serial SERIAL      the serial interface to the GQ GMC Geiger Counter (default: /dev/ttyUSB0)
```