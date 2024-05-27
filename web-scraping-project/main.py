from bs4 import BeautifulSoup
import requests
import csv

OUTPUT_PATH = "C:/Users/wired/Desktop/udemy/end-projects/web-scraping-project/billboard-top-100.csv"

response = requests.get("https://www.billboard.com/charts/hot-100/")
web_data = response.text

soup = BeautifulSoup(web_data, "html.parser")

divs = soup.find_all("div", class_="o-chart-results-list-row-container")
span_elements = soup.select('span.c-label.a-no-trucate.a-font-primary-s')

with open(OUTPUT_PATH, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Rank", "Title", "Artists"])

    for div, span_element in zip(divs, span_elements):
        rank = div.find(class_="c-label").text.strip()
        title = div.find("h3", class_="c-title").text.strip()
        artist = span_element.get_text(strip=True)

        writer.writerow([rank, title, artist])



