"""This is the file that attempts to do a tail -f on the file written in by createthefile.py """

import time

def follow(thefile):
    thefile.seek(0,0)
    while True:
	line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

if __name__ == '__main__':
    logfile = open("live_matchThread.txt", "r")
    loglines = follow(logfile)
    for line in loglines:
        print line
