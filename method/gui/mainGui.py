import wx
from . import registration, search, operateCsvDb, graph, common
from method.services import cacheService
from method.utils import chms_logger

logger = chms_logger.set_operate_logger(__name__)


class Main(wx.Frame):
    def __init__(self, parent, id, title):
        frame_size = common.main_frame_size()
        wx.Frame.__init__(self, parent, id, title, size=frame_size)
        self.SetIcon(common.get_icon())
        MainPanel(self)
        self.Bind(wx.EVT_CLOSE, self.frame_close)
        self.Center()
        self.Show()

    def frame_close(self, event):
        self.Destroy()
        event.Skip()
        wx.Exit()


class MainPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        self.frame = parent
        self.__myinit()

    def __myinit(self):
        # 初期設定
        self.font = common.main_defalut_font_size()
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)

        # cacheテーブルの初期化を行う
        cacheService.init_cache()

        # ボタンを初期作成する
        button_size = common.main_button_size()
        self.button1 = wx.Button(self, wx.ID_ANY, u'登録', size=button_size)
        self.button2 = wx.Button(self, wx.ID_ANY, u'検索', size=button_size)
        self.button3 = wx.Button(self, wx.ID_ANY, u'CSV操作/DB初期化', size=button_size)

        # ボタンにフォントサイズを適応する
        self.button1.SetFont(self.font)
        self.button2.SetFont(self.font)
        self.button3.SetFont(self.font)

        # ボタンにアクションを追加する
        self.button1.Bind(wx.EVT_BUTTON, self.click_button1)
        self.button2.Bind(wx.EVT_BUTTON, self.click_button2)
        self.button3.Bind(wx.EVT_BUTTON, self.click_button3)

        # レイアウト設定
        self.layout = wx.GridBagSizer(0, 0)
        self.layout.Add(self.button1, (4, 0), (1, 1), flag=wx.GROW | wx.LEFT | wx.TOP, border=30)
        self.layout.Add(self.button2, (4, 1), (1, 1), flag=wx.GROW | wx.LEFT | wx.TOP, border=30)
        self.layout.Add(self.button3, (4, 2), (1, 1), flag=wx.GROW | wx.LEFT | wx.TOP, border=30)

        self.SetSizer(self.layout)

    def click_button1(self, event):
        """登録を呼び出す

        Parameters
        ----------
        event : クリックイベント
            クリックイベント

        """
        self.frame.Destroy()
        wx.Exit()
        registration.call_register()

    def click_button2(self, event):
        """登録を呼び出す

        Parameters
        ----------
        event : クリックイベント
            クリックイベント

        """
        self.frame.Destroy()
        wx.Exit()
        search.call_search()

    def click_button3(self, event):
        self.frame.Destroy()
        wx.Exit()
        operateCsvDb.call_csvOperation()

    def OnEraseBackground(self, evt):
        """
        バッググラウンドに画像を表示する
        """
        dc = evt.GetDC()

        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)
        dc.Clear()
        bmp = wx.Bitmap("method/image/chms.jpg")
        dc.DrawBitmap(bmp, 0, 0)


def call_mainGui():
    app = wx.App(False)
    logger.info("START mainGui")
    Main(None, wx.ID_ANY, title=u'CHMS')
    app.MainLoop()
