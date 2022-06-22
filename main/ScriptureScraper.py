import requests
from bs4 import BeautifulSoup

# Request a response object from lds.org and obtain the page content
page = requests.get("https://www.churchofjesuschrist.org/study/scriptures/ot/2-sam/1?lang=eng")
soup = BeautifulSoup(page.content, 'html.parser')

# Grab the scripture content from the webpage
scripture = soup.find('div', class_="body")
verses = scripture.find_all(class_="verse")
first = verses[0]

if __name__ == '__main__':
    print(first.prettify())
