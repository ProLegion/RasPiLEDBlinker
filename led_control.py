#This program flashes an led connected to GIPO Pin 17 on the Raspberry PI

import gpiozero             #Importing LED functions from GIPO in Pyhton
import time                 #Import Sleep function

ledBlue = gpiozero.LED(17)  #Assign control of the pin to the variable, note this is referencing GIPO 17 not the pin#

while True:                 #Loop Always
    ledBlue.off()           #Start with LED OFF
    time.sleep(0.5)         #Wait half a second
    ledBlue.on()            #Turn the LED on
    time.sleep(0.5)         #Wait another half second
