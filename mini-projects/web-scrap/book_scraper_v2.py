from bs4 import BeautifulSoup
import requests
import csv

with open("scrapeBooksssss.csv", "w", newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["TITLES", "PRICES", "STOCK"])

    for i in range(1, 11):
        i = str(i)
        text = "https://books.toscrape.com/catalogue/page-" + i + ".html"
        page_to_scrape = requests.get(text)
        soup = BeautifulSoup(page_to_scrape.text, "html.parser")
        titles = soup.findAll("h3")
        prices = soup.findAll("p", attrs={"class": "price_color"})
        stocks = soup.findAll("p", attrs={"class": "instock availability"})

        for title, price, stock in zip(titles, prices, stocks):
            title_text = title.text.strip()
            price_text = price.text.strip()
            stock_text = stock.text.strip()

            print(title_text + " - " + price_text + " - " + stock_text)
            writer.writerow([title_text, price_text, stock_text])
