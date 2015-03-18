#!/usr/bin/env python
# encoding: utf-8
# @author: cc <chai_pengfei@163.com>

import random

class MineException(Exception):
    pass

class MineMap():
    """ """
    def __init__(self, width=9, height=9, mineNum=10):
        self.WIDTH = width
        self.HEIGHT = height
        self.MAPSIZE = self.WIDTH * self.HEIGHT
        self.MINENUM = mineNum
        self.mineMap = self.__make_Map()
        self.remainMineNum = self.MINENUM
        self.clickedMap = [ 0 for i in range(self.MAPSIZE)]

    def left_click(self, ids):
        n = self.mineMap[ids]
        if n == -1:
            raise MineException
        elif n == 0:
            return self.__expand(ids)
        else:
            self.clickedMap[ids] = 1
            return n

    def right_click(self, ids):
        if self.clickedMap[ids] == 0:
            self.clickedMap[ids] = 2
            self.remainMineNum -= 1
            return 2
        elif self.clickedMap[ids] == 2:
            self.clickedMap[ids] = 0
            self.remainMineNum += 1
            return 0
        return None

    def bprint(self):
        for i, v in enumerate(self.mineMap):
            print " %s " %(v),
            if i%self.WIDTH == self.WIDTH-1:
                print ''

    def __expand(self, ids, result = None):
        if result == None:
            result = []
        result.append(ids)
        self.clickedMap[ids] = 1
        rd = self.__get_round(ids)
        for r in rd:
            if self.clickedMap[r] == 0 and self.mineMap[r] == 0:
                self.__expand(r, result)
        return result

    def __make_Map(self):
        minePos = random.sample([i for i in range(self.MAPSIZE)], self.MINENUM)
        mineMap = [0 for i in range(self.MAPSIZE)]

        for i in minePos:
            mineMap[i] = -1
            rd = self.__get_round(i)
            for j in rd:
                mineMap[j] += 1
        return mineMap

    def get_width(self):
        return self.WIDTH

    def get_height(self):
        return self.HEIGHT

    def get_mineNum(self):
        return self.MINENUM

    def get_remainMineNum(self):
        return self.remainMineNum

    def get_mineMap(self):
        return self.mineMap

    def __get_round(self, ids):
        rd = []
        hPos = ids / self.WIDTH
        vPos = ids % self.WIDTH
        if 0 < (vPos) < (self.WIDTH - 1):
            rd.append(ids - 1)                      # left
            rd.append(ids + 1)                      # right
            if 0 < (hPos) < (self.HEIGHT - 1):
                rd.append(ids - self.WIDTH )      # top
                rd.append(ids + self.WIDTH )      # bottom
                rd.append(ids - self.WIDTH - 1)   # left top
                rd.append(ids - self.WIDTH + 1)   # right top
                rd.append(ids + self.WIDTH - 1)   # left bottom
                rd.append(ids + self.WIDTH + 1)   # right bottom
            elif 0 == (hPos):
                rd.append(ids + self.WIDTH )      # bottom
                rd.append(ids + self.WIDTH - 1)   # left bottom
                rd.append(ids + self.WIDTH + 1)   # right bottom
            else:
                rd.append(ids - self.WIDTH )      # top
                rd.append(ids - self.WIDTH - 1)   # left top
                rd.append(ids - self.WIDTH + 1)   # right top
        elif (vPos) == 0:           # first row
            rd.append(ids + 1)                    # right
            if 0 < (hPos) < (self.HEIGHT- 1):
                rd.append(ids - self.WIDTH )      # top
                rd.append(ids + self.WIDTH )      # bottom
                rd.append(ids - self.WIDTH + 1)   # right top
                rd.append(ids + self.WIDTH + 1)   # right bottom
            elif 0 == (hPos):
                rd.append(ids + self.WIDTH )      # bottom
                rd.append(ids + self.WIDTH + 1)   # right bottom
            else:
                rd.append(ids - self.WIDTH )      # top
                rd.append(ids - self.WIDTH + 1)   # right top
        else:                       # last row
            rd.append(ids - 1)                    # left
            if 0 < (hPos) < (self.HEIGHT- 1):
                rd.append(ids - self.WIDTH )      # top
                rd.append(ids + self.WIDTH )      # bottom
                rd.append(ids - self.WIDTH - 1)   # left top
                rd.append(ids + self.WIDTH - 1)   # left bottom
            elif 0 == (hPos):
                rd.append(ids + self.WIDTH )      # bottom
                rd.append(ids + self.WIDTH - 1)   # left bottom
            else:
                rd.append(ids - self.WIDTH )      # top
                rd.append(ids - self.WIDTH - 1)   # left top
        return rd
    def gg(self, ids):
        return self.__get_round(ids)

if __name__ == '__main__':
    mm = MineMap(15, 9, 40)
    # print mm.get_width()
    # print mm.get_height()
    # print mm.get_mineNum()
    mm.bprint()
    print mm.left_click(3)
    mm.bprint()
    print mm.left_click(12)
    mm.bprint()
    print mm.left_click(33)
    mm.bprint()
    mm.gg(0)
    mm.gg(2)
    mm.gg(12)



