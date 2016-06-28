#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Attempts to orchestrate createthefile and followthefile.
Intended flow: create a blank live_matchThread.txt file, write data to it, read the file, sleep(30), write data to file. """

from subprocess import call
import time
import createthefile

subprocess.call(['touch' , 'live_matchThread.txt'])
subprocess.call(['python' , 'createthefile.py'])
subprocess.call(['python' , 'followthefile.py'])

URLfromUser = createthefile.getURLfromUser()

try:
    while True:
        createthefile.dostuff(URLfromUser)
        subprocess.call(['python' , 'followthefile.py'])
        time.sleep(30)
        print "i overslept"
except KeyboardInterrupt:
    print 'Exiting'
