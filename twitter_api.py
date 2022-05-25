import tweepy
import pandas as pd

class TwitterAPI:
    def __init__(self,keys: dict):
        auth = tweepy.OAuthHandler(keys['api_key'],keys['api_key_secret'])
        auth.set_access_token(keys['access_token'],keys['access_token_secret'])
        self.api = tweepy.API(auth)
    
    def get_home_timeline_tweets(self):
        public_tweets = self.api.home_timeline()
        data = []
        for tweet in public_tweets:
            tweet_time = tweet.created_at
            tweet_user = tweet.user.screen_name
            tweet_text = tweet.text

            data.append({'Time':tweet_time, 'User':tweet_user, 'Tweet':tweet_text})
            
        return data
    
    def update_profile_banner(self,profile_banner_url: str):
        self.api.update_profile_banner(profile_banner_url)

    def update_profile_image(self,profile_image_url: str):
        self.api.update_profile_image(profile_image_url)
    
    def tweet(self, status: str):
        self.api.update_status(status)
    
    def send_direct_message(self, user: str, message: str):
        self.api.send_direct_message(user, message)

    def to_csv(self, tweets: list[dict]):
        df = pd.DataFrame(tweets)
        df.to_csv('tweets.csv', index=False)

