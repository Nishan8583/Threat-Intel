import requests

def botscout_query(query):
	'''
	Check if the query is associated with bot activity

	Usage:
		>>> botscout_query("1.1.1.1")
'''
	url = "http://botscout.com/test/?ip={}".format(query)
	resp = requests.get(url)

	print(resp.text)

#botscout_query("1.1.1.1")
