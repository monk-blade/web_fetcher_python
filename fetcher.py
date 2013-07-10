from urllib import urlopen
 
from BeautifulSoup import BeautifulSoup
 
import re
import urllib2 
# Copy all of the content from the provided web page
webpage = urlopen('http://www.gktoday.in/gk/general-knowledge-quizzes/').read()
 
# Grab everything that lies between the title tags using a REGEX
#patFinderTitle = re.compile('')
 
# Grab the link to the original article using a REGEX
patFinderLink = re.compile('<a .*href="(.*)title=/"Quiz [0-100].*">')
 
# Store all of the titles and links found in 2 lists
#findPatTitle = re.findall(patFinderTitle,webpage)
 
findPatLink = re.findall(patFinderLink,webpage)
 
# Create an iterator that will cycle through the first 16 articles and skip a few
listIterator = []
 
listIterator[:] = range(6,10)
 
soup2 = BeautifulSoup(webpage)
 
#print soup2.findAll("title")
 
#titleSoup = soup2.findAll("title")
 
linkSoup = soup2.findAll("a")
#linkbit = soup2.a['href']

output = [ x["href"] for x in linkSoup ]
#print output
 
for i in listIterator:
      print output[i]
      pageFile = urllib2.urlopen(output[i])
      pageHtml = pageFile.read()
      pageFile.close()
      soup = BeautifulSoup("".join(pageHtml)) 
      sAll = soup.findAll("div","entry")
      print sAll
#    print linkSoup[i]
#    print linkbit
#    print "\n"
