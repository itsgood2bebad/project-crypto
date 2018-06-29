import tweepy
import time

consumer_key = 'fDLolIWAySzQBp6JxQh9z484e'
consumer_secret = 'ajGDn5PMfEjrMXB8UkROHnVCCCeoxIYcHn4ZiD5NnL0mszRagE'
access_token = '1012622045186871296-g1cxl2KjYsofTNnzf9cAMx1SxHVyQA'
access_token_secret = '29GDmqe5SWT1mWwOGMGfqo1AtpAgRtz5ArrKzdLDGabfG'

authentification =tweepy.OAuthHandler(consumer_key,consumer_secret)
authentification.set_access_token(access_token,access_token_secret)
api =tweepy.API(authentification)
#user=tweepy.API.me(api)
user=api.get_user('llywi93')

print ("User id: " + user.id_str)
print (user.name)
print ("Description: " + user.description)
print ("Language: " + user.lang)
print ("Account created at: " + str(user.created_at))
print ("Location: " + user.location)
#print ("Time zone: " + user.time_zone)
print ("Number of tweets: " + str(user.statuses_count))
print ("Number of followers: " + str(user.followers_count))
print ("Following: " + str(user.friends_count))
print ("A member of " + str(user.listed_count) + " lists.")

statuses = api.user_timeline(id = user.id, count = 200)
 
for status in statuses:
	print ("***")
	print ("Tweet id: " + status.id_str)
	print (status.text)
	print ("Retweet count: " + str(status.retweet_count))
	print ("Favorite count: " + str(status.favorite_count))
	print (status.created_at)
	print ("Status place: " + str(status.place))
	print ("Source: " + status.source)
	print ("Coordinates: " + str(status.coordinates))
	time.sleep(1)
