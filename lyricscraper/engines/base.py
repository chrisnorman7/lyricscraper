"""
This file contains the base class from which all Lyric Scraper engines should
be derived.

Any engines should subclass BaseEngine and override the get_lyrics function.

If No lyrics are found, NoLyricsFound should be raised, otherwise the lyrics
should be returned as a string.
"""


class BaseEngine(object):
    """The base lyrics engine."""
    name = 'Base Engine'

    def get_lyrics(self, artist, title):
        """Get the lyrics for artist - title."""
        raise NotImplementedError('You must override this function.')

    def __str__(self):
        """Pretty print."""
        return self.name


class NoLyricsFound(Exception):
    """No lyrics were found."""
