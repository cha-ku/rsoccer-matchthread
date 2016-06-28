#!/usr/bin/env python
# -*- coding: utf-8 -*-

import get_soccer_update as update
import praw
import time
import os

if __name__ == '__main__':
    usr_url = raw_input("Enter the match thread url: ")
    keyword = raw_input("Input the starting word(s) of the match events : ")

    def dostuff(url):
        r = praw.Reddit(user_agent = 'cmdlinesoccer')
        match_thread = update.url_routine(url , r)
        KickOff_index = update.get_opening_min(match_thread, keyword)
        update.just_print(match_thread, KickOff_index)

    while True:
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
            dostuff(usr_url)
            time.sleep(30)
        except KeyboardInterrupt:
            print "Back to work, eh?"
            break
