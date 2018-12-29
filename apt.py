import requests,sys

def get_apt_report(query):
	'''
	The job of the function is to query www.threatminer.org, to see if the IP/domain/hash or any other stuff is associated
	with a particular APT. This threat intel source is a great one, and I was lucky enought to find it :)
'''
	url = "https://api.threatminer.org/v2/host.php?q={}&rt=6".format(query)
	resp = requests.get(url)
	response = resp.text

	print(response)

get_apt_report("1.1.1.1")
