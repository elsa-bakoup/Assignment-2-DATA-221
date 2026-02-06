#Question 8
from bs4 import BeautifulSoup
import requests

# adding headers to avoid being blocked by the website
headers = {
    "User-Agent": "Mozilla/5.0"
}

url = "https://en.wikipedia.org/wiki/Data_science"
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

headings = soup.find('div', id='mw-content-text').find_all('h2')  #finding the right tags and class

exclude = ["References", "External links", "See also", "Notes"]   #creating a list with excluded words to remove specific lines

clean_headings = []

for h in headings:
    text = h.get_text(strip=True).replace("[edit]", "").strip() #striping the text and removing any edit from the headings
    if not any(excluded in text for excluded in exclude):  #not appending any line with excluded words
        clean_headings.append(text)


with open("headings.txt", "w") as file:   #write over the file using a for loop to conserve the order, one at the time
    for line in clean_headings:
        file.write(f"{line}\n")
