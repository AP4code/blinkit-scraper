from bs4 import BeautifulSoup

with open("C:/Users/adiun/Documents/blinkit/page.html", "r", encoding="utf-8") as file:
    html = file.read()

soup = BeautifulSoup(html, "html.parser")

table = soup.find("table")
if not table:
    print("No table found.")
    exit()

rows = table.find_all("tr")

products = []
for row in rows:
    cells = row.find_all("td")
    if len(cells) >= 2:
        name = cells[0].get_text(strip=True)
        price = cells[1].get_text(strip=True)
        products.append((name, price))

if not products:
    print("No products found in the table.")
else:
    print("Products found:")
    for name, price in products:
        print(f"- {name}: {price}")

import csv

with open("products.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Product", "Price"])
    writer.writerows(products)

print("Saved to products.csv")

