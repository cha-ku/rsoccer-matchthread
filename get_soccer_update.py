#!/usr/bin/env python

import praw
from urlparse import urlparse
import time
#import pprint

"""thrd_url = raw_input("Enter the match thread url: ")
football_url = urlparse(thrd_url)
sub_id = football_url.path.split('/')[4]"""

sleepytime = 30
r = praw.Reddit(user_agent = 'cmdlinesoccer')
getUrl = raw_input("Enter the match thread url: ")

def UrlRoutine(thrd_url):
    football_url = urlparse(thrd_url)
#   sub_id = football_url.path.split('/')[4]
    mtch_slftxt = r.get_submission(submission_id = football_url.path.split('/')[4])
    return mtch_slftxt

def getOpeningMin(mtch_thread_by_submission):
    if (mtch_thread_by_submission.selftext.lower().find("0'") != -1):
        getKickOff_index = mtch_thread_by_submission.selftext.lower().find("0'")
    elif (mtch_thread.selftext.lower().find("1'") != -1):
        getKickOff_index = mtch_thread.selftext.lower().find("1'")
    else:
        getKickOff_index = mtch_thread.selftext.lower().find(raw_input("Input the word the live update starts with: "))
        return getKickOff_index


# mtch_thread = UrlRoutine(getUrl)

# KickOff_index = getOpeningMin(mtch_thread)

try:
    while True:
        mtch_thread = UrlRoutine(getUrl)
        KickOff_index = getOpeningMin(mtch_thread)
        print(chr(27) + "[2J")
        print(mtch_thread.selftext[KickOff_index : ])
        time.sleep(sleepytime)
except KeyboardInterrupt:
    print 'Back to work, eh?'
