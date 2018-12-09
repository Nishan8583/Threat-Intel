#!/usr/bin/python
import requests,sys,json
from get_key import get_key

def hybrid_query(query,type):
	'''	Queries hybrid analysis for informationn\n
	Hybrid is a great resource to see what activities the IP address was involved in
	Usage:
		from hybrid import hybrid_query
		hybrid_query("104.27.163.228")
'''
	key = get_key("Hybrid")  # Get the key from config file, Change it as necessary
	url = "https://www.hybrid-analysis.com/api/v2/search/terms"  # The api url
	headers={"api-key":key,"user-agent":"Falcon Sandbox","accept":"application/json"}  # The request headers
	if type == "domain":
		data={"domain":query}  # The data to post
	elif type == "ip":
		data={"host":query}
	else:
		return
	resp = requests.post(url,headers=headers,data=data)
	response = json.loads(resp.text)

	if response["count"] == 0:  # If no result was recieved
		print("Could not recieve value")
		return
	else:
		c = response["count"]
		print("[+] Hybrid analysis has got {} matches\n".format(c))
		for i in range(0,c):
			# Parsing the data
			print("Match No: {}\n".format(i))
			verdict = response["result"][i]['verdict']
			av_detect = response["result"][i]['av_detect']
			threat_score = response["result"][i]['threat_score']
			hash = response["result"][i]['sha256']
			submit_name = response["result"][i]['submit_name']
			analyzed_in = response["result"][i]['analysis_start_time']
			msg = "Verdit: {}\nAV_Detection: {}\nThreat_Score: {}\nSHA256_HASH: {}\nSubmit_Name: {}\nAnalyzed_in: {}\n".\
format(verdict,av_detect,threat_score,hash,submit_name,analyzed_in)
			print(msg)

hybrid_query(sys.argv[1],"domain")

