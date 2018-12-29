import requests,json
from get_key import get_key
from pprint import pprint

def cymon_query(query,type):
	"""
	This function queries cymon.io for threat intel information
	Cymon is very cool, in that it gives time information, such as which event happened in which time,

	prerequisite: Create an cymon account, and generate an API key, the API key has its limitation, see the reference links for more details
			Also paste the API key in config.txt, cymon_key section
			Ex: cymon_key:<your key here>

	Ex:
		>>> from cymon_intel import cymon_query
		For IP query
		>>> cymon_query("1.1.1.1","IP")

		For Domain Query
		>>> cymon_query("www.google.com","Domain")


	Response For cymon Example:
	{'count': 469,
 'next': 'https://cymon.io/api/nexus/v1/ip/1.1.1.1/events?limit=10&offset=10',
 'previous': None,
 'results': [{'created': '2018-11-22T19:04:18Z',
              'description': 'Domain: www.nlus-romania.ro',
              'details_url': None,
              'tag': 'phishing',
              'title': 'Phishing reported by Google SafeBrowsing',
              'updated': '2018-11-22T19:04:18Z'},
             {'created': '2018-11-22T19:03:51Z',
              'description': 'Domain: nlus-romania.ro',
              'details_url': None,
              'tag': 'phishing',
              'title': 'Phishing reported by Google SafeBrowsing',
              'updated': '2018-11-22T19:03:51Z'},
             {'created': '2018-10-27T18:06:07Z',
              'description': 'Domain: c.dzytccjq.com',
              'details_url': None,
              'tag': 'malware',

	The above is the detailed response from cymon, If you want more detailed output, modify the script per your re	quirement


	Reference: https://cymon.io/cp/api
	https://cymon.io/api/docs/#!/ip/Malware_list
"""
	api_key = get_key("cymon_key")
	if type == "IP":
		url = "https://cymon.io/api/nexus/v1/ip/{}/events".format(query)
	elif type == "Domain":
		url = "https://cymon.io/api/nexus/v1/domain/{}".format(query)
	headers = {"authorization": "Token {}".format(api_key)}
	response = requests.get(url,headers=headers)
	res = json.loads(response.text)
	pprint(res)


#cymon_query("www.google.com","Domain")

