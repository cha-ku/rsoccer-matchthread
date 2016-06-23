#!/usr/bin/env python
# -*- coding: utf-8 -*-
import praw
from urlparse import urlparse
import time
import re
#import os

def UrlRoutine(thrd_url , red):
    """ Returns the selftext  """
    football_url = urlparse(thrd_url)
    mtch_slftxt = red.get_submission(submission_id = football_url.path.split('/')[4])
    return mtch_slftxt

def getOpeningMin(mtch_thread_by_submission):
    """Checks for "Match Events" or "0'" or "1'" to get to the match events section"""
    getKickOff_index = mtch_thread_by_submission.selftext.lower().find("match events")
    if (getKickOff_index == -1):
        getKickOff_index = mtch_thread_by_submission.selftext.lower().find("0'")
        if (getKickOff_index == -1):
            getKickOff_index = mtch_thread_by_submission.selftext.lower().find("1'")
        else:
            manual_entry = raw_input("Input the starting word of the match events : ")
            getKickOff_index = mtch_thread_by_submission.selftext.lower().find(manual_entry)
    return getKickOff_index

def CleanseAndPrint(match_thread , match_events_index):
    """ Removes a bunch of unnecessary parts such as []#sprite6-p177 and []#icon-sub-big from the selftext """
    dirty_match_thread = match_thread.selftext[match_events_index : ]
    clean_match_thread = re.sub(r'\[\]\([^)]*\)', '', dirty_match_thread)
    return clean_match_thread

# def printToFile(mtch_thread , KO_indx):
#     livetextfile = open("live_matchThread.txt","w")
#     #livetextfile.truncate()
#     livetext = CleanseAndPrint(mtch_thread , KO_indx)
#     livetextfile.write(str(livetext.encode('utf-8')))
#     #livetextfile.close()

def justPrintIt(mtch_thread, KO_indx):
    while True:
        print CleanseAndPrint(mtch_thread , KO_indx)
        time.sleep(30)
        # except KeyboardInterrupt:
        #     print "Back to work, eh!?"
