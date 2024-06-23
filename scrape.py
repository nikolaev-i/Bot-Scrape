import requests
from bs4 import BeautifulSoup as bs


def to_scrape():
  s = requests.get('https://www.bgjargon.com/word/random')

  soup = bs(s.content, 'html.parser')

  find_title = [title.get_text().strip() for title in soup.select('article h2')]

  find_meaning = [meaning.get_text().strip() for meaning in soup.find('div', class_='meaning')]

  find_example = [example.get_text().strip() for example in soup.find('div', class_='example')]
  title = find_title
  meaning= ",".join(find_meaning)
  example = ",".join(find_example)

  return(title[0], meaning.lstrip(',').rstrip(','), example.lstrip(',').rstrip(','))




to_scrape