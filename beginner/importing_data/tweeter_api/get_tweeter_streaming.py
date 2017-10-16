# Import package
import json
import tweepy
from tweeter_listener import MyStreamListener
import re
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


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


def word_in_text(word, tweet):
    word = word.lower()
    text = tweet.lower()
    match = re.search(word, text)

    if match:
        return True
    return False

# Filter Twitter Streams to capture data by the keywords:
track = stream.filter(track=['clinton', 'trump', 'sanders', 'cruz'])

tweets_data = []
with open(tweets_data_path, 'r') as tweets_file:
    # Read in tweets and store in list: tweets_data
    for line in tweets_file:
        tweet = json.loads(line)
        tweets_data.append(tweet)

print(tweets_data[0].keys())
# Build DataFrame of tweet texts and languages
df = pd.DataFrame(tweets_data, columns=['text', 'lang'])

# Print head of DataFrame
print(df.head())

# Initialize list to store tweet counts
[clinton, trump, sanders, cruz] = [0, 0, 0, 0]

# Iterate through df, counting the number of tweets in which
# each candidate is mentioned
for index, row in df.iterrows():
    clinton += word_in_text('clinton', row['text'])
    trump += word_in_text('trump', row['text'])
    sanders += word_in_text('sanders', row['text'])
    cruz += word_in_text('cruz', row['text'])

# Set seaborn style
sns.set(color_codes=True)

# Create a list of labels:cd
cd = ['clinton', 'trump', 'sanders', 'cruz']

# Plot histogram
ax = sns.barplot(cd, [clinton, trump, sanders, cruz])
ax.set(ylabel="count")
plt.show()
