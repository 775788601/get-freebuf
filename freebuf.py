# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
'''
try:
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    print response.read()
except urllib2.URLError, e:
    if hasattr(e, "code"):
        print e.code
    if hasattr(e, "reason"):
        print e.reason


request = urllib2.Request(url)
response = urllib2.urlopen(request)
#content = response.read().decode('utf-8')
content = response.read()
pattern=re.compile('<div class="news_inner news-list">(.*?)</div>',re.S)
items = re.findall(pattern,content)
pattern1=re.compile('title="(.*?)"',re.S)
pattern2=re.compile('href="(.*?)"',re.S)
## print items[0]
for i in items:
    #print i
    items1= re.findall(pattern1,i)
    items2 = re.findall(pattern2, i)
    print items1[0],items2[0]
'''

pattern = re.compile('<div class="news_inner news-list">(.*?)</div>', re.S)
pattern1 = re.compile('title="(.*?)"', re.S)
pattern2 = re.compile('href="(.*?)"', re.S)


def getfreebuf(start,stop,name):
    fp = open(name, "w")
    fp.write('<html xmlns="http://www.w3.org/1999/xhtml">\n<head>\n<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />\n</head>\n<body>\n')
    for page in range(start,stop):
        url = 'http://www.freebuf.com/page/' + str(page)
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        content = response.read()
        items = re.findall(pattern, content)
        for i in items:
            items1 = re.findall(pattern1, i)
            items2 = re.findall(pattern2, i)
            #print items1[0], items2[0]
            fp.write ('<p><a href="'+items2[0]+'" >'+items1[0]+'</a></p>\n')
    fp.write('\n</body>\n</html>')
    fp.close()


#getfreebuf(1,10,'1-10.html')
start = raw_input("开始：");
stop = raw_input("结束：");
#print "你输入的内容是: ", start,stop
getfreebuf(int(start) ,int(stop)+1,start+'-'+stop+'.html')
print "\n结束\n"