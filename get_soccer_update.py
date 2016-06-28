#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urlparse import urlparse
import time
import re

def url_routine(thrd_url , red):
    """ Returns the selftext  """
    football_url = urlparse(thrd_url)
    mtch_slftxt = red.get_submission(submission_id = football_url.path.split('/')[4])
    return mtch_slftxt

def get_opening_min(mtch_thread_by_submission, manual_entry):
    """Directly asks user for the match events keyword"""
    getKickOff_index = mtch_thread_by_submission.selftext.lower().find(manual_entry.lower())
    return getKickOff_index

def clean_and_print(match_thread , match_events_index):
    """ Removes a bunch of unnecessary parts such as []#sprite6-p177 and []#icon-sub-big from the selftext """
    dirty_match_thread = match_thread.selftext[match_events_index : ]
    clean_match_thread = re.sub(r'\[\]\([^)]*\)', '', dirty_match_thread)
    return clean_match_thread

def just_print(mtch_thread, KO_indx):
    print clean_and_print(mtch_thread , KO_indx)
    time.sleep(30)
