"""
Get lyrics from metrolyrics.com.
"""

from requests import get
from bs4 import BeautifulSoup
from .base import BaseEngine, NoLyricsFound

class MetroLyricsEngine(BaseEngine):
 """Lyrics engine for metrolyrics.com."""
 name = 'Metro Lyrics'
 def get_lyrics(self, artist, title):
  response = get('http://www.metrolyrics.com/%s-lyrics-%s.html' % (title.lower().replace(' ', '-'), artist.lower().replace(' ', '-')))
  if response.ok:
   soup = BeautifulSoup(response.content)
   div = soup.find('div', id = 'lyrics-body-text')
   try:
    return div.text.strip()
   except AttributeError:
    raise NoLyricsFound()
  else:
   raise NoLyricsFound()
