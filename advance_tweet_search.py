from glob import glob
import pandas as pd
import snscrape.modules.twitter as sntwiter

# Creating a list of tweets
query = '(#crypto OR #bitcoin OR #cryptocurrency OR #blockchain OR #ethereum OR #btc OR #cryptonews OR #Tether OR #USDC OR #BNB) since:2021-01-01'
tweets = []
limit = 10000

for tweet in sntwiter.TwitterSearchScraper(query).get_items():
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date, tweet.user.username, tweet.content, tweet.url, tweet.hashtags])

# Creating a DataFrame
df_tweets = pd.DataFrame(tweets, columns=['Date', 'Username', 'Content','URL', 'Hashtags'])


# Saving the DataFrame
def save_file(name):
    try:
        assert name not in glob(name)
        df_tweets.to_csv(name)
    except:
        print("Try another Name")


save_file("crypto_10k_tweets_(2021_2022Nov).csv")
