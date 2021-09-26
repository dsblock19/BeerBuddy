# TEMP CONTROL FOR HOMEBREWING

'''LIBRARIES'''

import time
import board
from adafruit_onewire.bus import OneWireBus
from adafruit_ds18x20 import DS18X20
from digitalio import DigitalInOut, Direction


'''SETUP'''

# Constants
High = 72.0
Low = 64.0
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
    # Check Temp
    temp = ds18.temperature

    # If temp too hot, set machine to cool
    if temp > High:
        Cool = 1
    elif temp < High:
        Cool = 0

    # If temp too cold, set machine to heat
    if temp < Low:
        Heat = 1
    elif temp > Low:
        Heat = 0

    # If machine is set to heat
    if Heat == 1
        # Turn on heating pas
        heatPin = True
        while Heat == 1:
            temp = ds18.temperature
            if temp == Low + 2:
                Heat = 0
                heatPin = False
            else:
                time.sleep(30)

    # If machine is set to cool
    if Cool == 1
        # Turn on cooling pump
        coolPin = True
        while Cool == 1:
            temp = ds18.temperature
            if temp == High - 6):
                Cool = 0
                coolPin = False
            else:
                time.sleep(30)

    time.slep(1)
