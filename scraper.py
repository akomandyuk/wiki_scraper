import requests
from bs4 import BeautifulSoup
import random


def scrapeWikiArticle(url):
    response = requests.get(url=url)
    soup = BeautifulSoup(response.content, 'html.parser')

    title = soup.find(id="firstHeading")
    print(title.text)

    # Get all the links
    all_links = soup.find(id="bodyContent").find_all("a")
    random.shuffle(all_links)
    link_to_scrape = 0

    for link in all_links:
        if link['href'].find("/wiki/") == -1:
            continue
        link_to_scrape = link
        break

    scrapeWikiArticle("https://en.wikipedia.org" + link_to_scrape['href'])


scrapeWikiArticle("https://en.wikipedia.org/wiki/Web_scraping")
