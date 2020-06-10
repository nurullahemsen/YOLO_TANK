import RPi.GPIO as GPIO 
from time import sleep 
from inputs import get_gamepad

while 1:
    events = get_gamepad()
    for event in events:
        #print(event.ev_type, event.code, event.state)
        print(event.code, event.state)
        #if (event.code == "BTN_TOP" and event.state == 1):
        #elif (event.code == "BTN_TOP" and event.state == 0):
	

