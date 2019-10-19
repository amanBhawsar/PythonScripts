import requests
import unicodedata
import os
import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup

from googlesearch import search 
# to search 
query = "Aman Bhawsar"
urlCollection = []  
for j in search(query, tld='com', lang='en', num=10, start=0, stop=10, pause=2): 
    urlCollection.append(j)
# print(urlCollection)
user_agent = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}

ctr = int(0)
#os.makedirs(query)
for url in urlCollection:
    ctr = ctr + 1
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')
    fileN = './'+query+'/'+str(ctr)+'.html'
    soup = soup.encode("utf-8")
    with open(fileN, "w") as file:
        k = (str(soup)).replace('\\n', '')
        k = k.replace('b\'', '')
        print(k+"\n")
        file.write(k)
'''
import urllib.request, urllib.error, urllib.parse

url = 'http://www.oldbaileyonline.org/browse.jsp?id=t17800628-33&div=t17800628-33'

response = urllib.request.urlopen(url)
webContent = response.read()

f = open('obo-t17800628-33.html', 'w')
f.write(webContent.decode("utf-8") )
f.close

'''
