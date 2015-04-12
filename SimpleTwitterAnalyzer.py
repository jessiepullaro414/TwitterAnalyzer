import tweepy
from unicodedata import normalize
import sys

# Lists
punctuation = ["http://t.co/","\n","\t","\r","`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", ", ", "<", ".", ">", "?", "/", "{", "[", "}", "]", "|", "\\", ":", ";", "'", '"']
STOP_WORDS = ["","s","m" "a", "about", "above", "after", "again", "against", "all", "am", "an", "and", "any", "are", "aren't", "as", "at", "be", "because", "been", "before", "being", "below", "between", "both", "but", "by", "can't", "cannot", "could", "couldn't", "did", "didn't", "do", "does", "doesn't", "doing", "don't", "down", "during", "each", "few", "for", "from", "further", "had", "hadn't", "has", "hasn't", "have", "haven't", "having", "he", "he'd", "he'll", "he's", "her", "here", "here's", "hers", "herself", "him", "himself", "his", "how", "how's", "i", "i'd", "i'll", "i'm", "i've", "if", "in", "into", "is", "isn't", "it", "it's", "its", "itself", "let's", "me", "more", "most", "mustn't", "my", "myself", "no", "nor", "not", "of", "off", "on", "once", "only", "or", "other", "ought", "our", "ours", "ourselves", "out", "over", "own", "same", "shan't", "she", "she'd", "she'll", "she's", "should", "shouldn't", "so", "some", "such", "than", "that", "that's", "the", "their", "theirs", "them", "themselves", "then", "there", "there's", "these", "they", "they'd", "they'll", "they're", "they've", "this", "those", "through", "to", "too", "under", "until", "up", "very", "was", "wasn't", "we", "we'd", "we'll", "we're", "we've", "were", "weren't", "what", "what's", "when", "when's", "where", "where's", "which", "while", "who", "who's", "whom", "why", "why's", "with", "won't", "would", "wouldn't", "you", "you'd", "you'll", "you're", "you've", "your", "yours", "yourself", "yourselves"]
TWITTER_WORDS = ["amp","http", "https", "co", "com", "rt", "strl", "hstn", "t","u","1","2","3","4","5","6","7","8","9"]
ALPHABET="a b c d e f g h i j k l m n o p q r s t u v w x y z".split(" ");
# Return list of Tweet objects based on search query. Must take tweepy.API object
def getTweets(api, q, lang="en", max=200):
    tweets = []
    for tweet in tweepy.Cursor(api.search, q=q, lang=lang, count=100).items(max):
        tweets.append(tweet)
        sys.stdout.write(str(len(tweets))+" tweets\r")
    return tweets

# Return a list of words from a list of texts
def getWords(texts, exclude=[]):
    # Clean up punctuation and all that jazz (HaCha!)
    # By converting the word list to a string
    words = texts
    tempstring = ""
    for i in words: tempstring += normalize('NFKD', i.lower()).encode('ascii', 'ignore').decode("utf-8")+" "#Remove non-ASCII characters
    for i in punctuation: tempstring = tempstring.replace(i, " ")
    while tempstring != tempstring.replace("  ", " "): tempstring = tempstring.replace("  ", " ")

    # Convert back to list
    tempwords=tempstring.split(" ")
    words=[]
    for i in tempwords:
        if i.lower() not in exclude:
            words.append(i)
    return words

# Return a list of word counts from a list of words
def getWordCounts(words):
    # Create list of word counts
    wordcountlist=[]
    usedwordlist=[]
    for word in words:
        if word not in usedwordlist:
            count=0
            for i in words:
                if(i==word):
                    count+=1
            wordcountlist.append([word,count])
            usedwordlist.append(word)

    #bubble sort wordcountlist
    for passnumber in range(len(wordcountlist)-1,0,-1):
        for i in range(passnumber):
            if wordcountlist[i][1]>wordcountlist[i+1][1]:
                temp = wordcountlist[i]
                wordcountlist[i] = wordcountlist[i+1]
                wordcountlist[i+1] = temp
    #return result
    return wordcountlist[::-1]