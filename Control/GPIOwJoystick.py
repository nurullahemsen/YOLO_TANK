import pigpio
import time
import pexpect
import sys
from inputs import get_gamepad

def translate(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)

def move(event):
	if (event.code == "ABS_X"):
		if(100 < event.state < 156):
			pi.write(23,0)
			pi.write(24,0)
			pi.set_PWM_dutycycle(25, 0)
			pi.write(17,0)
			pi.write(27,0)
			pi.set_PWM_dutycycle(22, 0)
		elif(event.state >= 156):
			pi.write(23,1)
			pi.write(24,0)
			value = translate(event.state,157,255,70,255)
			pi.set_PWM_dutycycle(25, value)
			pi.write(17,0)
			pi.write(27,1)
			pi.set_PWM_dutycycle(22, value)
			return 0
		elif(event.state <= 100):
			pi.write(23,0)
			pi.write(24,1)
			value = translate(event.state,100,0,70,255)
			pi.set_PWM_dutycycle(25, value)
			pi.write(17,1)
			pi.write(27,0)
			pi.set_PWM_dutycycle(22, value)
			return 0
	
	if (event.code == "ABS_Y"):
		print(event.state)
		if(100 < event.state < 156):
			pi.write(23,0)
			pi.write(24,0)
			pi.set_PWM_dutycycle(25, 0)
			pi.write(17,0)
			pi.write(27,0)
			pi.set_PWM_dutycycle(22, 0)
		elif(event.state >= 156):
			pi.write(23,1)
			pi.write(24,0)
			value = translate(event.state,157,255,70,255)
			pi.set_PWM_dutycycle(25, value)
			pi.write(17,1)
			pi.write(27,0)
			pi.set_PWM_dutycycle(22, value)
		elif(event.state <= 100):
			pi.write(23,0)
			pi.write(24,1)
			value = translate(event.state,100,0,70,255)
			pi.set_PWM_dutycycle(25, value)
			pi.write(17,0)
			pi.write(27,1)
			pi.set_PWM_dutycycle(22, value)
		#pi.write(23,0)
		#pi.write(24,1)
		#pi.set_PWM_dutycycle(25, event.state)
		
def initializePigpiod():
	child = pexpect.spawnu('bash')
	child.logfile = sys.stdout
	child.sendline("sudo pigpiod")
	time.sleep(1)

initializePigpiod()

pi = pigpio.pi()
pi.set_PWM_dutycycle(25, 0)
pi.set_mode(23, pigpio.OUTPUT)
pi.set_mode(24, pigpio.OUTPUT)
pi.set_PWM_dutycycle(22, 0)
pi.set_mode(17, pigpio.OUTPUT)
pi.set_mode(27, pigpio.OUTPUT)

def init():	
	while 1:
		events = get_gamepad()
		for event in events:
			print(event.code, event.state)
			if(event.code == "BTN_TOP" and event.state == 0):
				pi.set_PWM_dutycycle(25, 0)
				pi.write(23,0)
				pi.write(24,0)
				pi.set_PWM_dutycycle(22, 0)
				pi.write(17,0)
				pi.write(27,0)
				return 0
			move(event)
	

	
init()
