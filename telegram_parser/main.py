import tweepy as tw
import pandas as pd

# API set-ups for the use of Twitter API
# Insert your keys and tokens below
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)



def get_tweets(listOfTweets, keyword, numOfTweets, data_since, data_until):
    for tweet in tw.Cursor(api.search, q=keyword+' -filter:retweets', since=data_since, until=data_until, lang='en').items(numOfTweets):
        dict_ = {
                 'Keywords': keyword,
                 'User Name': tweet.user.name,
                 'Screen Name': tweet.user.screen_name,
                 'Tweet Created at': tweet.created_at,
                 'Tweet Text': tweet.text,
                 'Location': tweet.user.location,
                 'Likes': tweet.favorite_count,
                 'Retweets': tweet.retweet_count
                 }
        listOfTweets.append(dict_)
    return listOfTweets

list_1 = []
numberOfPosts = 25
Start_date = '2019-12-06'
End_date = '2019-12-07'
hashtags = 'Wheat AND Australia'

get_tweets(list_1, hashtags, numberOfPosts, Start_date, End_date)
result_df = pd.DataFrame(list_1)
result_df.to_csv('Wheat_Tweets.csv', index=None)