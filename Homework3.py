import sys

from oauthfile import readOAuthFile
authTuple = readOAuthFile(sys.argv[1])

from twitter import OAuth, TwitterStream, TwitterHTTPError
oauth = OAuth(authTuple[0], authTuple[1], authTuple[2], authTuple[3])

# Initiate the connection to Twitter Streaming API
twitter_stream = TwitterStream(auth=oauth)

from textblob import TextBlob
def sentiment_subjectivity(contents):
	analysis = TextBlob(contents)
	result = analysis.sentiment
	# Sentiment
	if result[0] >= 0.5:
		term_sentiment = "STRONGLY POSITIVE"
	elif result[0] >= 0 and result[0] < 0.5:
		term_sentiment = "MILDLY POSITIVE"
	elif result[0] >= -0.5 and result[0] < 0:
		term_sentiment = "MILDLY NEGTIVE"
	else:
		term_sentiment = "STRONGLY NEGTIVE"
	print "\tTweet sentiment is %s (%s)" % (term_sentiment, str(result[0]))
	# Subjectivity
	if result[1] >= 0.75:
		term_subjectivity = "STRONGLY SUBJECTIVE"
	elif result[1] >= 0.5 and result[1] < 0.75:
		term_subjectivity = "MILDLY SUBJECTIVE"
	elif result[1] >= 0.25 and result[1] < 0.5:
		term_subjectivity = "MILDLY OBJECTIVE"
	else:
		term_subjectivity = "STRONGLY OBJECTIVE"
	print "\tTweet subjectivity is %s (%s)" % (term_subjectivity, str(result[1]))
	return term_sentiment, term_subjectivity, result

def overall_analysis(analysis_result):
	global overall_count, postive_count, negtive_count, subjective_count, objective_count, overall_sentiment, overall_subjectivity
	overall_count += 1
	if analysis_result[0] == "MILDLY POSITIVE" or analysis_result[0] == "STRONGLY POSITIVE":
		postive_count += 1
	else:
		negtive_count += 1
	if analysis_result[1] == "MILDLY SUBJECTIVE" or analysis_result[1] == "STRONGLY SUBJECTIVE":
		subjective_count += 1
	else:
		objective_count += 1
	overall_sentiment += analysis_result[2][0]
	overall_subjectivity += analysis_result[2][1]


while True:
	tweet_count = 10
	analysis_result = {}
	percentage = {}
	overall_count = 0
	postive_count = 0
	negtive_count = 0
	subjective_count = 0
	objective_count = 0
	overall_sentiment = 0
	overall_subjectivity = 0
	tweet_count = raw_input("Enter the number of tweets you want to search: ")
	if tweet_count == "quit":
		break
	tweet_count = int(tweet_count)
	search_term = raw_input("Enter a search term: ")
	if search_term == "quit":
		answer = raw_input("Are you sure you want to quit (Y: quit. N: search tweets about 'quit'.)?")
		if answer == "Y" or answer == "y":
			break
		else:
			try:
				# Get a sample of the public data following through 
				iterator = twitter_stream.statuses.filter(track=search_term, language="en")
				print "\n"
				for tweet in iterator:
				    print tweet["text"]
				    print "\tSent by user", tweet["user"]["screen_name"], "(Location: %s )" % tweet["user"]["location"]
				    print "\tHashtags:",
				    for hashtags in tweet["entities"]["hashtags"]:
				    	print "#%s" % hashtags["text"],
				    print "\t"
				    analysis_result = sentiment_subjectivity(tweet["text"])
				    overall_analysis(analysis_result)
				    print "-----------------"
				    tweet_count -= 1
				    if tweet_count <= 0:
				        break
				percentage[0] = float(postive_count) / overall_count
				percentage[0] = "%.1f%%" % (percentage[0] * 100)
				percentage[1] = float(negtive_count) / overall_count
				percentage[1] = "%.1f%%" % (percentage[1] * 100)
				percentage[2] = float(subjective_count) / overall_count
				percentage[2] = "%.1f%%" % (percentage[2] * 100)
				percentage[3] = float(objective_count) / overall_count
				percentage[3] = "%.1f%%" % (percentage[3] * 100)
				print "Overall analysis of %s tweets:" % overall_count
				print "%s were positive (%s)." % (postive_count, percentage[0]), "%s were negtive (%s)." % (negtive_count, percentage[1])
				print "Average sentiment value was %s" % (overall_sentiment / overall_count)
				print "%s were subjective (%s)." % (subjective_count, percentage[2]), "%s were objective (%s)." % (objective_count, percentage[3])
				print "Average subjectivity value was %s" % (overall_subjectivity / overall_count)
			except TwitterHTTPError, desc:
				print "Couldn't connect: ", desc
	else:
		try:
			# Get a sample of the public data following through 
			iterator = twitter_stream.statuses.filter(track=search_term, language="en")
			print "\n"
			for tweet in iterator:
			    print tweet["text"]
			    print "\tSent by user", tweet["user"]["screen_name"], "(Location: %s )" % tweet["user"]["location"]
			    print "\tHashtags:",
			    for hashtags in tweet["entities"]["hashtags"]:
			    	print "#%s" % hashtags["text"],
			    print "\t"
			    analysis_result = sentiment_subjectivity(tweet["text"])
			    overall_analysis(analysis_result)
			    print "-----------------"
			    tweet_count -= 1
			    if tweet_count <= 0:
			        break
			percentage[0] = float(postive_count) / overall_count
			percentage[0] = "%.1f%%" % (percentage[0] * 100)
			percentage[1] = float(negtive_count) / overall_count
			percentage[1] = "%.1f%%" % (percentage[1] * 100)
			percentage[2] = float(subjective_count) / overall_count
			percentage[2] = "%.1f%%" % (percentage[2] * 100)
			percentage[3] = float(objective_count) / overall_count
			percentage[3] = "%.1f%%" % (percentage[3] * 100)
			print "Overall analysis of %s tweets:" % overall_count
			print "%s were positive (%s)." % (postive_count, percentage[0]), "%s were negtive (%s)." % (negtive_count, percentage[1])
			print "Average sentiment value was %s" % (overall_sentiment / overall_count)
			print "%s were subjective (%s)." % (subjective_count, percentage[2]), "%s were objective (%s)." % (objective_count, percentage[3])
			print "Average subjectivity value was %s" % (overall_subjectivity / overall_count)
		except TwitterHTTPError, desc:
			print "Couldn't connect: ", desc
