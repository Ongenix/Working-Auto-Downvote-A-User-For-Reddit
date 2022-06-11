__author__ = "Ongenix"

import os;os.system('pip3 install praw') #setup
import praw
#===================
# You can get the data for this at ssl.reddit.com/prefs/apps and create a new script
# The username and password part is your username and password
r = praw.Reddit(user_agent='Auto-Downvote',
                client_id='',
                client_secret='',
                username="",
                password='')
#===================

limit = 1000 #keep this the same
user = ''
#person to stalk
downvote = True
upvote = False
debug = False

for i in ((r.redditor(user).submissions.new(limit=limit))):
  comment = r.submission(i.id)
  try:
    if downvote and not upvote:
      comment.downvote()
    else:
      comment.upvote()
  except Exception as e:
    if debug:
      print(e)
    else:1
