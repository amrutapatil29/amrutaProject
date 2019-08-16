import requests
from bs4 import BeautifulSoup
username = "codekul"
url = "http://www.codekul.com/"

response= requests.get (url)

soup= BeautifulSoup(response.text, 'html.parser')

all_links= soup.findAll("a")

for links in all_links:
    print (links.get('href'))
