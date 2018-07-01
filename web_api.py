#1
a="an access token is an object that describes the security context of a process or thread. The informaion in a token includes the identity and privileges of the user account associated with the process or thread."
print(a)
b="1011804384332693505-PcLjWkM4gbXF2AZJuBudxgYf5BCFMJ" #access token
print(b)

#2
# Google IP address is
print("172.217.15.110")
#facebook IP address is
print("31.13.65.36")

#3
from api import Consumer_Key,Consumer_Secret,Access_Token,Access_Secret
import tweepy

oauth=tweepy.OAuthHandler(Consumer_Key,Consumer_Secret)
oauth.set_access_token(Access_Token,Access_Secret)
api=tweepy.API(oauth)
print(api.search("#sanju"))

#4
a="API is a part of library which defines how an application communicates with external code."
b="API can be written in any language."
c="Library is written in same language which is a collection of all the functionalities required for the use case."
d="For example : Numpy is a library of Python, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays."

print(a,b,c,d)