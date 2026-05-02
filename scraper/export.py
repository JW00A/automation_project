import pandas as pd

def export_to_excel(df, filename="quotes.xlsx"):
    """
    Export a Pandas DataFrame to an Excel file.
    """
    df.to_excel(filename, index=False)

    print(f"Saved Excel file: {filename}")