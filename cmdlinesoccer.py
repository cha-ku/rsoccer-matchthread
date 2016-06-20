#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess

subprocess.call(['touch' , 'live_matchThread.txt'])
subprocess.call(['python' , 'createthefile.py'])
subprocess.call(['python' , 'followthefile.py'])

try:
    while True:
        subprocess.Popen(['python' , 'createthefile.py'])
        subprocess.call(['python', 'followthefile.py'])
        time.sleep(30)
except KeyboardInterrupt:
    print 'Exiting'
