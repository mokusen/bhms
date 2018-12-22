import wx
from . import mainGui, common, mainGraphNote


class Graph(wx.Frame):
    def __init__(self, parent, id, title, year_accounting_list, title_accounting_list, all_data, test):
        current_display_size = wx.DisplaySize()
        use_display_size = ((current_display_size[0]-1200) / 2+625, (current_display_size[1]-600-40) / 2)
        wx.Frame.__init__(self, parent, id, title, size=(650, 600), pos=use_display_size)
        self.SetIcon(common.get_icon())
        MainPanel(self, year_accounting_list, title_accounting_list, all_data, test)
        self.Bind(wx.EVT_CLOSE, self.frame_close)
        self.Show()

    def frame_close(self, event):
        self.Destroy()


class MainPanel(wx.Panel):
    def __init__(self, parent, year_accounting_list, title_accounting_list, all_data, test):
        wx.Panel.__init__(self, parent=parent)
        self.frame = parent
        self.graphNote = mainGraphNote.GraphNotePanel(self, year_accounting_list, title_accounting_list, all_data, test)
        self.__myinit()

    def __myinit(self):
        # レイアウト設定
        layout = wx.BoxSizer(wx.VERTICAL)
        layout.Add(self.graphNote, flag=wx.EXPAND)
        self.SetSizer(layout)


def call_graph(year_accounting_list, title_accounting_list, all_data, test):
    Graph(None, wx.ID_ANY, title=u'CHMS | グラフ', year_accounting_list=year_accounting_list, title_accounting_list=title_accounting_list, all_data=all_data, test=test)
