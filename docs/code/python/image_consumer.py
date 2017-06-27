﻿'''
image_consumer.py
author: Johannes Wagner <wagner@hcm-lab.de>

Copyright (C) University of Augsburg, Lab for Human Centered Multimedia

Output image on the console.
'''


import cv2
import numpy

def getOptions(opts, vars):

    opts['title'] = ''
    opts['x'] = 0
    opts['y'] = 0


def setImageFormatIn(format, opts, vars): 
    
    print(format)    


def consume_enter(sins, board, opts, vars):
    
    cv2.namedWindow(opts['title'])
    cv2.moveWindow(opts['title'], opts['x'], opts['y'])    
    cv2.resizeWindow(opts['title'], sins[0].width, sins[0].height)


def consume(info, sins, board, opts, vars): 

    img = numpy.asarray(sins[0])
    cv2.flip(img, 0, img)

    cv2.imshow(opts['title'], img)
    cv2.resizeWindow(opts['title'], sins[0].width, sins[0].height)
    cv2.waitKey(1)


def consume_flush(sins, board, opts, vars):
    
    cv2.destroyWindow(opts['title'])