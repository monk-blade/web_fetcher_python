
from bs4 import BeautifulSoup
import urllib 
import urllib2
import re

pageFile = urllib2.urlopen("http://www.insightsonindia.com/the-big-picture-debates/")
 
pageHtml = pageFile.read()
 
pageFile.close()
 
soup = BeautifulSoup("".join(pageHtml))


topic = soup.findAll('li')
#ttc = topic.find('a')
#print(soup.prettify())
#print topic
for tag in topic:
	tdTags = tag.find_all("a", text = re.compile(ur'(.*)(Lok Sabha TV Insights|Public Private Partnership|Lok Sabha Insights|Big Picture|World|State of the Economy|Special Report|News Analysis|Constitutional Logjam)(.*)', re.DOTALL))
	for tag in tdTags:
		try:
			list_url = tag['href']
			pageFile = urllib2.urlopen(list_url.encode('utf-8'))
			pageHtml = pageFile.read()
			pageFile.close()
			soup = BeautifulSoup("".join(pageHtml))
			ttl = soup.findAll('title')[0].next
			print "<center><h2>" + ttl.encode('cp1252') +"</h2></center>"
			#num = 1
			for strong_tag in soup.findAll('div',attrs={'class':'pf-content'}):
				   if len(strong_tag.text) >= 500:
				       #print "<b>ANSWER-" + str(num)+ ":</b>"
				       print strong_tag.encode('cp1252')
				       #print "\n"
				    #   num += 1
				   #if num == 3:
				   #  	break
		except:
			continue
