import requests
from bs4 import BeautifulSoup

url = 'https://nypost.com/2023/01/03/chat-bots-could-be-key-to-early-alzheimers-detection/amp/'

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# get the page title
title = soup.title.string

# get all paragraphs on the page
paragraphs = soup.find_all("p")
for p in paragraphs:
    print(p.text)
