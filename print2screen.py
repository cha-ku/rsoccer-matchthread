#!/usr/bin/env python
# -*- coding: utf-8 -*-

getUrl = raw_input("Enter the match thread url: ")

if __name__ == '__main__':
    import get_soccer_update as update
    import praw
    import time
    import os

    def dostuff(url):
        r = praw.Reddit(user_agent = 'cmdlinesoccer')
        match_thread = update.UrlRoutine(url , r)
        KickOff_index = update.getOpeningMin(match_thread)
        update.justPrintIt(match_thread, KickOff_index)

    while True:
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
            dostuff(getUrl)
            time.sleep(30)
        except KeyboardInterrupt:
            print "Back to work, eh?"
            break
