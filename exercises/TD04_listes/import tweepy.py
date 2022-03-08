import tweepy
import time
 
def auth():
    """
    se connecte à l'api twitter
    """
    # Clés de votre application
    consumer_key = "UJvRtM76qCvswSuEXxeQLWtMv"
    consumer_secret = "I5BSJkOJZcnzoEo6QS45PvjMi9upfaSugKel6WSHLLFIGv4cCX"
 
    # le access_token est le token de l'application twitter que nous avons crée précédement
    access_token = "1468560532491759620-ebxr7ByvkUAJhSga0jboioAD7lgs5v"
    access_token_secret = "HYpdfotGEZThEoCwZ322wvinuxdvX2iy31x4JghUbrhlc"
    bearer_token = "AAAAAAAAAAAAAAAAAAAAAFXGWgEAAAAAR0L1qmVKlHQdG24ZXBjoJeIWG5M%3Dv0NKRdeNlmwZi7yQ07v0GIJMcTlmnrHwKggtMXKbbsSh0mRwp"
    client = tweepy.Client(bearer_token=bearer_token, consumer_key=consumer_key, consumer_secret=consumer_secret, access_token=access_token, access_token_secret=access_token_secret)
    #auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    #auth.set_access_token(access_token, access_token_secret)
 
    #api = tweepy.API(auth)
    return client


while True:
    time.sleep(5.184)
    client =auth()
    query = "QSG"
    #client.create_tweet(text="test")
    tweets = client.search_recent_tweets(query, user_auth=True,max_results=10).data
    for tweet in tweets:
        print(tweet.id)
        client.retweet(tweet.id)