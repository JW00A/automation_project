import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def parse_quotes(html, url):
    """
    Scrape quotes, authors, and author links from HTML content.
    Returns a list of dictionaries.
    """
    soup = BeautifulSoup(html, "html.parser")

    quotes = []

    for q in soup.select("div.quote"):
        text = q.select_one("span.text")
        author = q.select_one("small.author")
        link_tag = q.select_one("a")
        link = link_tag["href"] if link_tag else None

        if text and author:
            quotes.append({
                "text": text.text.strip(),
                "author": author.text.strip(),
                "link": urljoin(url, link)
            }) 
    
    return quotes