# Blinkit Scraper — Dcluttr Task 1

This repository contains my solution for Task 1 of the Dcluttr data challenge.

---

## What it does

This project scrapes product listings from a Blinkit subcategory page (like Nachos), and exports the data into a CSV file. Since Blinkit doesn't expose this data through an open API, I used a real browser to render the page and extract the data from the HTML.

---

## Files included

| File | What it does |
|------|---------------|
| `test.py` | Opens the page using undetected-chromedriver and saves the full HTML (`page.html`) |
| `page.html` | Snapshot of the loaded Blinkit page (used for offline parsing) |
| `parse_products.py` | Extracts product names and prices from the HTML and writes them to `products.csv` |
| `products.csv` | Final output with clean product data |

---

## How to run it

1. Install required packages (once):
   ->
   pip install selenium undetected-chromedriver beautifulsoup4
