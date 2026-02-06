#Question 9
from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://en.wikipedia.org/wiki/Machine_learning"

headers = {                                                           #adding headers to avoid being blocked by the website
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')
content = soup.find('div', id='mw-content-text')                     # Locate main content area

# Find all tables on the page
tables = content.find_all("table")

target_table = None        # Initialize variable to store the first qualifying table

for table in tables:
    # Check if table is inside mw-content-text (if it exists)
    data_rows = table.find_all("tr")
    if len(data_rows) >= 3:  # at least 3 rows
        table_to_extract = table
        break


    rows = table.find_all("tr")
    data_rows = [r for r in rows if r.find_all("td")]

    if len(data_rows) >= 3:
        target_table = table
        break

if table_to_extract:
    # Extract headers
    headers = [th.get_text(" ",strip=True) for th in table_to_extract.find_all("th")]
    if not headers:
        # If no <th> present, we create generic headers
        first_row = table_to_extract.find("tr")
        num_cols = len(first_row.find_all(["td", "th"]))
        headers = [f"col{i+1}" for i in range(num_cols)]

    # Extract rows
    rows = []
    for tr in table_to_extract.find_all("tr"):
        cells = tr.find_all(["td", "th"])
        row = [cell.get_text(" ",strip=True) for cell in cells]
        # Pad missing values
        while len(row) < len(headers):
            row.append("")
        rows.append(row)

    df = pd.DataFrame(rows[1:], columns=headers)  # convert to DataFrame and save CSV  # skip first row if it's header

    print(df)
    #df.to_csv("wiki_table.csv", index=False)
    print("Table extracted and saved to wiki_table.csv")
else:       # if we can not find a table that meets the criteria

    print("No table with at least 3 rows found in the main content area.")
    pd.DataFrame().to_csv("wiki_table.csv", index=False)   #create an empty cvs file to still meet the assignment requirements
    print("Empty CSV created: wiki_table.csv")

