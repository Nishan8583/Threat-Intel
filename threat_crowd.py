import requests,json
from pprint import pprint

def threat_crowd(query,type):
	'''
	The function queries threat crowd for threat intel information

	Ex:
		threat_crowd("1.1.1.1","IP")
		threat_crowd("www.google.com","Domain")

	Possible threat_crowd queries
	https://www.threatcrowd.org/searchApi/v2/email/report/?email=william19770319@yahoo.com
	https://www.threatcrowd.org/searchApi/v2/domain/report/?domain=aoldaily.com
	https://www.threatcrowd.org/searchApi/v2/ip/report/?ip=188.40.75.132
	https://www.threatcrowd.org/searchApi/v2/antivirus/report/?antivirus=plugx
	https://www.threatcrowd.org/searchApi/v2/file/report/?resource=ec8c89aa5e521572c74e2dd02a4daf78

	response will be like:
	{'hashes': ['191f253425e18e957b43f70a2d25614f'],  // List of malwares assiciated with this link
	 'permalink': 'https://www.threatcrowd.org/ip.php?ip=9.9.9.9',  // Search link for theis query
	 'references': [],
	 'resolutions': []  // list fo domains
	 'response_code': '1',	
 'votes': 0	}
if vote == -1	:
	most us	er did it malicious
elif vote == 0:
	equal 	number fo malicious and non malicious votes
elsif vote == 1:
	benign

	Reference: https://github.com/AlienVault-OTX/ApiV2
'''
	if type == "IP":
		url = "https://www.threatcrowd.org/searchApi/v2/ip/report/?ip={}".format(query)
	elif type == "Domain":
		url = "https://www.threatcrowd.org/searchApi/v2/domain/report/?domain={}".format(query)
	response = requests.get(url)
	text = json.loads(response.text)
	pprint(text)

#threat_crowd("1.1.1.1","ip")
