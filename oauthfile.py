
# Inputs:  pass a string filename to this function.  The filename should refer
# to a file with contents with this format:
#
#   ACCESS_TOKEN="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
#   ACCESS_SECRET="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
#   CONSUMER_KEY="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
#   CONSUMER_SECRET="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
#
# The code will attempt to load this file and extract the credential information.
# If successful, the function will return a 4-item tuple containing
# (access_token, access_secret, consumer_key, consumer_secret)
#
# If unsuccessful, the function will display an error message and return None. Your
# program should check the return value from the function; if it's None, your code
# should exit and you should fix the problem. Otherwise, you'll use the tuple
# data returned to authenticate to Twitter.

def readOAuthFile(filename):
	accessToken = None
	accessSecret = None
	consumerKey = None
	consumerSecret = None
	try:
		file = open(filename, "r")
		lines = file.readlines()
		file.close()

		for line in lines:
			contents = line.split("=")
			if len(contents) == 0 or contents[0].strip() == "":
				# blank line, just skip it
				continue
			if contents[0].strip() == "ACCESS_TOKEN":
				accessToken = contents[1].strip().strip('"')
				pass
			elif contents[0].strip() == "ACCESS_SECRET":
				accessSecret = contents[1].strip().strip('"')
				pass
			elif contents[0].strip() == "CONSUMER_KEY":
				consumerKey = contents[1].strip().strip('"')
				pass
			elif contents[0].strip() == "CONSUMER_SECRET":
				consumerSecret = contents[1].strip().strip('"')
				pass
			else:
				print "Unknown data in OAuth file, cannot load:", contents[0]
				return None

		if accessToken == None:
			print "ACCESS_TOKEN not found in OAuth file"
			return None
		if accessSecret == None:
			print "ACCESS_SECRET not found in OAuth file"
			return None
		if consumerKey == None:
			print "CONSUMER_KEY not found in OAuth file"
			return None
		if consumerSecret == None:
			print "CONSUMER_SECRET not found in OAuth file"
			return None

		return accessToken, accessSecret, consumerKey, consumerSecret

	except Exception, detail:
		print "Problem reading OAuth file", filename, ":", detail
		return None

