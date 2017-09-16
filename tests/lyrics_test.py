from lyricscraper.lyrics import Lyrics, get_lyrics

artist = 'Eminem'
title = 'Mocking Bird'


def test_get_lyrics():
    l = get_lyrics(artist, title)
    assert isinstance(l, Lyrics)
    assert str(l) == '{} - {}'.format(artist, title)
