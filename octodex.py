#
# 	@author Rex Finn <rexcfinn@gmail.com>
# 	@version 1.0
# 	@link http://github.com/OctodexAPI/octodex.py
# 	@package octodex.py
#

# import urllib2 in order to do our cURL request
import urllib2
# import json to convert our JSON to dictionary
import json


class Octodex:
	# the URL to the API - strings will be appended for specification
	baseURL = 'https://octodexapi.herokuapp.com/'

	# Fetches the complete octodex
	# @return the complete octodex as a dictionary
	def completeOctodex(self):
		# do a cURL (in our cURL method) with just baseURL and return the result
		return self.cURL(self.baseURL)

	# Fetches a random octocat
	# @return the single octocat as a dictionary
	
	def randomOctocat(self):
		# do a cURL (in our cURL method) with baseURL appending '?random' and return the result
		return self.cURL(self.baseURL+'?random')

	# Fetches an octocat by its number
	# @param int number - the number of the octocat
	# @return the single octocat as an array
	
	def numberedOctocat(self, number):
		# do a cURL (in our cURL method) with baseURL appending '?number={@param number}' and return the result
		return self.cURL(self.baseURL+'?number='+str(number))

	# Performs all cURLs that are initated in each function, protected function
	# @param string endpoint is the URL of the cURL
	# @return the JSON as a parsed array
	
	def cURL(self, endpoint):
		# use urllib2 to perform a GET request and then use json to parse it
		return json.loads(urllib2.urlopen(endpoint).read())