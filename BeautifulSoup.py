import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
if len(url) < 1:
    url = 'https://www.google.com'                    #'http://data.pr4e.org/romeo.txt'
html = urllib.request.urlopen(url, context=ctx).read()          #context=ctx -> adde to igmore SSL cert
soup = BeautifulSoup(html, 'html.parser')

tags = soup('a')   # a -> give a list of all anchor tags in a doc
for tag in tags:
    print(tag.get('href', None))
