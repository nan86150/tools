#!/usr/bin/env python
# encoding: utf-8
"""
对一道面试题的仿真试验，题目如下：
一楼到十楼的每层电梯门口都放着一颗钻石，钻石大小不一。你乘坐电梯从一楼到十楼，每层楼电梯门都会打开一次，只能拿一次钻石，问怎样才能拿到最
大的一颗？"""

import random

def main():
    N = 10
    totalScore = [0 for i in range(N)]

    for t in range(100000):
        diamond = [i for i in range(N)]
        random.shuffle(diamond)

        for i in range(N):
            totalScore[i] += getMax(diamond, i)

    print totalScore

def getMax(diamond, n):
    if n == 0:
        return diamond[0]
    m = max(diamond[:n])
    for i in range(n, len(diamond)):
        if diamond[i] > m:
            return diamond[i]
    else :
        return diamond[-1]


if __name__ == '__main__':
    main()

