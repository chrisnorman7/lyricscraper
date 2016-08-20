"""
Lyric-related functions and classes.
"""

from .engines import base

class Lyrics(object):
 """A lyrics result."""
 def __init__(self, artist, title, lyrics, engine):
  """Create the result."""
  self.artist = artist
  self.title = title
  self.lyrics = lyrics
  self.engine = engine
 
 def __str__(self):
  return '{0.artist} - {0.title}'.format(self)

def get_lyrics(artist, title):
 for e in base.engines:
  try:
   return Lyrics(artist, title, e.get_lyrics(artist, title), e)
  except base.NoLyricsFound:
   pass # Finally return None if nothing is found.
