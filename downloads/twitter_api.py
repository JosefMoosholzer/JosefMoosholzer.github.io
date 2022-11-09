import configparser
import tweepy
import pandas as pd
from time import sleep, perf_counter

config = configparser.ConfigParser()
config.read('config.ini')
api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']
bearer_token = "AAAAAAAAAAAAAAAAAAAAAHVQjAEAAAAA0HIm%2BLoEEGytO9XagY9Fw8pH%2F1Y%3DJXiZE4xS2sK2djOhwVNIEt3QLFiVkrYSeJa2S2tcngx8LaAbHH"
access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

auth = tweepy.OAuth1UserHandler(api_key, api_key_secret, access_token, access_token_secret)
api = tweepy.API(auth)

alltweets = []

new_tweets = api.user_timeline(screen_name='@JoeBiden', count=200, include_rts=False, exclude_replies=True)
alltweets.extend([{'ID': tweet.id, 'Time': tweet.created_at, 'Tweet': tweet.text, 'Author': 'Joe Biden'} for tweet in new_tweets])
oldest = alltweets[-1]['ID']

while (len(new_tweets) > 0) and (len(alltweets) < 20000):
   sleep(10)

   new_tweets = api.user_timeline(screen_name='@JoeBiden', count=200, include_rts=False, exclude_replies=True, max_id=oldest-1)
   alltweets.extend([{'ID': tweet.id, 'Time': tweet.created_at, 'Tweet': tweet.text, 'Author': 'Joe Biden'} for tweet in new_tweets])
   oldest = alltweets[-1]['ID']

   print(f"...{len(alltweets)} tweets downloaded so far")

df = pd.DataFrame(alltweets)
print(df.head())
df.to_csv('Joe_Tweets.csv', index=False)