#!/usr/bin/env python
# -*- coding: utf-8 -*-

import praw
from urlparse import urlparse
import time

sleepytime = 30
r = praw.Reddit(user_agent = 'cmdlinesoccer')
getUrl = raw_input("Enter the match thread url: ")

def UrlRoutine(thrd_url):
    """ Returns the selftext  """
    football_url = urlparse(thrd_url)
    mtch_slftxt = r.get_submission(submission_id = football_url.path.split('/')[4])
    return mtch_slftxt

def getOpeningMin(mtch_thread_by_submission):
    """ Searches for the opening minute ( 0' or 1') in the selftext.
    If not found, asks for the starting word of the match events"""
    if (mtch_thread_by_submission.selftext.lower().find("0'") != -1):
        getKickOff_index = mtch_thread_by_submission.selftext.lower().find("0'")
    elif (mtch_thread.selftext.lower().find("1'") != -1):
        getKickOff_index = mtch_thread.selftext.lower().find("1'")
    else:
        getKickOff_index = mtch_thread.selftext.lower().find(raw_input("Input the starting word of the match events : "))
    return getKickOff_index


try:
    while True:
        mtch_thread = UrlRoutine(getUrl)
        KickOff_index = getOpeningMin(mtch_thread)
        print(mtch_thread.selftext[KickOff_index : ])
        time.sleep(sleepytime)
except KeyboardInterrupt:
    print 'Back to work, eh?'
