from bs4 import BeautifulSoup

with open("C:/Users/adiun/Documents/blinkit/page.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

script_tag = soup.find("script", id="__NEXT_DATA__")

if not script_tag:
    print("__NEXT_DATA__ script tag not found.")
else:
    print("Found __NEXT_DATA__ script tag.")
    print("Preview:", script_tag.string[:500])
