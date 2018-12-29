import shodan,sys
from get_key import get_key

def query(address,type):
	if type == "mal":
		address = "category:malware " + address
	key = get_key("shodan")

	searcher = shodan.Shodan(key)  # Shodan Object

	# query shodan
	results = searcher.search(address)
	print("Result found: {}".format(results['total']))

	for result in results["matches"]:
		print(result)


#query_ip(sys.argv[1]"mal")
