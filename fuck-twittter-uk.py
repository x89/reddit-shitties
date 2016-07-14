import itertools
from praw import Reddit
r = Reddit(user_agent="Twitteroo")
r.login()

subs = ('unitedkingdom', 'ukpolitics', 'scotland')

for sub in subs:
    s = r.get_subreddit(sub)
    submissions = list(itertools.chain.from_iterable([s.get_new(), s.get_top()]))
    for submission in submissions:
        if 'twitter' in submission.url:
            submission.downvote()
            print('Downvoted %s (%s).' % (submission.title, submission.url))
