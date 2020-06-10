from Main import Main
import pigpio
from time import sleep
import pexpect
import sys

child = pexpect.spawnu('bash')
child.logfile = sys.stdout
child.sendline("sudo pigpiod")
sleep(2)
pi = pigpio.pi()
pi.set_PWM_dutycycle(25, 0)
pi.set_mode(23, pigpio.OUTPUT)
pi.set_mode(24, pigpio.OUTPUT)
pi.set_PWM_dutycycle(22, 0)
pi.set_mode(17, pigpio.OUTPUT)
pi.set_mode(27, pigpio.OUTPUT)

Main()
