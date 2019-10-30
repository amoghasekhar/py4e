import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

sum=0

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    x= tag.contents[0]
    y= int(x)
    sum= sum+y

print('Sum',sum)
