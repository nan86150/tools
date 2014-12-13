#!/usr/bin/python

# 帮同学写着玩的
import urllib2
import time

def getIpAndPort():
	ip = []
	file = open('proxy.txt','r')
	for line in file:
		text = line.strip('\n')
		ip.append(text)
	return ip

def getPage():
	num = 1
	proxy_info = getIpAndPort()
	for i in range(5):
		for ip in proxy_info:
			print 'ip address is: ',
			print ip
			proxy_support = urllib2.ProxyHandler({"http" : ip})
			# We create an opener which uses this handler:
			opener = urllib2.build_opener(proxy_support)
			# Then we install this opener as the default opener for urllib2:
			urllib2.install_opener(opener)
			# Now we can send our HTTP request:
			try:
				response = urllib2.urlopen("http://vote.longhoo.net/index.php?m=lhvote&c=index&a=lhvote_d&catid=659&voteid=6965",  timeout=1)
				# response  = urllib2.urlopen("http://www.whatismyip.com.tw/", timeout=1)
			except KeyboardInterrupt:
				exit()
			except Exception:
				print 'Exception !!!'
				continue
			if response.getcode() == 200:
				page = response.read()
				if page == '1':
					print ' succeed: %d' % num
					num += 1
			# print response.read()
			# raw_input('please input any key to continue')
			# sleep 1s
			time.sleep(1)
	
if __name__ == '__main__':
	getPage()
		
