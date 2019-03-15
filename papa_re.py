# coding:utf-8
import json
import re

import requests


class PaPa(object):
    def __init__(self):
        self.url = "https://search.bilibili.com/all?keyword=%E5%82%85%E5%AE%A3&order=pubdate&duration=0&tids_1=0"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36"
        }
        self.file = open("fx.json", "w", encoding='utf-8')

    def get_data(self, url):
        response = requests.get(url, headers=self.headers)
        return response.content.decode()

    # 正则解析
    def parse_data(self, data):
        # '<a title="【敏若cp]  初见" href="//www.bilibili.com/video/av39195937?from=search&amp;seid=1935225583475212884" target="_blank" class="title">'
        result = re.findall('<a title=".*?" href=".*?" target="_blank" class="title">', data)
        # print(result)
        # print(result[0].replace('<a title="',''))

        data_list = []
        for i in result:
            i = i.replace('<a title="', '')
            i = i.replace('" target="_blank" class="title">', '')
            i = i.split('" href="//')
            temp = {}
            temp["title"] = i[0]
            a=re.findall('www.bilibili.com/video/av\d+', i[1])
            temp["link"] = a[0]
            temp["av号"]=a[0].replace('www.bilibili.com/video/', '')
            data_list.append(temp)
        page_data = re.findall('<li class="page-item active"><button class="pagination-btn num-btn">\d+</button></li>',data)
        next_page = re.search("\d+", page_data[0])
        next_page = int(next_page.group()) + 1

        return data_list, next_page

    def save_data(self, data_list):
        for data in data_list:
            str_data=json.dumps(data,ensure_ascii=False)+',\n'
            self.file.write(str_data)

    def run(self):
        # url
        # header
        next_url = self.url
        # 循环
        while True:
            # 发送请求获取响应
            data = self.get_data(next_url)
            # 正则解析
            data_list, next_page = self.parse_data(data)

            # 保存
            self.save_data(data_list)
            # 翻页，提取下一页链接
            # 根据是否有下一页判断是否退出循环
            if next_page <= 17:
                next_url = self.url+'&page=' + str(next_page)
                print(next_url)
            else:
                break


if __name__ == '__main__':
    papa = PaPa()
    papa.run()
