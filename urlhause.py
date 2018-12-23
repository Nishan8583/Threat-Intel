from bs4 import BeautifulSoup
import requests,sys

def urlhause(query):
	"""
	The URLHause us a very nice threat feed site, which can be used to see which website delivers which malware.
	That being said, they only provide API to download csv dumps of their registered malicious domain and currently the API
	can not be used to query for information directly. While downloading dumps is easy and quick, it is not real when you want real 
	time data. So I created a web scraper using requests and BeautifulSoup module. It queries the site by changing the URL.
	And scarping the HTML resonse obtains the result.

	Example:


			>>> from urlhause import urlhause
			>>> urlhause("senorita")
			Date: 2018-07-07 06:14:04 Link: http://www.senoritasmargaritas.com/wp-includes/... 
			Status: Offline, Tags: doc Trickbot  , Reporter: @p5yb34m
			>>> urlhause("<any IP address>")

	NOTE: The script obtains any useful infomration from the HTML response, however if you feel like it does not
	Change per your will
"""
	response = requests.get("https://urlhaus.abuse.ch/browse.php?search={}".format(query))
	lost = response.text
	soup = BeautifulSoup(lost,"html.parser")
	tables = soup.find("table")

	all_rows = tables.find_all("tr")
	if len(all_rows) < 2:
		print("Not listed in URLHause")
	else:
		for i in range(1,len(all_rows)):
			get_tds = all_rows[i].find_all("td")
			print("|Date: {}| 	|Link: {}|	 |Status: {}|	 |Tags: {}|	 |Reporter: {}|\n".format(get_tds[0].text,get_tds[1].text,get_tds[2].text,get_tds[3].text,get_tds[4].text))
urlhause(sys.argv[1])








































# IyBJIGZ1a2VuIGhhdGUgdmVyeXRoaW5nLCBpbmNsdWRpbmcgbXlzZWxm
