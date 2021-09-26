# TEMP CONTROL FOR HOMEBREWING

'''LIBRARIES'''

import time
import board
from adafruit_onewire.bus import OneWireBus
from adafruit_ds18x20 import DS18X20
from digitalio import DigitalInOut, Direction


'''SETUP'''

# Constants
High = 0.0
Low = 0.0
Heat = 0
Cool = 0

# Temp Sensing
# Initialize one-wire bus on board pin D5.
ow_bus = OneWireBus(board.D5)
# Scan for sensors and grab the first one found.
ds18 = DS18X20(ow_bus, ow_bus.scan()[0])

# Heating
heatPin = DigitalInOut(board.D5)
heatPin.direction = Direction.OUTPUT

# Cooling
coolPin = DigitalInOut(board.D6)
coolPin.direction = Direction.OUTPUT

'''LOOP'''

while True:
    temp = ds18.temperature

    if temp > High:
        Cool = 1
    elif temp < High:
        Cool = 0

    if temp < Low:
        Heat = 1
    elif temp > Low:
        Heat = 0

    if Heat = 1
        heatPin = True
    elif Heat = 0
        heatPin = False

    if Cool = 1
        coolPin = True
    elif Cool = 0
        coolPin = False

    time.slep(1)
