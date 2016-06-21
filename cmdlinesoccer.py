#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Attempts to orchestrate createthefile and followthefile.
Intended flow: create a blank live_matchThread.txt file, write data to it, read the file, sleep(30), write data to file. """

import subprocess

subprocess.call(['touch' , 'live_matchThread.txt'])
subprocess.call(['python' , 'createthefile.py'])
subprocess.call(['python' , 'followthefile.py'])

try:
    while True:
        import createthefile
        subprocess.call(['python', 'followthefile.py'])
        time.sleep(30)
except KeyboardInterrupt:
    print 'Exiting'
