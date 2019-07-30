import requests
from bs4 import BeautifulSoup
import re
import datetime

resp = requests.get("http://www.srikanthtechnologies.com/rss.xml")

bs = BeautifulSoup(resp.text, "xml");

cur_year = datetime.date.today().year
for tag in bs.find_all("item"):
    pubdate = tag.find("pubDate").text
    m = re.search('\d{4}', pubdate)  # look for 4 digits (year)
    if m is None:
        continue

    if int(m.group()) == cur_year:
        title = tag.find("title").text
        print(title)
