from BeautifulSoup import BeautifulSoup
 
import urllib2

pageFile = urllib2.urlopen("http://www.halfmantr.com/disaster-management/1429-development-and-disaster")
 
pageHtml = pageFile.read()
 
pageFile.close()
 
soup = BeautifulSoup("".join(pageHtml))
 
sAll = soup.findAll("div", "newsitem_text")
#print(soup.prettify())
print sAll
