from datetime import datetime
import tweepy
from textblob import TextBlob
from kafka import KafkaProducer
from json import dumps
 
import pandas as pd

 
CONSUMER_KEY = "laGxhU1viKGmRZJPjt8srIpzM"
CONSUMER_SECRET = "DYffNCEIPUTIq6Nw14telSrQy5twPn8z85TxkwFoVmEZHA5V9Y"
ACCESS_TOKEN = "1592830280829702145-J4UUrxKGDuGdgQ17SI1rUwrvmhu9MD"
ACCESS_TOKEN_SECRET = "HJv7I71XyD67K8pQWxJgWzqONLZuVLrARbcqte8gRPD13"
def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, (datetime, datetime.date)):
        return obj.isoformat()
    raise TypeError("Type %s not serializable" % type(obj))
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
producer = KafkaProducer(bootstrap_servers=['localhost:9092'],value_serializer=lambda K:dumps(K,default=json_serial).encode('utf-8'))
columns = ['Time', 'User','text']
data = []
api = tweepy.API(auth)
cursor = tweepy.Cursor(api.search_tweets,q="Tesla",tweet_mode='extended').items(50)
for tweet in cursor:
   # producer.send('testTopic',tweet.full_text)
   print(tweet.user.screen_name)
   producer.send('twitter-topic',[tweet.full_text,tweet.user.screen_name])
   data.append([tweet.created_at, tweet.user.screen_name,tweet.full_text])
df = pd.DataFrame(data, columns=columns)


print(datetime.now().strftime("%Y-%m-%d"))

df.to_csv('articles-'+datetime.now().strftime("%Y-%m-%d") +
                  '.csv')

