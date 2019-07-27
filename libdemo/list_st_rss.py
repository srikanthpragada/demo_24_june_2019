
import requests
from bs4 import BeautifulSoup

resp = requests.get("http://www.srikanthtechnologies.com/rss.xml")

bs = BeautifulSoup(resp.text,"xml");

for tag in bs.find_all("title"):
    print(tag.text)






