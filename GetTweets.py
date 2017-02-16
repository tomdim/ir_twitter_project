# -*- coding: utf-8 -*-
import config
import mysql.connector
import tweepy
from datetime import date
import nltk
import stemming
import re
import unicodedata
import traceback
import codecs
import datetime
from datetime import timedelta

#yesterday
_date = datetime.date.today() - timedelta(days=5) #since
_dateu = datetime.date.today() - timedelta(days=0) #until  
#today = date.today()
_date.strftime('%y%m%d')

class GetTweets:
    def createTables(self):
        cur.execute("""CREATE TABLE IF NOT EXISTS TweetsTsipras(
                        date VARCHAR(10),
                        tweet_text VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
                        stemmed_text VARCHAR(160),
                        Sentiment VARCHAR(10),
                        PRIMARY KEY(stemmed_text)
                        )""")
        db.commit()
        print "Created table TweetsTsipras"
        
        cur.execute("""CREATE TABLE IF NOT EXISTS TweetsMitsotakis(
                        date VARCHAR(10),
                        tweet_text VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
                        stemmed_text VARCHAR(160),
                        Sentiment VARCHAR(10),
                        PRIMARY KEY(stemmed_text)
                        )""")
        db.commit()
        print "Created table TweetsMitsotakis"
        
        cur.execute("""CREATE TABLE IF NOT EXISTS TweetsSyriza(
                        date VARCHAR(10),
                        tweet_text VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
                        stemmed_text VARCHAR(160),
                        Sentiment VARCHAR(10),
                        PRIMARY KEY(stemmed_text)
                        )""")
        db.commit()
        print "Created table TweetsSyriza"
        
        cur.execute("""CREATE TABLE IF NOT EXISTS TweetsNeaDimokratia(
                        date VARCHAR(10),
                        tweet_text VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
                        stemmed_text VARCHAR(160),
                        Sentiment VARCHAR(10),
                        PRIMARY KEY(stemmed_text)
                        )""")
        db.commit()
        print "Created table TweetsNeaDimokratia"
        
    def searchTweets(self, stopwords):   
        tweetCount = 0
        self.createTables()  
        
        auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
        auth.set_access_token(config.access_token, config.access_token_secret)
        
        api = tweepy.API(auth)
        print "Twitter Authorization OK"
        
        try:
            for tweet in tweepy.Cursor(api.search,
                                       q="#SYRIZA OR #ND OR #NEADIMOKRATIA OR @atsipras OR @kmitsotakis",
                                       rpp=100,
                                       result_type="recent",
                                       since=_date,
                                       #until=_dateu,
                                       lang="el",
                                       include_entities=True
                                       ).items():        
                
                try: quoted = tweet.quoted_status.id_str
                except: quoted = "Not a quote Tweet"    
                try: retweet = tweet.retweeted_status.id_str
                except: retweet = "Not a Retweet"
                
                if(quoted == "Not a quote Tweet" and retweet == "Not a Retweet" and tweet.lang == "el"):
                    print '\n\n***************************************'
                    print '***************************************'
                    clean_text = self.clean_text(tweet.text).upper()
                    print "INITIAL TWEET: " + tweet.text
                    print "_____________________________________________________________________________"
                    print "CLEAN TEXT: " + clean_text
                    clean_text_without_stopwords = self.remove_stopwords(clean_text, stopwords)
                    print "_____________________________________________________________________________"
                    print "\nCLEAN TEXT WITHOUT STOPWORDS: " + clean_text_without_stopwords
                    stemmed_text_without_stopwords = self.stem(clean_text_without_stopwords)     
                    print "_____________________________________________________________________________"
                    print "\nSTEMMED TEXT WITHOUT STOPWORDS: " + stemmed_text_without_stopwords           
                    print '***************************************'
                    tweet_date = tweet.created_at.strftime('%Y-%m-%d')[:10]
                    print tweet_date
                    try:
                        for i in range(0,len(tweet.entities['hashtags'])):
                            if tweet.entities['hashtags'][i]['text'].lower() == "syriza":
                                print "\nNew tweet syriza"
                                cur.execute("INSERT INTO TweetsSyriza(date, tweet_text, stemmed_text, Sentiment) VALUES (%s,%s,%s,%s) ON DUPLICATE KEY UPDATE stemmed_text=%s", (tweet_date, tweet.text, stemmed_text_without_stopwords, "Neutral", stemmed_text_without_stopwords))
                                db.commit()
                                tweetCount += 1
                            #test both #neadimokratia and #nd hashtags because there are not enough tweets
                            if (tweet.entities['hashtags'][i]['text'].lower() == "neadimokratia" or tweet.entities['hashtags'][i]['text'].lower() == "nd"):
                                print "\nNew tweet neadimokratia"
                                cur.execute("INSERT INTO TweetsNeaDimokratia(date, tweet_text, stemmed_text, Sentiment) VALUES (%s,%s,%s,%s) ON DUPLICATE KEY UPDATE stemmed_text=%s", (tweet_date, tweet.text, stemmed_text_without_stopwords, "Neutral", stemmed_text_without_stopwords))
                                db.commit()
                                tweetCount += 1
                            
                        for i in range(0,len(tweet.entities['user_mentions'])):          
                            if tweet.entities['user_mentions'][i]['screen_name'].lower()== "atsipras":
                                print "\nNew tweet atsipras"
                                cur.execute("INSERT INTO TweetsTsipras(date, tweet_text, stemmed_text, Sentiment) VALUES (%s,%s,%s,%s) ON DUPLICATE KEY UPDATE stemmed_text=%s", (tweet_date, tweet.text, stemmed_text_without_stopwords, "Neutral", stemmed_text_without_stopwords))
                                db.commit()
                                tweetCount += 1
                            
                            if tweet.entities['user_mentions'][i]['screen_name'].lower()== "kmitsotakis":
                                print "\nNew tweet kmitsotakis"
                                cur.execute("INSERT INTO TweetsMitsotakis(date, tweet_text, stemmed_text, Sentiment) VALUES (%s,%s,%s,%s) ON DUPLICATE KEY UPDATE stemmed_text=%s", (tweet_date, tweet.text, stemmed_text_without_stopwords, "Neutral", stemmed_text_without_stopwords))
                                db.commit()
                                tweetCount += 1
                            
                    except:
                        continue
                    
        except:
            print "\n\nEnd of Results (API Rate Limiting)"
        print "\n________________________________________________\nNumber of new tweets stored in DB since",_date, ":" , tweetCount
       
    def clean_text(self, tweet_text):
        tmp1 = re.sub(r"http\S+", "", tweet_text)
        tmp2 = re.sub(u'[^Α-Ωα-ωΆ-Ώά-ώ]+', " ", tmp1)
        tmp3 = tmp2.lstrip()
        tmp3.rstrip()
        return ''.join(c for c in unicodedata.normalize('NFD', tmp3)
                     if unicodedata.category(c) != 'Mn')
    
    def remove_stopwords(self, clean_text, stopwords):
        t = nltk.word_tokenize(clean_text)
        clean_text_without_stopwords = ''
        
        try:          
            for i in range(0, len(t)):
                if t[i] not in stopwords:
                    clean_text_without_stopwords += t[i] + ' '
                else:
                    continue
        except:
            traceback.print_exc()
        
        return clean_text_without_stopwords.rstrip(' ')
    
    def get_stopwords(self):
        with codecs.open("greekstopwords.txt", mode="r", encoding="utf-8") as f:
            stopwords = []
            for line in f:
                stopwords.append(line.strip())
            
        return stopwords
        
    def stem(self, clean_text_without_stopwords):  
        words = nltk.word_tokenize(clean_text_without_stopwords)

        try:
            stemmed = ''
            for i in range(0, len(words)):
                stemmed += stemming.stem(unicode(words[i])) + " "
        except AttributeError:
            traceback.print_exc()
        except UnboundLocalError:
            traceback.print_exc()
        except UnicodeEncodeError:
            traceback.print_exc()
        except UnicodeDecodeError:
            traceback.print_exc()
            
        return stemmed.rstrip()

if __name__ == '__main__':
    tweetCount = 0
    db = mysql.connector.connect(host="localhost",    
                                 user="root",                
                                 passwd=config.passDB,     
                                 db="tweets",
                                 charset='utf8',
                                 use_unicode=True)
            
    print "Connecting to MYSQL .. .. .."
    cur = db.cursor()
    print "Connected to MYSQL"
    print _date , ' - ', _dateu
    
    g = GetTweets()
    stopwords = g.get_stopwords()
    g.searchTweets(stopwords)
    
    