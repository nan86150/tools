#!/usr/bin/env python
# encoding: utf-8
# @author: cc <chai_pengfei@163.com>

import wx
import random
import time
import mineMap


class FindMineGame(wx.Frame):

    def __init__(self):
        """ """
        self.WIDTH = 19
        self.HEIGHT= 19
        self.MAPSIZE = self.WIDTH * self.HEIGHT
        self.MINENUM = 10
        self.mineMap = mineMap.MineMap(self.WIDTH, self.HEIGHT, self.MINENUM)

        wx.Frame.__init__(self, None, -1, r"扫雷", size=(400, 300))
        panel = wx.Panel(self, -1)
        self.MINESIZE = 20

        # time and last mine
        self.timeLbl = wx.StaticText(panel, -1, "Spend Time 000", size = (100, 20))
        self.lastLbl = wx.StaticText(panel, -1, "MineNum: %d" %(self.MINENUM), size = (90, 20))

        # mines
        self.mines = [wx.Button(panel, i, " ", size=(20, 20)) for i in range(self.MAPSIZE)]

        # btns
        self.resetBtn = wx.Button(panel, -1, "Reset")
        self.quitBtn = wx.Button(panel, -1, "Quit")

        mainSizer = wx.BoxSizer(wx.VERTICAL)

        # top
        topSizer = wx.BoxSizer(wx.HORIZONTAL)
        topSizer.Add((20, 20), 1)
        topSizer.Add(self.timeLbl)
        topSizer.Add((20, 20), 1)
        topSizer.Add(self.lastLbl)
        topSizer.Add((20, 20), 1)
        mainSizer.Add(topSizer, 0, wx.EXPAND | wx.BOTTOM, 10)
        mainSizer.Add(wx.StaticLine(panel), 0,
                wx.EXPAND | wx.TOP | wx.BOTTOM, 5)

        # mines
        minesSizer = wx.FlexGridSizer(cols = self.WIDTH)
        for wine in self.mines:
            # minesSizer.Add((20, 20), 1)
            minesSizer.Add(wine, 0, wx.EXPAND)
        mainSizer.Add(minesSizer, 0, wx.EXPAND | wx.BOTTOM, 10)
        mainSizer.Add(wx.StaticLine(panel), 0,
                wx.EXPAND | wx.TOP | wx.BOTTOM, 5)

        # bottom
        btnSizer = wx.BoxSizer(wx.HORIZONTAL)
        btnSizer.Add((20, 20), 1)
        btnSizer.Add(self.resetBtn)
        btnSizer.Add((20, 20), 1)
        btnSizer.Add(self.quitBtn)
        btnSizer.Add((20, 20), 1)
        mainSizer.Add(btnSizer, 0, wx.EXPAND | wx.BOTTOM, 10)

        panel.SetSizer(mainSizer)
        mainSizer.Fit(self)
        mainSizer.SetSizeHints(self)

        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.OnTimer, self.timer)
        for b in self.mines:
            b.Bind(wx.EVT_LEFT_UP, self.OnLClick)
            b.Bind(wx.EVT_RIGHT_UP, self.OnRClick)
        self.quitBtn.Bind(wx.EVT_BUTTON, self.Quit)

        self.isBegin = False
        self.isOver = False
        self.startTime = time.time()

    def OnLClick(self, event):
        if self.isBegin == False:
            self.Begin()
        eId = event.GetId()
        try:
            r = self.mineMap.left_click(eId)
            if isinstance(r, list):
                for i in r:
                    self.mines[i].SetLabel(u"0")
            else:
                self.mines[eId].SetLabel(str(r))
        except mineMap.MineException as e:
            self.Over()

    def OnRClick(self, event):
        if self.isBegin == False:
            self.Begin()
        eId = event.GetId()
        r = self.mineMap.right_click(eId)
        if r != None:
            if r == 2:
                self.mines[eId].SetLabel(u"▲")
            elif r == 0:
                self.mines[eId].SetLabel(u" ")
            self.lastLbl.SetLabel("MineNum: %2d " %(self.mineMap.get_remainMineNum()))

    def __initTimer__(self):
        self.startTime = time.time()
        self.timer.Start()
        self.timeLbl.SetLabel("Spend Time %3d s" %(0))
        self.lastLbl.SetLabel("MineNum: %2d " %(self.mineMap.get_mineNum()))

    def OnTimer(self, event):
        if self.isOver == False:
            self.timeLbl.SetLabel(
                    "Spend Time %3d s" %(time.time() - self.startTime))

    def Begin(self):
        self.isBegin = True
        self.__initTimer__()

    def Over(self):
        self.isOver = True
        self.timer.Stop()
        print 'over'

    def Reset(self, event):
        pass

    def Quit(self, event):
        exit()

    def make_Map(self):
        minePos = random.sample([i for i in range(self.MINENUM)], 8)
        mineNum = [0 for i in range(self.MINENUM)]

        for i in minePos:
            rd = self.get_round(i)
            for j in rd:
                mineNum[j] += 1

        for i in minePos:
            mineNum[i] = -1

        return mineNum

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


if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = FindMineGame()
    frame.Show()
    app.MainLoop()

