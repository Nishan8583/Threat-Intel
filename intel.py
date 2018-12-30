from check_who import check_who_ip,check_who_domain
from pprint import pprint
from shodan_intel import shodan_query
from cymon_intel import cymon_query

def intel(query,type):
	'''
	Uses all of the scripts to get relevant information
'''
	# Whois

	if type == "domain":
		res = check_who_domain(query)

		# Getting creation_Date, expiraiton_Date and Last Updated date into more readable format
		cd = "{}-{}-{}".format(res["creation_date"].year, res["creation_date"].month,res["creation_date"].day)
		ed = "{}-{}-{}".format(res["expiration_date"].year, res["expiration_date"].month,res["expiration_date"].day)
		ld = "{}-{}-{}".format(res["last_updated"].year, res["last_updated"].month,res["last_updated"].day)

		# The years the domain has been available
		diff = res["expiration_date"].year - res["creation_date"].year

		# Replacing old values
		res["creation_date"] = cd
		res["expiration_date"] = ed
		res["last_updated"] = ld
		res["Age_of_domain"] = diff
		print(res)

	elif type == "ip":

		# Process similar to above
		res = check_who_ip(query)
		who_ip_result = {}
		who_ip_result['asn'] = res["asn"]
		who_ip_result["asn_country_code"] = res["asn_country_code"]
		who_ip_result['asn_description']= res['asn_description']
		who_ip_result['asn_registry'] = res['asn_registry']
		who_ip_result["network"] = res["network"]["cidr"]
		who_ip_result["country"] = res["network"]["country"]
		who_ip_result["end_address"] = res["network"]["end_address"]
		who_ip_result["start_address"] = res["network"]["start_address"]
		del res
		pprint(who_ip_result)
	else:
		print(
	"[-]Please enter a valid type, currently supported is ip and domain\n	Example: \n		intel('1.1.1.1',type='ip')	OR	intel('www.google.com',type='domain')")
	#return


	# Shodan

	#results = shodan_query(query,"mal")
	#pprint(shodan_result)
	#print("Result found: {}".format(results['total']))

	#for result in results["matches"]:
	#	pprint(result)


	# Cymon
	print("\n[+] Now querying cymon for threat intel data\n")
	cymon_result = cymon_query(query,type)
	print("[+] Cymon has detected {} counts of events".format(cymon_result['count']))
	if cymon_result['count'] > 0:  # if a threat intel event was regustered
		for result in cymon_result["results"]:
			tdd = result["created"].split("-")  # getting time from string
			year = tdd[0]
			month = tdd[1]
			day = tdd[2].split("T")[0]
			datec = "{}-{}-{}".format(year,month,day)
			print(
			'''On {}\n	Description: {}\n	Details_Url: {}\n	Tag: {}\n	Title: {}\n'''.format(datec,result['description'],result['details_url'],result['tag'],result['title'])
		)

if __name__ == '__main__':
	intel("87.244.210.165","ip")
