#!/usr/bin/env python
# encoding: utf-8
# @author: cc <chai_pengfei@163.com>

import wx
import random

class FindMineGame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, -1, r"扫雷", size=(400, 300))
        panel = wx.Panel(self, -1)

        self.MAPSIZE = 10
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
            self.buttons[bId].SetLabel(u"0")
        elif num == -1:
            self.buttons[bId].SetLabel(u"*")
        else:
            self.buttons[bId].SetLabel(str(num))

    def OnRClick(self, event):
        bId = event.GetId()
        if self.clickMap[bId] == 0:
            self.buttons[bId].SetLabel(u"▲")
            self.clickMap[bId] = 2      # 标记过雷

    def make_Map(self):
        minePos = random.sample([i for i in range(self.MINENUM)], 8)
        mineNum = [0 for i in range(self.MINENUM)]
        tmp = (-(self.MAPSIZE+1), -self.MAPSIZE, -(self.MAPSIZE-1),
               -1,                                              1,
               (self.MAPSIZE+1),   self.MAPSIZE,  (self.MAPSIZE-1))      # 周围8个点

        for i in minePos:
            for j in tmp:
                if 0<= (i+j) < self.MINENUM:
                    mineNum[i+j] += 1

        for i in minePos:
            mineNum[i] = -1

        return mineNum

class MineMap():

    def __init__(self):
        self.mapSize = 10
        self.mineNum = self.mapSize * self.mapSize
        self.mineMap = self.initMap()

    def initMap(self):
        minePos = random.sample([i for i in range(self.mineNum)], 8)
        mineNum = [0 for i in range(self.mineNum)]
        tmp = (-(self.mapsize+1), -self.mapsize, -(self.mapsize-1),
               -1,                                              1,
               (self.mapsize+1),   self.mapsize,  (self.mapsize-1))      # 周围8个点

        for i in minePos:
            for j in tmp:
                if 0<= (i+j) < self.mineNum:
                    mineNum[i+j] += 1

        for i in minePos:
            mineNum[i] = -1

        return mineNum


    def get_map_size(self):
        return self.mapSize



if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = FindMineGame()
    frame.Show()
    app.MainLoop()

