"""Test the engines."""

from lyricscraper.engines.base import *

def test_azlyrics():
 """Test the AZ lyrics engine."""
 e = AZLyricsEngine()
 assert e.get_lyrics('Gordon Lightfoot', 'That Same Old Obsession')

def test_pylyrics():
 e = PyLyricsEngine()
 assert e.get_lyrics('Eminem', 'Mocking Bird')

def test_metro_lyrics():
 e = MetroLyricsEngine()
 e.get_lyrics('LeAnn Rimes', 'You Made Me Find Myself')

