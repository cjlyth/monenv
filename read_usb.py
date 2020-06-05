#!/usr/bin/python
import os, sys
import serial
import time

ser = serial.Serial('/dev/ttyUSB0',115200, timeout = 5)

headerLineStart = 'rtcDate'
headerValue = ""
hasHeader = False

while True:
    line = ser.readline()
    
    if len(line) == 0:
        print("Time out! Exit.\n")
        sys.exit()
    
    if (hasHeader):
        print line,

    if (line.startswith(headerLineStart)):
        print "Header line: ", line
        headerValue = line
        hasHeader = True
