"""
This class utilises the pylyrics module.
"""

from PyLyrics import PyLyrics
from .base import BaseEngine, NoLyricsFound

class PyLyricsEngine(BaseEngine):
 """An engine utilising pylyrics."""
 def get_lyrics(self, artist, title):
  try:
   return PyLyrics.getLyrics(artist, title)
  except ValueError:
   raise NoLyricsFound()
