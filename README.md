# automation_project
## Project Overview
This project automates the process of scraping quotes and author names from QuotesToScrape.com, cleaning the data, generating possible email formats for each author, and exporting the final dataset to an Excel file. The goal is to demonstrate basic automation, data extraction, and data processing skills.

## Tools & Technologies
- **Python 3**
- **Requests** – fetching HTML pages
- **BeautifulSoup (bs4)** – parsing HTML
- **Pandas** – cleaning and structuring data
- **OpenPyXL** – Excel export engine

## How to Run the Project
- Install dependencies:
**pip install -r requirements.txt**
- Run the script:
**python main.py**
- The output Excel file will appear in the project folder.

## Output
The script generates an Excel file containing:
- Quote text
- Author name
- Author page link
- Generated email formats

## Automation
The script is structured so it can be scheduled using:
- Windows Task Scheduler
- Cron (Linux/Mac)
