# Example plugin using requests library to access Wolfram Alpha's API 
# See https://products.wolframalpha.com/short-answers-api/documentation/ for API information
from grossmaulplugin import GrossmaulPlugin
# 
from urllib import parse
import requests

APPID = 'ENTER APP ID HERE' # Request your free API access at https://products.wolframalpha.com/api/ and place it here
ENDPOINT = 'http://api.wolframalpha.com/v1/result' 

class WolframPlugin(GrossmaulPlugin):
	def __init__(self):
		self.OPERATORS = {}
		self.COMMANDS = {'wolfram' : self.comWolfram }
		self.PROCESSCOMMANDS = {'wolfram' : False }

	def comWolfram(self, message, sender, STATE, private=False):
		# strip out command from message
		message = message[len('wolfram')+1:].lstrip()

		# create a dictionary with parameters to be passed, encoded for HTTP
		request_parameters = parse.urlencode({ 'appid' : APPID, 'i' : message })
		response = requests.get(ENDPOINT, params = request_parameters)
		# make sure our request was successful
		if response.status_code is requests.codes.ok:
			return '[Wolfram] ' + response.text
		elif response.status_code == 501:
			return '[Wolfram] Input cannot be interpreted, please rephrase your question'
		else:
			return '[Wolfram] Error code ' + str(response.status_code)

