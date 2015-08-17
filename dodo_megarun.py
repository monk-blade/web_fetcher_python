from bs4 import BeautifulSoup
import urllib 
import urllib2
import wget
import os
for num in range(3035,3069):
    i=1
    os.system("rm [0-9]*")

    urlll="http://www.epw.in/ejournal/show/1/_/"+str(num)
    print "Downloading new issue from :" + urlll 
    pageFile = urllib2.urlopen(urlll)
 
    pageHtml = pageFile.read()
     
    pageFile.close()
     
    soup = BeautifulSoup("".join(pageHtml))


    #sAll = soup.findAll("div", "sectionon")
    sAll = soup.findAll("em")[0].next

    issue_name=sAll.replace(' ','').replace('.','').replace(',','_')

    data = soup.findAll('div',attrs={'class':'content-content'});
    for div in data:
        links = div.findAll('a')
        for a in links:
            b = "http://www.epw.in" + a['href'];
            pageFile = urllib2.urlopen(b)
            pageHtml = pageFile.read()
            pageFile.close()
            soup = BeautifulSoup("".join(pageHtml))
            data1 = soup.findAll(attrs={"name":"citation_pdf_url"}) 
            pdflinks = data1[0]['content'].encode('utf-8')
            print "\n Downloading :" + pdflinks
            dlink = "wget --load-cookies=/home/ubuntu/workspace/koki.txt " + pdflinks + " -O " + str(i).zfill(2)+"_"+pdflinks.replace('http://www.epw.in/system/files/pdf/','').replace('/','')
            os.system(dlink)
            i += 1
                    #print "\n"
                    #print i
                    #print "\n"
    pdf_merge="pdftk *.pdf cat output " + issue_name + ".pdf"

    os.system(pdf_merge)
