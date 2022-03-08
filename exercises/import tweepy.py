import tweepy

def auth():
    """
    se connecte à l'api twitter
    """
    # Clés de votre application
    consumer_key = "UJvRtM76qCvswSuEXxeQLWtMv"
    consumer_secret = "I5BSJkOJZcnzoEo6QS45PvjMi9upfaSugKel6WSHLLFIGv4cCX"

    # le access_token est le token de l'application twitter que nous avons crée précédement
    access_token = "1468560532491759620-nix5nSeEd6DY6zfOgVfz739uwMcGXh"
    access_token_secret = "4yK8iSVTDtar8bG31IZvaQBqdNKJ4oOmOxfkskW5Z0ku4"
    bearer_token = "AAAAAAAAAAAAAAAAAAAAAFXGWgEAAAAAR0L1qmVKlHQdG24ZXBjoJeIWG5M%3Dv0NKRdeNlmwZi7yQ07v0GIJMcTlmnrHwKggtMXKbbsSh0mRwp"
    client = tweepy.Client(bearer_token=bearer_token, consumer_key=consumer_key, consumer_secret=consumer_secret, access_token=access_token, access_token_secret=access_token_secret)
    #auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    #auth.set_access_token(access_token, access_token_secret)

    #api = tweepy.API(auth)
    return client
client =auth()
print(client.create_tweet(text=""))