#!/usr/bin/python3
# coding:utf-8
# 某论坛帖子采集

import requests
from threading import Thread
from lxml import etree
from queue import Queue

class YaoH:
    def __init__(self):
        self.data_link = []
        self.data_title = []
        self.data_author = []
        self.content_text = []
        self.fj_href = []
    def get_html(self):
        url = 'https://yaohuo.me/bbs/book_list.aspx?gettotal=2019&action=new'
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36'}
        cookies = {'Cookie': 'GUID=d1739b2516300751; _ga=GA1.2.1113147474.1548405017; sidyaohuo=005C3324F55C3ED_DD4_04144_33660_71001-3-0-0-0-0; _gid=GA1.2.867504917.1549695333; ASP.NET_SessionId=ytlapr55m3dzzl55wnnr2h45; _gat_gtag_UA_88858350_1=1'}
        response = requests.get(url=url, headers=header, cookies=cookies)
        print(response.status_code)
        response.encoding = 'utf-8'
        html = etree.HTML(response.text)
        _title = html.xpath('//div[@class="line1"]/a[1]/text()|//div[@class="line2"]/a[1]/text()')
        _anthor = html.xpath('//div[@class="line1"]/text()[2]|//div[@class="line2"]/text()[2]|//div[@class="line1"]/font/text()|//div[@class="line2"]/font/text()')
        _date  = html.xpath('//div[@class="line1"]/span[@class="right"]/text()|//div[@class="line2"]/span[@class="right"]/text()')
        _href = html.xpath('//div[@class="line1"]/a[1][@href]/@href|//div[@class="line2"]/a[1][@href]/@href')
        for _ in range(len(_title)):
            title_i = _title[_]
            author = _anthor[_]
            link = 'https://yaohuo.me' + _href[_]
            self.data_link.append(link)
            self.data_author.append(author)
            self.data_title.append(title_i)
        # json_data = json.dumps(json_, ensure_ascii=False, indent=4, separators=(',', ': '))
        return self.data_link
    def run(self):
        '''多线程获取帖子内容
        :return:
        '''
        self.get_html()
        q = Queue()
        workers = []
        for url in self.data_link: q.put(url)
        for _ in range(15):
            workers.append(Thread(target=self.content, args=(q,)))
            q.put(0)
        for s in workers: s.start()
        for e in workers: e.join()
        return self.content_text, self.data_title, self.data_author,self.fj_href

    def content(self, url):
        '''获取帖子内容
        :return: content
        '''
        while True:
            url_ = url.get()
            if url_ ==0: break
            cookies = {'Cookie': 'GUID=d1739b2516300751; _ga=GA1.2.1113147474.1548405017; sidyaohuo=005C3324F55C3ED_DD4_04144_33660_71001-3-0-0-0-0; _gid=GA1.2.867504917.1549695333; ASP.NET_SessionId=ytlapr55m3dzzl55wnnr2h45'}
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36',
                'Referer': 'https://yaohuo.me/bbs/book_list.aspx?gettotal=2019&action=new',
            }
            response = requests.get(url=url_, headers=headers, cookies=cookies)
            html = etree.HTML(response.text)
            cont = html.xpath('//div[@class="bbscontent"]/text()')
            # fj = html.xpath('//div[@class="bbscontent"]/div/a/img[@src]/@src')
            self.content_text.append(''.join(cont))

if __name__ == '__main__':
    x = YaoH()
    x.run()