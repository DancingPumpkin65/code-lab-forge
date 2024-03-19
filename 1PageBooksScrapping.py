from bs4 import BeautifulSoup
import requests
import csv

page_to_scrape = requests.get("https://books.toscrape.com")
soup = BeautifulSoup(page_to_scrape.text, "html.parser")
titles = soup.findAll("h3")
prices = soup.findAll("p", attrs={"class":"price_color"})
stocks = soup.findAll("p", attrs={"class":"availability"})

with open("OnePageSSS.csv", "w", newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["TITLES", "PRICES"])
    for title, price in zip(titles, prices) : 
        print(title.text + " - " + price.text)
        writer.writerow([title.text, price.text])
