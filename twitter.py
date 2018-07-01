from api import Consumer_Key,Consumer_Secret,Access_Token,Access_Secret
import tweepy

oauth=tweepy.OAuthHandler(Consumer_Key,Consumer_Secret)
oauth.set_access_token(Access_Token,Access_Secret)
api=tweepy.API(oauth)
print(api.search("#sanju"))

user=api.get_user('prachi_singh')
print(user.screen_name)
print(user.followers_count)

