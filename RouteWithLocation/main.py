#!/usr/bin/env python
# encoding: utf-8

import sys
import urllib2
import re


baseUrl = "http://freeapi.ipip.net/"


def getIpLocation(m):
    if m:
        ip = m.group(1)
        return ip + urllib2.urlopen(baseUrl + ip).read()
    else:
        return ''

if __name__ == '__main__':
    p = re.compile("((?:(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))\.){3}(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d))))")
    while True:
        content = sys.stdin.readline()
        if not content:
            break
        print p.sub(getIpLocation, content)[:-1]

