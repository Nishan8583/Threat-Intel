import requests,json,sys
from get_key import get_key

def query_malshare(query):

	'''
	Get Malshare data:

	Prerequisite:
		You are expected to have obtained a malshare API key, and put it in config.txt
		Ex:
			Config.txt
				....
				malshare:<your API key here>

	Usage:
		>>> from malshare_query import query_malshare
		>>> query_malshare("domainname or IP address")


'''
	key = get_key("malshare")

	# The query is super late
	url = "https://malshare.com/api.php?api_key={}&action=search&query={}".format(key,query)  # malshare API URL
	resp = requests.get(url).text
	print(json.dumps(resp,sort_keys=True, indent=4, separators=(',', ': ')))

#query_malshare(sys.argv[1])
