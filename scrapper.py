gallery_url = r"https://azurlane.koumakan.jp/wiki/List_of_Ships_by_Image"
import attr
from bs4 import BeautifulSoup

import json
import requests

page = requests.get(gallery_url)
soup = BeautifulSoup(page.text, "html.parser")
ships = {}

gallery = soup.findAll("div", class_="alc-img")

for scan in gallery:
    rarity = scan.attrs["class"][-1][-1]

    link = scan.find("span").find("a")
    title = link["title"]
    href = link["href"]
    src = link.find("img")["src"]
    print(src)

    ship = {"title": title, "href": href, "src": src}

    if not rarity in ships:
        ships[rarity] = {}

    ships[rarity][title] = ship

    # print(scan.find("span").find("a")["title"])
    # print(scan)


def getFull(shipUrl):
    

with open("gallery.json", "w", encoding="utf-8") as f:
    f.write(json.dumps(ships, ensure_ascii=False))
