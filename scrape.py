import requests
from bs4 import BeautifulSoup as bs


def to_scrape():
  s = requests.get('https://www.bgjargon.com/word/random')

  soup = bs(s.content, 'html.parser')

  find_title = [title.get_text().strip() for title in soup.select('article h2')]

  find_meaning = [meaning.get_text().strip() for meaning in soup.select('article p')]

  return(find_title,find_meaning)






