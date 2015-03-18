import requests
from bs4 import BeautifulSoup


url = "http://dailybruin.com/category/news/" #saves the url
r = requests.get(url)

soup = BeautifulSoup(r.content) #soup will hold the contents of the website

data = soup.find_all("h2") #search for all lines with h2

#could not figure out how to do only the headlines, but did get all headlines
for item in data:
    print item.text.strip() #prints the text and strips
