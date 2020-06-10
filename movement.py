from parser import FeatureObject
from time import sleep
import pigpio

pi = pigpio.pi()

def move(obj):
	left = obj.left
	right = obj.right
	
	if (left + right) // 2 < 416 // 3:
		moveLeft()
		
	elif (416 * 2) // 3 > (left + right) // 2 > 416 // 3:
		moveForward()
			
	else:
		moveRight()






def moveForward():
	print("MOVE FORWARD!!!")
	
	pi.write(23,1)
	pi.write(24,0)
	pi.set_PWM_dutycycle(25, 120)
	pi.write(17,1)
	pi.write(27,0)
	pi.set_PWM_dutycycle(22, 120)
	sleep(0.5)
	
	pi.write(23,0)
	pi.write(24,0)
	pi.set_PWM_dutycycle(25, 0)
	pi.write(17,0)
	pi.write(27,0)
	pi.set_PWM_dutycycle(22, 0)

	
	
	
def moveLeft():
	print("MOVE LEFT!!!")
	pi.write(23,0)
	pi.write(24,1)
	pi.set_PWM_dutycycle(25, 120)
	pi.write(17,1)
	pi.write(27,0)
	pi.set_PWM_dutycycle(22, 120)
	sleep(0.2)
	
	pi.write(23,0)
	pi.write(24,0)
	pi.set_PWM_dutycycle(25, 0)
	pi.write(17,0)
	pi.write(27,0)
	pi.set_PWM_dutycycle(22, 0)
	
	
	
	
	
def moveRight():
	print("MOVE RIGHT!!!")
	pi.write(23,1)
	pi.write(24,0)
	pi.set_PWM_dutycycle(25, 120)
	pi.write(17,0)
	pi.write(27,1)
	pi.set_PWM_dutycycle(22, 120)
	sleep(0.2)
	
	pi.write(23,0)
	pi.write(24,0)
	pi.set_PWM_dutycycle(25, 0)
	pi.write(17,0)
	pi.write(27,0)
	pi.set_PWM_dutycycle(22, 0)
