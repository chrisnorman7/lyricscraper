"""
An engine for azlyrics.com.
"""

from .base import BaseEngine, NoLyricsFound
from bs4 import BeautifulSoup
from requests import get
from requests.exceptions import RequestException, ConnectionError


class AZLyricsEngine(BaseEngine):
    """An engine for getting lyrics from azlyrics.com."""
    name = 'AZ Lyrics'
    strip_chars = ' .,<>=-+_\\|\'"`/?'

    def get_lyrics(self, artist, title):
        for char in self.strip_chars:
            artist = artist.replace(char, '').lower()
            title = title.replace(char, '').lower()
        url = 'http://azlyrics.com/lyrics/%s/%s.html' % (artist, title)
        try:
            res = get(url)
        except (RequestException, ConnectionError):
            raise NoLyricsFound()
        if not res.ok:
            raise NoLyricsFound()
        soup = BeautifulSoup(res.content, 'html.parser')
        return soup.find(
            'div', attrs={'class': None, 'id': None}).text.strip(
        )
