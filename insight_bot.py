#coding=UTF-8

from bs4 import BeautifulSoup
import urllib 
import urllib2
import re
pageFile = urllib2.urlopen("http://www.insightsonindia.com/secure-2015/")
 
pageHtml = pageFile.read()
 
pageFile.close()
 
soup = BeautifulSoup("".join(pageHtml))


topic = soup.findAll('li')
#ttc = topic.find('a')
#print(soup.prettify())
#print topic
for tag in topic:
	tdTags = tag.find_all("a", text = re.compile(ur'^[0-9](.*)July(.*)2015.*', re.DOTALL))
	for tag in tdTags:
		list_url = tag['href']
		pageFile = urllib2.urlopen(list_url.encode('utf-8'))
		pageHtml = pageFile.read()
		pageFile.close()
		soup = BeautifulSoup("".join(pageHtml))
		ttl = soup.findAll('title')[0].next
		print "<center><h2>" + ttl.encode('cp1252') +"</h2></center>"
		tdTags = soup.find_all("a", text = re.compile(ur'[0-9](.*)Words.*', re.DOTALL))
		for tag in tdTags:
			que_url = tag['href']
			pageFile = urllib2.urlopen(que_url.encode('utf-8'))
			pageHtml = pageFile.read()
			pageFile.close()
			soup = BeautifulSoup("".join(pageHtml))
			#topic = soup.findAll('blockquote')[0].next
			que = soup.findAll('title')[0].next
			print "<span style=\"color: #3366ff;\"><h3>"
			print que.encode('utf-8')
			print "</h3></span>"
			for topic in soup.findAll('blockquote'):
				if len(topic.text) > 1:
					print topic.encode('cp1252')
				break
			print "\n\n"
			num = 1
			for strong_tag in soup.findAll('div',attrs={'class':'dsq-comment-message'}):
			    if len(strong_tag.text) >= 500:
			        print "<b>ANSWER-" + str(num)+ ":</b>"
			        print strong_tag.encode('cp1252')
			        print "\n"
			        num += 1
			    if num == 3:
			     	break
