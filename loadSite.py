from bs4 import BeautifulSoup
import requests
import sys

size = 0

def getSiteMap(url):
	xmlDict = {}

	r = requests.get(url)
	xml = r.text

	soup = BeautifulSoup(xml, 'lxml')
	sitemapTags = soup.find_all("sitemap")

	print ("The number of sitemaps are {0}".format(len(sitemapTags)))

	for sitemap in sitemapTags:
		xmlDict[sitemap.findNext("loc").text] = sitemap.findNext("lastmod").text

	for x in xmlDict:
		print(x)
		if("index" in x):
			getSiteMap(x)
		else:
			getWebPage(x)
	global size
	print("Current size = " + str(size))

def getWebPage(url):
	xmlDict = {}

	r = requests.get(url)
	xml = r.text

	soup = BeautifulSoup(xml, 'lxml')
	sitemapTags = soup.find_all("url")
	
	print ("The number of urls are {0}".format(len(sitemapTags)))

	for sitemap in sitemapTags:
		xmlDict[sitemap.findNext("loc").text] = sitemap.findNext("lastmod").text

	for x in xmlDict:
#		print(x)
			response = requests.get(url)
			s = len(response.content)
			global size
			size = size + s
		
def main():
	print(sys.argv[1])
	print('running')
	try:
		getSiteMap(sys.argv[1])
	except:
		print("Error")

if __name__=="__main__":
    main()
