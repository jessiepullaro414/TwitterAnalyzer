#!/usr/bin/env python

#import modules - STA includes Tweepy
from SimpleTwitterAnalyzer import*
import json
import sys


#Authenticate application and create API object
print("Authorizing application\r")
auth=tweepy.OAuthHandler("", "")
api=tweepy.API(auth)


# Collect tweets
print("")
if(sys.version_info[0]==2):
	query=raw_input("Query>")
	max_number_of_results=int(raw_input("Max Results>"))
else:
	query=input("Query>")
	max_number_of_results=int(input("Max Results>"))
tweets=getTweets(api,query, max=max_number_of_results)# get 'max' results


# Collect tweet text and JSON data
print("Converting Data...          \r")
tweet_texts=[]
json_dump=""
tweetcount=0;
for tweet in tweets:
    tweet_texts.append(tweet.text)
    json_dump += json.dumps(tweet._json)+"\n"
    tweetcount+=1


# Get word counts
print("Doing Wordcount...          \r")
wordcount=getWordCounts(getWords(tweet_texts,exclude=STOP_WORDS+TWITTER_WORDS+ALPHABET))


# Export JSON
print("Exporting Data...          \r")
json_file=open("twitter_dump("+query+").json", "w")
json_file.write(json_dump)
json_file.close();


# Export word count
wc_text=""
for i in wordcount:
    wc_text += i[0]+":"+str(i[1])+"\n"
wc_file=open("twitter_dump("+query+")_wordcount.txt","w")
wc_file.write(wc_text)
wc_file.close()


# Finish
print("Finished.                    ")
print("# of tweets exported:\t"+str(tweetcount))
print("# of words exported:\t"+str(len(wordcount)))
