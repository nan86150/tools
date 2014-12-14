#!/usr/bin/env python
# encoding: utf-8

from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy import log

from proxy.items import ProxyItem


class proxySpider(Spider):
    """爬取cn-proxy中的代理服务器ip和端口"""
    #log.start("log",loglevel='INFO')
    name = "proxy"
    allowed_domains = ["cn-proxy.com/"]
    start_urls = [
            "http://cn-proxy.com/"
    ]

    def parse(self, response):

        sel = Selector(response)
        sites = sel.xpath('//table[@class="sortable"]/tbody/tr')
        items = []

        for site in sites:
            item = ProxyItem()
            ip = site.xpath('td[1]/text()').extract()
            port = site.xpath('td[2]/text()').extract()

            item['ip'] = [t.encode('utf-8') for t in ip]
            item['port'] = [p.encode('utf-8') for p in port]
            items.append(item)

            #记录
            log.msg("Appending item...",level='INFO')


        log.msg("Append done.",level='INFO')
        return items
