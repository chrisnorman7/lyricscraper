from setuptools import setup

setup(
 name = 'lyricscraper',
 version = '0.0.5',
 description = 'A library for grabbing song lyrics from several sources.',
 url = 'http://github.com/chrisnorman7/lyricscraper.git',
 author = 'Chris Norman',
 author_email = 'chris.norman2@googlemail.com',
 license = 'MPL',
 packages = ['lyricscraper', 'lyricscraper.engines'],
 zip_safe = False,
 keywords = ['lyrics', 'song', 'music', 'web', 'scraping'],
 long_description_markdown_filename = 'README.md',
 setup_requires = ['setuptools-markdown'],
 install_requires = ['pylyrics', 'requests', 'beautifulsoup4'], 
)
