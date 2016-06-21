#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This writes to a live_matchThread.txt"""

if __name__ == '__main__':
    getUrl = raw_input("Enter the match thread url: ")

import get_soccer_update as update
import praw
import time

sleepytime = 30
r = praw.Reddit(user_agent = 'cmdlinesoccer')

match_thread = update.UrlRoutine(getUrl , r)
KickOff_index = update.getOpeningMin(match_thread)
update.printToFile(match_thread, KickOff_index)
