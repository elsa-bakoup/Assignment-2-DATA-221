#Question 7
from bs4 import BeautifulSoup
import requests

# adding headers to avoid being blocked by the website
headers = {
    "User-Agent": "Mozilla/5.0"
}

url = "https://en.wikipedia.org/wiki/Data_science"
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

title = soup.title.text      #finding the title

print(title)

content = soup.find('div', id='mw-content-text').find('div', class_='mw-parser-output')

first_paragraph = ''
for p in content.find_all('p'):
    text = p.get_text(" ",strip=True)
    if len(text) >= 50:  # skip empty paragraphs and kipping the first paragraph that's at least 50 characters
        first_paragraph = text
        break

print(first_paragraph)