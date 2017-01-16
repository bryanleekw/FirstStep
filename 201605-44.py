# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 20:16:44 2017

@author: LKW084
"""

import twitter
import json
import oauth

access_token = "188803757-J5l1FcqqH8gpnPYQ3ht8EloOa9I3Ptd0QcYLqlxJ"
access_secret = "pxS7wpqhgEUwp9pjPALeVSGeaw43iUTvXHFnVK6V6LGta"
consumer_key = "Lg9zL2u3zalFnb01Jh8EZcyBP"
consumer_secret = "3YhpH3dPZfBFSF7fhlYrJRILB4JaEG1G2SpVVLQuoF5t3cQwNL"

t = twitter(auth=OAuth(access_token, access_secret, consumer_key, consumer_secret))

twitter_api = twitter.Twitter(auth=auth)
q = '#Trump'
count = 100

search_results = twitter_api.search.tweets(q=q, count=count)

statuses = search_results['statuses']

status_texts = [status['text'] 
				 for status in statuses ]
         
screen_names = [user_mention['screen_name'] 
				 for status in statuses
				 	for user_mention in status['entities']['user_mentions']]
          
hashtags = [hashtag['text']
			  for status in statuses
			  	for hashtag in status['entities']['hashtags']]

words = [w
			for t in status_texts
				for w in t.split() ]

print(json.dumps(status_texts[0:100], indent =1))
print(json.dumps(screen_names[0:100], indent =1))
print(json.dumps(hashtags[0:100], indent =1))
print(json.dumps(words[0:100], indent =1))

