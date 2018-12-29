from check_who import check_who_ip,check_who_domain

def intel(query,type):
	'''
	Uses all of the scripts to get relevant information
'''

	if type == "domain":
		who_result = check_who_domain(query)
	elif type == "ip":
		who_result = check_who_ip(query)
	else:
		print(
	"[-]Please enter a valid type, currently supported is ip and domain\n	Example: \n		intel('1.1.1.1',type='ip')	OR	intel('www.google.com',type='domain')")
		return
	print(who_result)
intel("google.com","domain")
