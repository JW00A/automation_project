from scraper.fetch import fetch_page
from scraper.parse import parse_quotes
from scraper.clean import clean_dataframe
from scraper.export import export_to_excel

def main():
    base_url = "https://quotes.toscrape.com/page/{}/"

    all_quotes = []

    for page in range(1, 4):
        url = base_url.format(page)
        html = fetch_page(url)

        if html is None:
            print(f"Failed to fetch page {page}")
            continue

        quotes = parse_quotes(html, url)
        all_quotes.extend(quotes)
    
    df = clean_dataframe(all_quotes)
    export_to_excel(df, "quotes.xlsx")

if __name__ == "__main__":
    main()