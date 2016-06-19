#!/usr/bin/env python
# -*- coding: utf-8 -*-

import praw
from urlparse import urlparse
import time
import re

sleepytime = 30
r = praw.Reddit(user_agent = 'cmdlinesoccer')
getUrl = raw_input("Enter the match thread url: ")

def UrlRoutine(thrd_url):
    """ Returns the selftext  """
    football_url = urlparse(thrd_url)
    mtch_slftxt = r.get_submission(submission_id = football_url.path.split('/')[4])
    return mtch_slftxt

def getOpeningMin(mtch_thread_by_submission):
    getKickOff_index = mtch_thread_by_submission.selftext.lower().find("match events")
    if (getKickOff_index == -1):
        getKickOff_index = mtch_thread_by_submission.selftext.lower().find("0'")
        if (getKickOff_index == -1):
            getKickOff_index = mtch_thread_by_submission.selftext.lower().find("1'")
        else:
            getKickOff_index = mtch_thread.selftext.lower().find(raw_input("Input the starting word of the match events : "))
    return getKickOff_index

def CleanseAndPrint(match_thread , match_events_index):
    """ Removes a bunch of unnecessary parts []#sprite6-p177 and []#icon-sub-big """
    dirty_match_thread = match_thread.selftext[match_events_index : ]
    clean_match_thread = re.sub(r'\[\]\([^)]*\)', '', dirty_match_thread)
    return clean_match_thread

try:
    while True:
        mtch_thread = UrlRoutine(getUrl)
        KickOff_index = getOpeningMin(mtch_thread)
        # print(mtch_thread.selftext[KickOff_index : ])
        print CleanseAndPrint(mtch_thread , KickOff_index)
        time.sleep(sleepytime)
except KeyboardInterrupt:
    print 'Back to work, eh?'
