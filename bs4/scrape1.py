import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

l= list()
i=0

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url= input('Enter url: ')
c= input('Enter count: ')
count= int(c)
p= input('Enter position:')
pos= int(p)

i=0

while i<count:
    l= list()
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")

    # Retrieve all of the anchor tags
    tags = soup('a')
    for tag in tags:
        x= tag.get('href',None)
        l.append(x)


    url= l[pos-1]
    print(url)
    del l[:]
    i= i+1
