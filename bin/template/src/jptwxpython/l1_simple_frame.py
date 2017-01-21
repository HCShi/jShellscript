#!/usr/bin/python
# coding: utf-8
import wx
class Frame(wx.Frame):
    def __init__(self, parent, id, title, size):    # parent 一般为 NULL, id 一般为 -1
        wx.Frame.__init__(self, parent, id, title)  # 这里设置 title
        self.SetSize(size)  # 大小
        self.Center()       # 居中
        self.Show()         # 显示出来, 下面就是具体的逻辑了
        self.chatFrame = wx.TextCtrl(self, pos=(5, 5), size=(490, 290), style=wx.TE_MULTILINE | wx.TE_READONLY)
        self.message = wx.TextCtrl(self, pos=(5, 305), size=(390, 30))
        self.sendButton = wx.Button(self, label="Send", pos=(420, 305), size=(50, 30))
        self.sendButton.Bind(wx.EVT_BUTTON, self.send)  # 消息相应函数
    def send(self, event):
        msg = self.message.GetValue()
        self.message.Clear()
        self.chatFrame.AppendText(msg + '\n')
if __name__ == '__main__':
    app = wx.App()  # The wx.App object must be created first!
    Frame(None, -1, title='Chat', size=(500, 340))
    app.MainLoop()

