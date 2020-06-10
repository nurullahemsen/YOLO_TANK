import pexpect
import sys
from picamera import PiCamera
import threading
from time import sleep
import os, fcntl
import cv2
from shutil import copyfile
from parser import parseObject, FeatureObject, mainObject
from movement import move

def Main():
    iframe = 0

    camera = PiCamera()

    camera.resolution = (416, 416)

    camera.capture('frame.jpg')
    sleep(0.1)


    iframe = 0
    child = pexpect.spawnu('bash')
    child.logfile = sys.stdout
    child.sendline("./darknet detect ./cfg/yolov3-tiny.cfg ./yolov3-tiny.weights -thresh 0.15")
    
    while(True):
      child.expect("Enter Image Path")
      child.sendline("frame.jpg")
      sleep(0.1)
        
      
      try:
        obj = mainObject("/home/pi/Desktop/deneme.txt")
        print(obj.confidence)
        move(obj)
          
      except Exception as e:
        print(str(e));
      
      im = cv2.imread('predictions.png')
      cv2.imshow('yolov3-tiny',im)
      key = cv2.waitKey(20)
      camera.capture('frame.jpg')

            











