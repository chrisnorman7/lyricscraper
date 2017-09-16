import wx
from lyricscraper.lyrics import get_lyrics


class LyricsFrame(wx.Frame):
    """A frame for viewing the lyrics."""

    def __init__(self):
        super(LyricsFrame, self).__init__(None, title='Lyricscraper')
        p = wx.Panel(self)
        s = wx.BoxSizer(wx.VERTICAL)
        s1 = wx.GridSizer(2, 0, 0)
        s1.Add(wx.StaticText(p, label='&Artist'))
        self.artist = wx.TextCtrl(p)
        s1.Add(self.artist)
        s1.Add(wx.StaticText(p, label='&Title'))
        self.title = wx.TextCtrl(p)
        s1.Add(self.title)
        s.Add(s1, 0, wx.GROW)
        self.btn = wx.Button(p, label='&Get Lyrics!')
        self.btn.Bind(wx.EVT_BUTTON, self.get_lyrics)
        self.btn.SetDefault()
        s.Add(self.btn, 0, wx.GROW)
        s.Add(wx.StaticText(p, label='&Lyrics'), 0, wx.GROW)
        self.lyrics = wx.TextCtrl(p, style=wx.TE_MULTILINE | wx.TE_READONLY)
        s.Add(self.lyrics, 1, wx.GROW)
        p.SetSizerAndFit(s)

    def do_error(self, message):
        """Error box."""
        return wx.MessageBox(message, 'Error', style=wx.ICON_EXCLAMATION)

    def get_lyrics(self, event):
        """The get lyrics button was pressed."""
        artist, title = self.artist.GetValue(), self.title.GetValue()
        if not artist:
            self.do_error('Artist cannot be blank.')
            self.artist.SetFocus()
        elif not title:
            self.do_error('Title cannot be blank.')
            self.title.SetFocus()
        else:
            lyrics = get_lyrics(artist, title)
            if lyrics is None:
                self.do_error('No lyrics found for %s - %s.' % (artist, title))
            else:
                self.lyrics.SetValue(
                    '%s - %s (%s)\n\n%s' % (
                        artist, title, lyrics.engine, lyrics.lyrics
                    )
                )
                self.lyrics.SetFocus()


if __name__ == '__main__':
    a = wx.App()
    f = LyricsFrame()
    f.Show(True)
    f.Maximize(True)
    a.MainLoop()
