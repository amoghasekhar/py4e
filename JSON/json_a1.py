import json
import urllib.request, urllib.parse, urllib.error
import ssl

ctx= ssl.create_default_context()
ctx.check_hostname= False
ctx.verify_mode= ssl.CERT_NONE

url= input('Enter- ')
uh= urllib.request.urlopen(url, context=ctx)
data= uh.read()

sum=0

info= json.loads(data.decode('utf-8'))

for i in info['comments']:
    x= i['count']
    y= int(x)
    sum= sum+y

print('Sum',sum)
