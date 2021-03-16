from time import sleep
from playsound import playsound
import psutil
import os

# Change the path to the location of your 'sound.mp3' file
path = ''
os.chdir(path)
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
