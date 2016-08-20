import pytest
from lyricscraper import lyrics

artist = 'Eminem'
title = 'Mocking Bird'

def test_get_lyrics():
 l = lyrics.get_lyrics(artist, title)
 assert isinstance(l, lyrics.Lyrics)
 assert str(l) == '{} - {}'.format(artist, title)
