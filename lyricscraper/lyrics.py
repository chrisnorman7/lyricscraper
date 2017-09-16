"""
Lyric-related functions and classes.
"""

from attr import attrs, attrib
from .engines.base import NoLyricsFound
from .engines.azlyrics import AZLyricsEngine
from .engines.pylyrics import PyLyricsEngine
from .engines.metro_lyrics import MetroLyricsEngine


@attrs
class Lyrics(object):
    """A lyrics result."""

    artist = attrib()
    title = attrib()
    lyrics = attrib()
    engine = attrib()

    def __str__(self):
        return '{0.artist} - {0.title}'.format(self)


def get_lyrics(artist, title):
    for e in engines:
        try:
            return Lyrics(artist, title, e.get_lyrics(artist, title), e)
        except NoLyricsFound:
            pass  # Finally return None if nothing is found.


# Add all engines to the below list.

engines = [
    AZLyricsEngine(),
    PyLyricsEngine(),
    MetroLyricsEngine(),
]
