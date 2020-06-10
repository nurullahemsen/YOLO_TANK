import pigpio
import time
import pexpect
import sys

iframe = 0
child = pexpect.spawnu('bash')
child.logfile = sys.stdout
child.sendline("sudo pigpiod")

time.sleep(1)

pi = pigpio.pi()
pi.set_PWM_dutycycle(25, 0)

def init():
	for i in range(255):
		pi.set_PWM_dutycycle(25, i)
		time.sleep(0.02)
		print(i)	
	for j in range(255, 0, -1):
		pi.set_PWM_dutycycle(25, j)
		time.sleep(0.02)
		print(j)
	pi.set_PWM_dutycycle(25, 0)
	
	#child = pexpect.spawnu('bash')
	#child.logfile = sys.stdout
	child.sendline("sudo killall pigpiod")
	
init()
