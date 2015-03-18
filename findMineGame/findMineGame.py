#!/usr/bin/env python
# encoding: utf-8
# @author: cc <chai_pengfei@163.com>

import wx
import random

class FindMineGame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, -1, r"扫雷", size=(600, 500))
        panel = wx.Panel(self, -1)

        self.MAPSIZE = 16
        self.MINENUM = self.MAPSIZE * self.MAPSIZE
        self.MINESIZE = 20

        self.mineMap = self.make_Map()
        self.clickMap = [0 for i in range(self.MINENUM)]

        minePos = [(j * self.MINESIZE, i * self.MINESIZE)
                for i in range(self.MAPSIZE) for j in range(self.MAPSIZE)]
        self.buttons = [wx.Button(
                        panel, i,
                        " ",
                        size = (self.MINESIZE, self.MINESIZE),
                        pos = pos) for i, pos in enumerate(minePos)]
        for b in self.buttons:
            b.Bind(wx.EVT_LEFT_UP, self.OnLClick)
            b.Bind(wx.EVT_RIGHT_UP, self.OnRClick)

    def OnLClick(self, event):
        bId = event.GetId()
        num = self.mineMap[bId]
        if num == 0:
            self.yidapian(bId)
            # self.buttons[bId].SetLabel(u"0")
            # TODO 增加同时打开一大片
        elif num == -1:
            self.buttons[bId].SetLabel(u"*")
            self.over()
        else:
            self.buttons[bId].SetLabel(str(num))

    def yidapian(self, bId):
        self.buttons[bId].SetLabel(u"0")
        self.clickMap[bId] = 1
        rd = self.get_round(bId)
        for ro in rd:
            if self.clickMap[ro] == 0 and self.mineMap[ro] == 0:
                self.yidapian(ro)


    def OnRClick(self, event):
        bId = event.GetId()
        if self.clickMap[bId] == 0:
            self.buttons[bId].SetLabel(u"▲")
            self.clickMap[bId] = 2      # 标记过雷

    def change_state(self, ids, flag):
        pass

    def get_round(self, ids):
        rd = []
        hPos = ids / self.MAPSIZE
        vPos = ids % self.MAPSIZE
        if 0 < (vPos) < (self.MAPSIZE - 1):
            rd.append(ids - 1)                      # left
            rd.append(ids + 1)                      # right
            if 0 < (hPos) < (self.MAPSIZE - 1):
                rd.append(ids - self.MAPSIZE )      # top
                rd.append(ids + self.MAPSIZE )      # bottom
                rd.append(ids - self.MAPSIZE - 1)   # left top
                rd.append(ids - self.MAPSIZE + 1)   # right top
                rd.append(ids + self.MAPSIZE - 1)   # left bottom
                rd.append(ids + self.MAPSIZE + 1)   # right bottom
            elif 0 == (hPos):
                rd.append(ids + self.MAPSIZE )      # bottom
                rd.append(ids + self.MAPSIZE - 1)   # left bottom
                rd.append(ids + self.MAPSIZE + 1)   # right bottom
            else:
                rd.append(ids - self.MAPSIZE )      # top
                rd.append(ids - self.MAPSIZE - 1)   # left top
                rd.append(ids - self.MAPSIZE + 1)   # right top
        elif (vPos) == 0:           # first row
            rd.append(ids + 1)                      # right
            if 0 < (hPos) < (self.MAPSIZE - 1):
                rd.append(ids - self.MAPSIZE )      # top
                rd.append(ids + self.MAPSIZE )      # bottom
                rd.append(ids - self.MAPSIZE + 1)   # right top
                rd.append(ids + self.MAPSIZE + 1)   # right bottom
            elif 0 == (hPos):
                rd.append(ids + self.MAPSIZE )      # bottom
                rd.append(ids + self.MAPSIZE + 1)   # right bottom
            else:
                rd.append(ids - self.MAPSIZE )      # top
                rd.append(ids - self.MAPSIZE + 1)   # right top
        else:                       # first row
            rd.append(ids - 1)                      # left
            if 0 < (hPos) < (self.MAPSIZE - 1):
                rd.append(ids - self.MAPSIZE )      # top
                rd.append(ids + self.MAPSIZE )      # bottom
                rd.append(ids - self.MAPSIZE - 1)   # left top
                rd.append(ids + self.MAPSIZE - 1)   # left bottom
            elif 0 == (hPos):
                rd.append(ids + self.MAPSIZE )      # bottom
                rd.append(ids + self.MAPSIZE - 1)   # left bottom
            else:
                rd.append(ids - self.MAPSIZE )      # top
                rd.append(ids - self.MAPSIZE - 1)   # left top
        return rd


    def make_Map(self):
        minePos = random.sample([i for i in range(self.MINENUM)], 40)
        mineNum = [0 for i in range(self.MINENUM)]

        for i in minePos:
            rd = self.get_round(i)
            for j in rd:
                mineNum[j] += 1

        for i in minePos:
            mineNum[i] = -1

        return mineNum

    def over(self):
        for key, bt in enumerate(self.buttons):
            bt.SetLabel(str(self.mineMap[key]))

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = FindMineGame()
    frame.Show()
    app.MainLoop()

