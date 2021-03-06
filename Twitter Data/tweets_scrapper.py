import tweepy #https://github.com/tweepy/tweepy
import csv

#Twitter API credentials
consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""

def get_all_tweets(screen_name):

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    alltweets = []

    new_tweets = api.user_timeline(screen_name = screen_name,count=500)

    alltweets.extend(new_tweets)

    oldest = alltweets[-1].id - 1

    count =0
    while len(new_tweets)>0 and count<500:
        print ("getting tweets before %s" % (oldest))
        count +=1

    new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)

    alltweets.extend(new_tweets)

    oldest = alltweets[-1].id - 1

    print ("...%s tweets downloaded so far" % (len(alltweets)))

    outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]

#write the csv	
    with open('%s_tweets.csv' % screen_name, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["id","created_at","text"])
        writer.writerows(outtweets)

    pass

if __name__ == '__main__':
    get_all_tweets("itsayushthada")
