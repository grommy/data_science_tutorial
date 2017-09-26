import json
import tweepy


class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api=None):
        super(MyStreamListener, self).__init__()
        self.num_tweets = 0
        self.file = "tweets.txt"

    def on_status(self, status):
        tweet = status._json
        with open(self.file, 'a') as file:
            file.write(json.dumps(tweet) + '\n')
        self.num_tweets += 1
        if self.num_tweets < 4:
            return True
        else:
            return False

    def on_error(self, status):
        print(status)
