from bs4 import BeautifulSoup
import urllib 
import urllib2
import wget
import os
i=1
os.system("rm *.pdf")

pageFile = urllib2.urlopen("http://www.epw.in/ejournal/show/1/_/3068")
 
pageHtml = pageFile.read()
 
pageFile.close()
 
soup = BeautifulSoup("".join(pageHtml))


#sAll = soup.findAll("div", "sectionon")
sAll = soup.findAll("em")[0].next

issue_name=sAll.replace(' ','').replace('Vol.50,','').replace('.','').replace(',','_')

data = soup.findAll('div',attrs={'class':'content-content'});
for div in data:
    links = div.findAll('a')
    for a in links:
        b = "http://www.epw.in" + a['href'];
        pageFile = urllib2.urlopen(b)
        pageHtml = pageFile.read()
        pageFile.close()
        soup = BeautifulSoup("".join(pageHtml))
        data = soup.findAll('div',attrs={'class':'filefield-file'});
        for div in data:
            links = div.findAll('a')
            for a in links:
                pdflinks = a['href'];
                print "\n Downloading :" + pdflinks
                wget.download(pdflinks,out=str(i).zfill(2)+".pdf")
                i += 1
                #print "\n"
                #print i
                #print "\n"
pdf_merge="pdftk *.pdf cat output " + issue_name + ".pdf"

os.system(pdf_merge)
