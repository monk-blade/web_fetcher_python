from urllib import urlopen
 
from BeautifulSoup import BeautifulSoup
 
import re
import urllib2 
# Copy all of the content from the provided web page
webpage = urlopen('http://www.halfmantr.com/environment').read()
 
# Grab everything that lies between the title tags using a REGEX
#patFinderTitle = re.compile('')
 
# Grab the link to the original article using a REGEX
#patFinderLink = re.compile('<a .*href="(.*)title=/"Quiz [0-100].*">')
 
# Store all of the titles and links found in 2 lists
#findPatTitle = re.findall(patFinderTitle,webpage)
  
#create list iterator
listIterator = []
 
listIterator[:] = range(0,50)
 
soup2 = BeautifulSoup(webpage)

 
#titleSoup = soup2.findAll("title")
 
linkSoup = soup2.findAll("a" , "yjnewsflash_title")
#fetching links

output = [ x["href"] for x in linkSoup ]
#fetching href(url) attribute value
 
for i in listIterator:
      
      #print "Fetching article http://www.halfmantr.com" + output[i]
      pageFile = urllib2.urlopen("http://www.halfmantr.com" + output[i])
      pageHtml = pageFile.read()
      pageFile.close()
      soup = BeautifulSoup("".join(pageHtml)) 
      sAll = soup.findAll("div","newsitem_text")
      for member in sAll:
         print member

