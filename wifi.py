#!/usr/bin/env python
import os
import string
import parse

def name():
    return_code = os.popen("/sbin/iwconfig wlan0 | grep ESSID | cut -d'\"' -f2").read()
    output = str(return_code)
    output = output.strip()
    return output

def strength():
    return_code = os.popen("/sbin/iwconfig wlan0 | grep Signal").read()
    output = str(return_code)
    output = parse.sandwich('Signal level=','/100',output)
    output = int(output)
    return output

print 'network name: ' + name() + '\tsignal strength: ' + str(strength())
