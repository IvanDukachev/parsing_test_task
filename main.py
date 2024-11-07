import requests
from collections import defaultdict
from bs4 import BeautifulSoup
import json


page = 1
data = defaultdict(list)
data["tags"] = set()

while True:
    url = f"https://quotes.toscrape.com/page/{page}/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    result = soup.find_all("div", class_="quote")
    if not result:
        break

    for res in result:
        quote = res.find_all("span")
        author = quote[1].small.text
        data[author].append(quote[0].text[1:-1])
        for tag in res.find_all("a", class_="tag"):
            data["tags"].add(tag.text)

    page += 1

data["tags"] = list(data["tags"])

with open('data.json', 'w') as file:
    json.dump(data, file)
