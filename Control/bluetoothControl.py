import serial
import time
import pigpio
import pexpect
import sys

ser = 1

for i in range(5):
    txt = "/dev/rfcomm{index}"
    try:
        ser = serial.Serial(txt.format(index = i), baudrate=9600)
        break
    except Exception:
        print(txt.format(index = i), " is not used trying another...")

# ~ while True:
    # ~ if (36 != int.from_bytes(ser.read() , "big")):
        # ~ continue
    # ~ x = ser.read()          # read one byte
    # ~ print(int.from_bytes(x, "big"))

def translate(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)

def move(x,y):
    if(100 < x < 156):
        pi.write(23,0)
        pi.write(24,0)
        pi.set_PWM_dutycycle(25, 0)
        pi.write(17,0)
        pi.write(27,0)
        pi.set_PWM_dutycycle(22, 0)
    elif(x >= 156):
        pi.write(23,1)
        pi.write(24,0)
        value = translate(x,157,255,70,255)
        pi.set_PWM_dutycycle(25, value)
        pi.write(17,0)
        pi.write(27,1)
        pi.set_PWM_dutycycle(22, value)
        return 0
    elif(x <= 100):
        pi.write(23,0)
        pi.write(24,1)
        value = translate(x,100,0,70,255)
        pi.set_PWM_dutycycle(25, value)
        pi.write(17,1)
        pi.write(27,0)
        pi.set_PWM_dutycycle(22, value)
        return 0
    

    print(y)
    if(100 < y < 156):
        pi.write(23,0)
        pi.write(24,0)
        pi.set_PWM_dutycycle(25, 0)
        pi.write(17,0)
        pi.write(27,0)
        pi.set_PWM_dutycycle(22, 0)
    elif(y >= 156):
        pi.write(23,1)
        pi.write(24,0)
        value = translate(y,157,255,70,255)
        pi.set_PWM_dutycycle(25, value)
        pi.write(17,1)
        pi.write(27,0)
        pi.set_PWM_dutycycle(22, value)
    elif(y <= 100):
        pi.write(23,0)
        pi.write(24,1)
        value = translate(y,100,0,70,255)
        pi.set_PWM_dutycycle(25, value)
        pi.write(17,0)
        pi.write(27,1)
        pi.set_PWM_dutycycle(22, value)
        
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
        if (36 != int.from_bytes(ser.read() , "big")):
            continue
        x = ser.read()          # read one byte
        x = int.from_bytes(x, "big")
        print(x)
        # ~ time.sleep(0.005)
        y = ser.read()          # read one byte
        y = int.from_bytes(y, "big")
        print(y)
        END = int.from_bytes(ser.read(), "big")
        if(END == 0):
            pi.set_PWM_dutycycle(25, 0)
            pi.write(23,0)
            pi.write(24,0)
            pi.set_PWM_dutycycle(22, 0)
            pi.write(17,0)
            pi.write(27,0)
            print("Session Ended.")
            return 0
        if (35 != int.from_bytes(ser.read() , "big")):
            continue
            
        move(x,y)
        
        

    

    
init()
