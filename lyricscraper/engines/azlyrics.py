"""
An engine for azlyrics.com.
"""

from .base import BaseEngine, NoLyricsFound
from bs4 import BeautifulSoup
from urllib import request, error
from http.client import RemoteDisconnected

class AZLyricsEngine(BaseEngine):
 """An engine for getting lyrics from azlyrics.com."""
 name = 'AZ Lyrics'
 strip_chars = ' .,<>=-+_\\|\'"`/?'
 
 def get_lyrics(self, artist, title):
  for char in self.strip_chars:
   artist = artist.replace(char, '').lower()
   title = title.replace(char, '').lower()
  req = request.Request('http://azlyrics.com/lyrics/%s/%s.html' % (artist, title), headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})
  try:
   res = request.urlopen(req)
  except (error.URLError, RemoteDisconnected):
   raise NoLyricsFound()
  soup = BeautifulSoup(res.read())
  return soup.find('div', attrs = {'class': None, 'id': None}).text.strip()
