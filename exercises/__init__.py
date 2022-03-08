import tweepy

def auth():
    """
    se connecte à l'api twitter
    """
    # Clés de votre application
    consumer_key = "UJvRtM76qCvswSuEXxeQLWtMv"
    consumer_secret = "I5BSJkOJZcnzoEo6QS45PvjMi9upfaSugKel6WSHLLFIGv4cCX"

    # le access_token est le token de l'application twitter que nous avons créée précédement
    access_token = "Bot UVSQ "
    access_token_secret = "B0tuvsq!"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    return api,auth