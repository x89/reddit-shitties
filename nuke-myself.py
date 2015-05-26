from praw import Reddit
r = Reddit(user_agent='downvoting myself')
r.login()
me = r.user.get_comments('all')
for thing in me:  # Ooh sexy
    print(thing)
    thing.downvote()
