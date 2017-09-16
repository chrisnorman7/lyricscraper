"""
Get lyrics from metrolyrics.com.
"""

from requests import get
from requests.exceptions import RequestException, ConnectionError
from bs4 import BeautifulSoup
from .base import BaseEngine, NoLyricsFound


class MetroLyricsEngine(BaseEngine):
    """Lyrics engine for metrolyrics.com."""
    name = 'Metro Lyrics'

    def get_lyrics(self, artist, title):
        try:
            response = get(
                'http://www.metrolyrics.com/%s-lyrics-%s.html' % (
                    title.lower().replace(' ', '-'),
                    artist.lower().replace(' ', '-')
                )
            )
        except (RequestException, ConnectionError):
            raise NoLyricsFound()
        if not response.ok:
            raise NoLyricsFound()
        soup = BeautifulSoup(response.content, 'html.parser')
        div = soup.find('div', id='lyrics-body-text')
        try:
            return div.text.strip()
        except AttributeError:
            raise NoLyricsFound()
