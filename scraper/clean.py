import pandas as pd
from scraper.email_utils import generate_email_formats

def clean_dataframe(quotes):
    """
    Convert scraped quote data into a clean Pandas DataFrame.
    Removes duplicates, fills missing values, strips whitespace,
    and resets the index.
    """
    df = pd.DataFrame(quotes)

    df = df.drop_duplicates()
    df = df.fillna("N/A")

    df = df.apply(lambda col: col.str.strip() if col.dtype == "object" else col)

    df = df.reset_index(drop=True)

    df["email_guesses"] = df["author"].apply(
        lambda name: generate_email_formats(name, "example.com")
    )

    return df