from time import sleep
from playsound import playsound
import psutil
import os

os.chdir('C:/Users/S0gusjak/Documents/Charge')
was_plugged = False

print(os.path)

while True:

    battery = psutil.sensors_battery()
    plugged = battery.power_plugged

    if plugged:
        print("Plugged")
    else:
        print("Not plugged")
    
    if plugged != was_plugged:
        playsound('sound.mp3')

    was_plugged = plugged

    sleep(.1)