#!/usr/bin/env python
# encoding: utf-8
# @author: cc <chai_pengfei@163.com>

import wx
import re


class  MainFrame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Example', size=(400, 300))
        panel = wx.Panel(self, -1)

        self.contentLabel = wx.StaticText(panel, -1, r"内容")
        self.contentText = wx.TextCtrl(panel, -1, "", size=(175, 100), style=wx.TE_MULTILINE)
        self.contentText.SetInsertionPoint(0)

        self.expressionLabel = wx.StaticText(panel, -1, r"正则表达式")
        self.expressionText = wx.TextCtrl(panel, -1, "", size=(175, -1))

        self.resultLabel = wx.StaticText(panel, -1, r"结果")
        self.resultText = wx.TextCtrl(panel, -1, "", size=(175, 100), style=wx.TE_MULTILINE)
        self.resultText.SetInsertionPoint(0)

        self.button = wx.Button(panel, -1, r"解析", pos = (263, 106))
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.button)
        self.button.SetDefault()

        self.cb1 = wx.CheckBox(panel, -1, u"全局匹配", (260, 50), (110, 20))
        self.cb1.SetValue(True)
        self.cb2 = wx.CheckBox(panel, -1, u"忽略大小写", (260, 70), (110, 20))

        sizer = wx.FlexGridSizer(cols = 2, hgap = 6, vgap = 6)
        sizer.AddMany([self.contentLabel, self.contentText, self.expressionLabel, self.expressionText, self.resultLabel, self.resultText])
        panel.SetSizer(sizer)

    def OnClick(self, event):
        if self.cb2.GetValue():
            prog = re.compile(self.expressionText.GetString(0, -1), re.I)
        else:
            prog = re.compile(self.expressionText.GetString(0, -1))

        if self.cb1.GetValue():
            result = prog.findall(self.contentText.GetString(0, -1))
            rString = u'共检索到{0}条\n'.format(len(result))
            for r in result:
                rString += r+'\n'
        else:
            result = prog.search(self.contentText.GetString(0, -1))
            if result:
                rString = u'匹配结果:' + result.group()
            else:
                rString = u'没有匹配成功!'

        self.resultText.SetValue(rString)


if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = MainFrame()
    frame.Show()
    app.MainLoop()
