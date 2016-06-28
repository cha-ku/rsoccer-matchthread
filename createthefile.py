#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This writes to a live_matchThread.txt"""

getUrl = raw_input("Enter the match thread url: ")

if __name__ == '__main__':
    import get_soccer_update as update
    import praw
    import time

    def dostuff(url):
        r = praw.Reddit(user_agent = 'cmdlinesoccer')
        match_thread = update.UrlRoutine(url , r)
        KickOff_index = update.getOpeningMin(match_thread)
        update.printToFile(match_thread, KickOff_index)

    dostuff(getUrl)
