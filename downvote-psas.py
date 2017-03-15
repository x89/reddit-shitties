# Every single "PSA:" is a joke and deserves to be buried.
# Works well with the Reddit option to "hide down-voted submissions"

from praw import Reddit
r = Reddit(user_agent="Die-PSA")
r.login()

for post in r.get_front_page():
    if 'psa' in str.lower(post.title):
        post.downvote()
        print('Downvoted %s.' % post.title)
