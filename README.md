##  Aurthor: Yujia(BoBo) Wang
##  Date: 2017-10-2

##  Description:

This program connects to Twitter using the streaming API, and then collects and analyzes tweets for a search term that the user enters. For each tweet from Twitter, the program would display the tweet itself, including the twitter handle and user name of the tweet, and any hashtags included in the tweet. 

Also, for each tweet, the program would display an objectivity and sentiment analysis of the tweet based on the TextBlob. The program would keep a running tally of overall sentiment and objectivity. At the end, this summative data would be displayed. 

The command line looks like as follows:
python Homework3.py /User/keith/oauthdata.txt

The user can keep searching terms. To quit the program, input "quit".

## Function:

def sentiment_subjectivity(contents):
ananlyze the sentiment and subjectivity of the tweets.
return term_sentiment, term_subjectivity, result

term_sentiment: the sentiment of the tweet.
term_subjectivity: the subjectivity of the tweet.
result: a list that contains the value of sentiment and subjectivity.

def overall_analysis(analysis_result):
calcuate the overall value.


