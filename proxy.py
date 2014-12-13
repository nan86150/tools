#!/usr/bin/python

#!/usr/bin/python
#-*- coding: UTF-8 -*-

# python 使用代理访问
import urllib2
import time
import re

def getIpAndPort():
	ip = []
	file = open('proxy.txt','r')
	for line in file:
		text = line.strip('\n')
		ip.append(text)
	return ip

def testProxy():
	num = 1
	proxy_info = getIpAndPort()
	pattern = re.compile(r'\d+\.\d+\.\d+\.\d+')
	for ip in proxy_info:
		print 'Proxy ip address is: ',
		print ip
		proxy_support = urllib2.ProxyHandler({"http" : ip})
		# We create an opener which uses this handler:
		opener = urllib2.build_opener(proxy_support)
		# Then we install this opener as the default opener for urllib2:
		urllib2.install_opener(opener)
		# Now we can send our HTTP request:
		try:
			response  = urllib2.urlopen("http://www.whatismyip.com.tw/", timeout=1)
		except KeyboardInterrupt:
			exit()
		except Exception:
			print 'Error '
			continue
		if response.getcode() == 200:
			page = response.read()
			match = pattern.search(page)
			if match: 
				print 'Check ip from whatismyip is',
				print match.group()
		time.sleep(1)
	
if __name__ == '__main__':
	testProxy()
		
