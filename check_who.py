#!/usr/bin/python
import whois,sys
from ipwhois import IPWhois
from pprint import pprint
def check_who_domain(domain):
	'''This function is responsible for gathering whois information about domain\n
	check_who(domain) gives infomraiton about the domain\n
	Ex:\n
		from check_who import check_who_domain\n
		check_who_domain('google.com')'''
	try:
		print("[+] Gathering Whois Information about the domain \n")
		qob = whois.query(domain).__dict__  # Obtaining dictionary object from the domain object
		message = \
"Creation_date: Year: {} Month: {} Day: {} \nUpdated: Year: {} Month: {} Day: {}\nRegistrar: {} \nCreation_date: Year: {} Month: {} Day: {}".format(qob["creation_date"].year,qob["creation_date"].month,qob["creation_date"].day,qob["last_updated"].year,\
		qob["last_updated"].month,qob["last_updated"].day,qob["registrar"],qob["expiration_date"].year,qob["expiration_date"].month,qob["expiration_date"].day)
		print(message)
	except:
		print("[-] Could not get info, Are you sure you entered the right domain?...")


def check_who_ip(address):
	'''This function is responsible for gathering whois information about IP address\n
        check_who_ip(domain) gives infomraiton about the domain\n
        Ex:\n
                from check_who import check_who_ip\n
                check_who_ip('8.8.8.8')'''

	obj = IPWhois(address)
	result = obj.lookup_rdap(depth=0)
	pprint(result) # Raw result
	#msg =\
	#'''ASN: {}, \nASN_COUNTRY: {}\nASN_DATE: {}\n Network:{} \n'''
#if __name__ == '__main__':
#	check_who_ip(sys.argv[1])
