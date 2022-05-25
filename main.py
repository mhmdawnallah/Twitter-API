import configparser
from twitter_api import TwitterAPI

def main(args):
    twitterAPI = TwitterAPI(args)
    tweets = twitterAPI.get_home_timeline_tweets()
    twitterAPI.to_csv(tweets)
    twitterAPI.tweet("Hello World from Twitter API using Python!")



if __name__ == '__main__':
    # read configs
    config = configparser.ConfigParser()
    config.read('config.ini')

    api_key = config['twitter']['api_key']
    api_key_secret = config['twitter']['api_key_secret']
    access_token = config['twitter']['access_token']
    access_token_secret = config['twitter']['access_token_secret']

    args = {'api_key':api_key, 'api_key_secret':api_key_secret,
            'access_token':access_token, 'access_token_secret':access_token_secret}
    
    main(args)


