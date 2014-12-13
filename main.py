
import urllib2


# proxy_handler = urllib2.ProxyHandler({'http': '103.247.158.178:8080'})
# proxy_auth_handler = urllib2.ProxyBasicAuthHandler()
# # proxy_auth_handler.add_password('realm', 'host', 'username', 'password')

# opener = urllib2.build_opener(proxy_handler, proxy_auth_handler)
# # This time, rather than install the OpenerDirector, we use it directly:
# page = opener.open('http://www.ip38.com/')
# print page.read()


# # The proxy address and port:
# proxy_info = { 'host' : '111.1.36.26',
               # 'port' : 83
             # }

# # We create a handler for the proxy
# proxy_support = urllib2.ProxyHandler({"http" : "http://%(host)s:%(port)d" % proxy_info})

# # We create an opener which uses this handler:
# opener = urllib2.build_opener(proxy_support)

# # Then we install this opener as the default opener for urllib2:
# urllib2.install_opener(opener)

# # Now we can send our HTTP request:
# htmlpage = urllib2.urlopen("http://www.whatismyip.com.tw/").read(200000)
# print htmlpage

# import httplib
# import socket
# class HTTPConnection_with_ip_binding(httplib.HTTPConnection):
    # def __init__(self, host, port=None, strict=None,
                # timeout=socket._GLOBAL_DEFAULT_TIMEOUT, bindip=None):
        # httplib.HTTPConnection.__init__(self,host,port,strict,timeout)
        # self.bindip = bindip
    # def connect(self):
        # msg = "getaddrinfo returns an empty list"
        # for res in socket.getaddrinfo(self.host, self.port, 0,
                                      # socket.SOCK_STREAM):
            # af, socktype, proto, canonname, sa = res
            # try:
                # self.sock = socket.socket(af, socktype, proto)
                # if self.debuglevel > 0:
                    # print "connect: (%s, %s)" % (self.host, self.port)
                # if self.bindip is not None:
                    # self.sock.bind((self.bindip,0))
                # self.sock.connect(sa)
            # except socket.error, msg:
                # if self.debuglevel > 0:
                    # print 'connect fail:', (self.host, self.port)
                # if self.sock:
                    # self.sock.close()
                # self.sock = None
                # continue
            # break
        # if not self.sock:
            # raise socket.error, msg
# def testip():
    # conn = HTTPConnection_with_ip_binding(host="darwin.bio.uci.edu",bindip="0.0.0.0")
    # conn.request("GET", "/cgi-bin/ipecho.pl")
    # r1 = conn.getresponse()
    # print r1.status, r1.reason
    # data1 = r1.read()
    # print data1
    # conn.close()
# if __name__=='__main__':
    # testip()
	
import time

for i in range(3):
	print 'hehho'
	time.sleep(1)