# Import package
import json
import tweepy
from tweeter_listener import MyStreamListener

# Store OAuth authentication credentials in relevant variables
access_token = "808368154758021120-ZUiuPXLnufvCn25kP54dup04KVYGKhT"
access_token_secret = "j9yZb6xZbrq5qmZQvmhNAUDxyPeHxrDVG1daPbb9fqT3l"
consumer_key = "xkb6VPJL41lqsqAzoWLthwGwv"
consumer_secret = "QeLVKt4uiAjl8m2LoEERLZZieGDqi5QATHXIlRWpiudGREOyp5"

# Pass OAuth details to tweepy's OAuth handler
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

tweets_data_path = 'tweets.txt'
# Initialize Stream listener
l = MyStreamListener()

# Create you Stream object with authentication
stream = tweepy.Stream(auth, l)


# Filter Twitter Streams to capture data by the keywords:
track = stream.filter(track=['clinton', 'trump', 'sanders', 'cruz'])

tweets_data = []
with open(tweets_data_path, 'r') as tweets_file:
    # Read in tweets and store in list: tweets_data
    for line in tweets_file:
        tweet = json.loads(line)
        tweets_data.append(tweet)

print(tweets_data[0].keys())
