"""Test the engines."""

from lyricscraper.lyrics import AZLyricsEngine, PyLyricsEngine, \
     MetroLyricsEngine
from lyricscraper.engines.base import NoLyricsFound


def test_azlyrics():
    """Test the AZ lyrics engine."""
    e = AZLyricsEngine()
    try:
        assert e.get_lyrics('Gordon Lightfoot', 'That Same Old Obsession')
    except NoLyricsFound:
        pass


def test_pylyrics():
    e = PyLyricsEngine()
    try:
        assert e.get_lyrics('Eminem', 'Mocking Bird')
    except NoLyricsFound:
        pass


def test_metro_lyrics():
    e = MetroLyricsEngine()
    try:
        assert e.get_lyrics(
            'LeAnn Rimes', 'You Made Me Find Myself'
        ) is not None
    except NoLyricsFound:
        pass
