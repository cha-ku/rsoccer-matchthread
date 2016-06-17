#!/usr/bin/env python

import praw
from urlparse import urlparse
#import pprint

thrd_url = raw_input("Enter the match thread url: ")
football_url = urlparse(thrd_url)
sub_id = football_url.path.split('/')[4]

r = praw.Reddit(user_agent = 'cmdlinesoccer')

mtch_thread = r.get_submission(submission_id = sub_id)

def getOpeningMin(mtch_thread_by_submission):
    if (mtch_thread_by_submission.selftext.lower().find("1'") != -1):
        getKickOff_index = mtch_thread_by_submission.selftext.lower().find("1'")
    elif (mtch_thread.selftext.lower().find("1'") != -1):
        getKickOff_index = mtch_thread.selftext.lower().find("1'")
    else:
        getKickOff_index = mtch_thread.selftext.lower().find(raw_input("Input the word the live update starts with: "))
    return getKickOff_index

KickOff_index = getOpeningMin(mtch_thread)

print(mtch_thread.selftext[KickOff_index : ])
