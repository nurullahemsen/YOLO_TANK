from picamera import PiCamera
from subprocess import Popen, PIPE
import threading
from time import sleep
import os, fcntl
import cv2
from shutil import copyfile
from Tools.parser import FeatureObject, mainObject
from Tools.movement import move

iframe = 0

camera = PiCamera()

camera.resolution = (416, 416)

camera.capture('frame.jpg')
sleep(0.1)


iframe = 0

while True:
    try:
        yolo_proc = Popen(["./darknet",
                   "detect",
                   "./cfg/yolov3-tiny.cfg",
                   "./yolov3-tiny.weights",
                   "-thresh","0.1"],
                   stdin = PIPE, stdout = PIPE, text = True)
                   
                   
        obj = mainObject("/home/pi/Desktop/deneme.txt")
        try:
            print(obj.confidence)
            move(obj)
            
            
            
            
        except Exception:
            pass
        
        
        stdout = yolo_proc.communicate(input='frame.jpg')
        print('ne')
        if 'Enter Image Path' in stdout[0]:
            print('ne')
            try:
               im = cv2.imread('predictions.png')
               cv2.imshow('yolov3-tiny',im)
               key = cv2.waitKey(500)
               camera.capture('frame.jpg')
            except Exception:
               pass
            
    except Exception:
        pass
