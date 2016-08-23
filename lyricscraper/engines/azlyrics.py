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
 def get_lyrics(self, title, artist):
  for char in self.strip_chars:
   artist = artist.replace(char, '').lower()
   title = title.replace(char, '').lower()
  try:
   res = request.urlopen('http://azlyrics.com/lyrics/%s/%s.html' % (title, artist))
   res = request.urlopen('http://azlyrics.com/lyrics/%s/%s.html' % (title, artist))
  except (error.URLError, RemoteDisconnected):
   raise NoLyricsFound()
  soup = BeautifulSoup(res.read())
  return soup.find('div', attrs = {'class': None, 'id': None}).text.strip()
