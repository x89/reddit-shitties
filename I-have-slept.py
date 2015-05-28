#!/usr/bin/env python

import praw
from datetime import datetime
r = praw.Reddit(user_agent='I have logged in')
r.login()

fp = r.get_front_page()
for thing in fp:
    delta = datetime.now() - datetime.fromtimestamp(thing.created)
    if delta.seconds // 60 // 60 > 12:
        print("{0} :: {1} hours old.".format(thing.title,
            delta.seconds // 60 // 60))
        thing.hide()
        thing.downvote()
