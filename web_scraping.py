from bs4 import BeautifulSoup

import requests

import pandas as pd

player = "8332"
url = "https://www.pdga.com/player/" + player
result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")


tags = ["nationality", "join-date","current-rating",
"current-rating", "career-wins disclaimer", "career-earnings",
"world-rank"]
my_list = []
for c in tags:
    item = doc.find("li", class_ = c)
    info = item.text.split(":")
    temp_list = []
    for x in info:
        temp_list.append(x.strip())
    my_list.append(temp_list)
df = pd.DataFrame(my_list)
print(df)