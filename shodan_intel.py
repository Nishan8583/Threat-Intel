import shodan,sys
from get_key import get_key

def shodan_query(address,type):
	if type == "mal":
		address = "category:malware " + address
	key = get_key("shodan")

	searcher = shodan.Shodan(key)  # Shodan Object

	# query shodan
	results = searcher.search(address)
	#return results
	print("Result found: {}".format(results['total']))

	for result in results["matches"]:
		print(result)


#shodan_query(sys.argv[1]"mal")
