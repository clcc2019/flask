#! /user/bin/env python3
# coding=utf-8
import requests
import re
import sys
from lxml import etree
# import json
from decimal import Decimal
from threading import Thread

class NetQuery:
    def __init__(self):
        self.name = []
        self.size = []
        self.use = []
        self.over = []
        self.list_data = []
        self.data = {}

    def get(self):
        '''获取网页
        :return: 返回网页结构
        '''
        global get_data
        url = 'https://m.client.10010.com/mobileService/operationservice/queryOcsPackageFlowLeftContent.htm'
        cookies = {'Cookie': 'MUT_S=android8.1.0; city=081|826; u_type=11; login_type=01; login_type=01; u_account=17628371896; c_version=android@6.002; d_deviceCode=866778030276749; random_login=0; cw_mutual=6ff66a046d4cb9a67af6f2af5f74c32174fc1e297e76168e140c26396069181bb5093f93a2493075bed75308d98158aa97b535ca6d125c1bf4d1aadc3d753b9f; c_mobile=17628371896; wo_family=0; u_areaCode=826; req_mobile=17628371896; req_serial=; req_wheel=ssss; ecs_acc=gn8fM47Y78NCM6d0r0USrYAwRWuu+5Fwjg8W7GCnUJBCD/fnC1hi4UENUkDW/pf2NOxhTkJaLRlVWWBHSyFX96pEXRWJ1o87yxHQCO9WJjlmAcLf+P40nNirCTeFq0w95RjauFmrqQHHaKZJ/lxDtqffQIRsM9UUQYb+/IKiMHw=; c_sfbm=4g_1; req_mobile=17628371896; req_serial=; req_wheel=ssss; on_info=b7ebdc40ed1791ad2f844a90b2dc06c5; MyAccount=0JGDcThWyjpTyJlyQTKC6ZGxGQDy7nXYpppvrYsgQGPcGygkMkj6!-2141796276; mallcity=36|360; gipgeo=36|360; SHOP_PROV_CITY=; MUT_V=android%406.002; UID=2qSXNXbOKOLdXV69u5Geh7GIO5KMGTb9; CaptchaCode=cdm9lpe7twz5GYgYh0awYlzAY4jnN1GpgNNKo4YX0Hs=; WT_FPC=id=2a9b6aa45a12c2a94cf1548952633191:lv=1548952633207:ss=1548952633191; route=518b31842820372a15efdab8ac61bee1; redpacketsplit=p9nZcTkGDX8L2yXd1X42nsDmdXw19ch52vJp3VTYTLpnH0NyYv9D!1815218768; on_token=dc6a39d2c38fd2760e18a740d96ad30c; route=55f54410e8db5be50a8dbc21f26a6e18; quickNews=7a6aa5187ddccd5126a41fdceeb54e1e; clientid=13|130; JSESSIONID=P3GKcTyFG7w5tfPd33yWH687wdQ3VgmGc6p8XvLLkNTLYttcxWsh!362477239; myPrizeForActivity=xB9fcTyLzyMJyn7sQCd1ynyhG1yfrhkbwnwBG10LlwqgchQJrqzT!-1192071580; a_token=eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1NDk1ODAxMTgsInRva2VuIjp7ImxvZ2luVXNlciI6IjE3NjI4MzcxODk2IiwicmFuZG9tU3RyIjoieWhmNDAxYWIxNTQ4OTc1MzE4In0sImlhdCI6MTU0ODk3NTMxOH0.jMd7VJhupoOAu0dUS05-F_8BplI5hXRROGdq8xUwE6iBn0NOkvKGIH6nI0kndTqKpMvg5pFOT_DpqHCyjPFTxQ; c_id=df10e205697ed15809b9c96eb2d505378d4f0b0ae24f88c55689c18835933210; enc_acc=vBoENHJR8P2z6eG3i+8+DCj/H6IrHxF2xBAmq+GDbTKJzMfE5b/thNE+JTsmqvMNficbIYIp7TbvuNGpE8FZNJjPqyZZRJlrVccX5Lza99CixiDnH/xiqEaWRh/7jhuphGAxw45PTp+LsDWZWFQFo6fKvfDubeZZJv+qflt1wVw=; ecs_acc=vBoENHJR8P2z6eG3i+8+DCj/H6IrHxF2xBAmq+GDbTKJzMfE5b/thNE+JTsmqvMNficbIYIp7TbvuNGpE8FZNJjPqyZZRJlrVccX5Lza99CixiDnH/xiqEaWRh/7jhuphGAxw45PTp+LsDWZWFQFo6fKvfDubeZZJv+qflt1wVw=; t3_token=c708d3c94d7ad6f0ac9fe56b6743fde9; invalid_at=73b72c1e01ddbed157aa69396b902e9e0ac6981356072a0ebae98c478c254e96; third_token=eyJkYXRhIjoiMTMyYzJlNGFmOTFiOWU0ZTRmMmMyMDQwOWVkNWU5NDI3NGJkMTFjZTQ4OWRhZjhmMmNiNGIzMTdmMjY5M2ZmZjY5NWY2Yzc5OTBhODkzMDQ2MTc0MDNhODM3ZjA5MWE0YWI4MzMzOTIyZmIxZTI0YThjN2JkZmRlMThmMzI1YjQ5ZTBkMTZmZGFhZTg5OGIxMDFkODVmYzAyODBjODc0NCIsInZlcnNpb24iOiIwMCJ9; ecs_token=eyJkYXRhIjoiNWVjMzc1MzNjZDhiYmJhZTEwYWQ1NDMzYjIyNDJkODc1YThhMjBiZmJjYWIwZDNhOTI4NTNkYTcwODBmZGRlYjJjMmRkNzhiMmY5ZjQyNTY0N2I1YzFiMDBiZGI4YjYzMDBiMmJlY2Y2OGVkMmU3YjU5OGYyNzA1ZjRlNjc0MzYyMjY4ZWRhYjc5ZjUxYzY0MmExYzQ3NmM4MTdhYTkwNDBlOGVhNzc2MmQzODVjMGU5NTk2ODZjZmMwMTc5NTAzIiwidmVyc2lvbiI6IjAwIn0=; jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtb2JpbGUiOiIxNzYyODM3MTg5NiIsInBybyI6IjA4MSIsImNpdHkiOiI4MjYiLCJpZCI6ImEzODc1MzQzNDYwYjc4YzAwYTdmYmFlMmE5ODFjOGQxIn0.c8J1lda-VigWtmoqU2km7IRDfAndwwZ65DVZ_k48Gn8; c_sfbm=4g_1; ecs_acc=vBoENHJR8P2z6eG3i+8+DCj/H6IrHxF2xBAmq+GDbTKJzMfE5b/thNE+JTsmqvMNficbIYIp7TbvuNGpE8FZNJjPqyZZRJlrVccX5Lza99CixiDnH/xiqEaWRh/7jhuphGAxw45PTp+LsDWZWFQFo6fKvfDubeZZJv+qflt1wVw=; mobileServicecb=46c90e76262ec5f1a4fddec93a66b6e9; mobileService=CVQLcTTTNF9p1nJ1J3YrntT25WHhDGJcY3XgHwPTgG63QrJ01JTQ!-1168092354; mobileService=Kyv4cTTWjJc9yGhcJCykpfqTnHfvDvKsZ5G2Ny3HLnLySVncnN71!-1168092354'}
        headers = {
            'Referer': 'https://m.client.10010.com/mobileService/operationservice/queryOcsPackageFlowLeft.htm?menuId=000200020004&mobile_c_from=null&Accesstype=null&activiChannel=null',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; 16th Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.110 Mobile Safari/537.36; unicom{version:android@6.002,desmobile:17628371896};devicetype{deviceBrand:Meizu,deviceModel:16th}',
        }
        data = {
            'menuId': '000200020004',
            'mobile_c_from': 'null',
            'Accesstype': 'null',
            'activiChannel': 'null',
        }
        response = requests.post(
            url=url,
            cookies=cookies,
            headers=headers,
            data=data)
        if response.status_code == 200:
            get_data = response.text
            file_name = './templates/hs.html'
            with open(file_name, 'w', encoding='utf-8') as f:
                f.write(response.text)
        else:
            print('获取网页：请求过期')
        size = sys.getsizeof(response.content)
        if size <= 4100:
            str_ = "联通又炸了"
            self.data['use'] = str_
            return self.data
            # return self.data.append('联通又炸了')
        else:
            self.count_over()

    def count_over(self):  # 过滤定向包，统计所有剩余
        self.listdata()
        sum_over = 0
        for i in self.list_data:
            if re.search(r'定向', i['包名']) is not None:  # 去掉定向包
                self.list_data.remove(i)
        for _ in self.list_data:  # Decimal解决浮点数计算精度问题
            _over = Decimal(
                re.search(
                    r'[0-9]{1,3}.[0-9]{1,2}',
                    _['剩余']).group())
            sum_over = sum_over + _over  # 剩余可用
            # print(type(sum_over))
        self.data['use'] = sum_over

    def listdata(self):
        self.lx_data()
        for _ in range(len(self.name)):  # 列表转json格式
            over_num = float(
                re.search(
                    r'[0-9]{1,4}.[0-9]{2}',
                    self.over[_]).group())  # 获取剩余量浮点数
            if over_num > 0:  # 过滤无用包
                self.list_data.append(
                    {
                        '包名': '{}'.format(
                            self.name[_]), '大小': '{}'.format(
                            self.size[_]), '已使用': '{}'.format(
                            self.use[_]), '剩余': '{}'.format(
                            self.over[_])})  # 导入list_data列表
            else:
                continue
        return self.list_data

    def lx_data(self):  # 格式化包名，大小，使用量，剩余量，返回json数据
        html = etree.HTML(get_data)
        packg_name = html.xpath(
            '/html/body/div[2]/div/div[5]//div[@class="infopackage5"]/text()')  # 流量包名
        packg_size = html.xpath(
            '/html/body/div[2]/div/div[5]//p[@class="TotleData"]/span[1]/text()')  # 包总量
        packg_use = html.xpath(
            '/html/body/div[2]/div/div[5]//p[@class="TotleData"]/span[2]/text()')  # 已使用
        packg_over = html.xpath(
            '/html/body/div[2]/div/div[5]//p[@class="lastData"]/span/text()|/html/body/div[2]/div/div[5]//p[@class="lastData"]/span/span/text()')
        for _ in packg_name:  # 包名
            if len(_.strip('\r\n ')) == 0:
                continue
            else:
                self.name.append(_.strip('\r\n  '))
        for _ in packg_size:
            self.size.append(_.strip())
        for _ in packg_use:
            self.use.append(_.strip())
        for _ in packg_over:
            if len(_.strip()) == 0:
                continue
            else:
                self.over.append(_.strip())

    def get_all(self):  # 本月使用总量
        '''获取使用总量
        :return: 返回总量
        '''
        headers = {
            'Referer': 'https://m.client.10010.com/mobileService/operationservice/queryOcsPackageFlowLeft.htm?menuId=000200020004&mobile_c_from=null&Accesstype=null&activiChannel=null',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; 16th Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.110 Mobile Safari/537.36; unicom{version:android@6.002,desmobile:17628371896};devicetype{deviceBrand:Meizu,deviceModel:16th}',
        }
        cookies2 = {'Cookie': 'MUT_S=android8.1.0; city=081|826; u_type=11; login_type=01; login_type=01; u_account=17628371896; c_version=android@6.002; d_deviceCode=866778030276749; random_login=0; cw_mutual=6ff66a046d4cb9a67af6f2af5f74c32174fc1e297e76168e140c26396069181bb5093f93a2493075bed75308d98158aa97b535ca6d125c1bf4d1aadc3d753b9f; c_mobile=17628371896; wo_family=0; u_areaCode=826; req_mobile=17628371896; req_serial=; req_wheel=ssss; ecs_acc=gn8fM47Y78NCM6d0r0USrYAwRWuu+5Fwjg8W7GCnUJBCD/fnC1hi4UENUkDW/pf2NOxhTkJaLRlVWWBHSyFX96pEXRWJ1o87yxHQCO9WJjlmAcLf+P40nNirCTeFq0w95RjauFmrqQHHaKZJ/lxDtqffQIRsM9UUQYb+/IKiMHw=; c_sfbm=4g_1; req_mobile=17628371896; req_serial=; req_wheel=ssss; mobileServicecb=d07ffd33ac27e8cc1776be6f409034ef; on_info=b7ebdc40ed1791ad2f844a90b2dc06c5; on_token=dc905cb7f093b99cb9cc335eb2c59cd4; mobileService=M0FpcRYKmGLYv6nVpJnpydZTkM1D5gNnQqyjcsHnp0bQm8t00Mvk!-2059739984; route=55f54410e8db5be50a8dbc21f26a6e18; quickNews=a8d1ba6ebe63380d1148174fe979297e; clientid=36|360; a_token=eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1NDk0Mzk5ODYsInRva2VuIjp7ImxvZ2luVXNlciI6IjE3NjI4MzcxODk2IiwicmFuZG9tU3RyIjoieWhlM2I4ZDAxNTQ4ODM1MTg2In0sImlhdCI6MTU0ODgzNTE4Nn0.db1gI__m-TyC562XYz2HJ2qL7Ug4SvMAdX7VSVt0TuJF2i3vkQA1qw-XziQJkKq7W8RoNlRNG8uKGjWFtx2fHA; c_id=df10e205697ed15809b9c96eb2d505370f601dcd6f9ea658ba928ed171523629; enc_acc=2ogxaBqvNhsV4IXgEOnLsk7UYRUiRpRBfa3If7cbVjqDGajNO8T/oMlUs5kQ99Qi+w8DE2tm12GQihXkMTowkZtQSCn9L/7lAlGJk7vdNdOEDcOAVh25fhZSvcyTsqFX/EEuDs2xVJ2gu51Gw4fTwkVU7TTDFYaQePhB4h2kgww=; ecs_acc=2ogxaBqvNhsV4IXgEOnLsk7UYRUiRpRBfa3If7cbVjqDGajNO8T/oMlUs5kQ99Qi+w8DE2tm12GQihXkMTowkZtQSCn9L/7lAlGJk7vdNdOEDcOAVh25fhZSvcyTsqFX/EEuDs2xVJ2gu51Gw4fTwkVU7TTDFYaQePhB4h2kgww=; t3_token=96aaf3ef29d525729b9383c5bb055d1f; invalid_at=359d12e1fa11317224f4641747768160dce280c9f98c5a3b2b3cb9ef2972c04c; third_token=eyJkYXRhIjoiMTMyYzJlNGFmOTFiOWU0ZTRmMmMyMDQwOWVkNWU5NDI1NjMxM2RiYzM5ZWEzNTBlODViOGNjZDIxYmNkYTg1N2ZiNzUzYWI4NmM4OGMwZmY5ZTI3Mzk0ZmVhY2JkYjMyMGNjMWRhMWEzMDYyMGIzOTM2MjgwNTQ2NjBkY2U4NTk3OTVkNWYxNGYxNTE0NTNkNmQ4NmQ1ZTllNzkyMjI1MCIsInZlcnNpb24iOiIwMCJ9; ecs_token=eyJkYXRhIjoiNWVjMzc1MzNjZDhiYmJhZTEwYWQ1NDMzYjIyNDJkODc1YThhMjBiZmJjYWIwZDNhOTI4NTNkYTcwODBmZGRlYjA0ZDg3YTRlNTZlNzEwMmI5YWVkYjY1MjZhNDNlNjIzMGExZDZhMDlkOWVjYWNiMDk1NmRjYzU2ZGRiN2UxZDU2NDE2MWNhZGIwOWQ0MmU0ZjA5OWFmOTFjYmI3YTcwNGVjYzhhODAyMWY4NmEzYzBhYjFmNmIxMTU2MDM2Mjc1IiwidmVyc2lvbiI6IjAwIn0=; jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtb2JpbGUiOiIxNzYyODM3MTg5NiIsInBybyI6IjA4MSIsImNpdHkiOiI4MjYiLCJpZCI6IjI2MTM3MjYxMmNmMjViZDI2YjcyZTg0N2I5OWJhY2FmIn0.EKLjjJYBMiN5SWATUKmoFYcXAHoljHo6owRtvOvr1ww; mobileService=12FccRZTJ1nPvZNVnyTYsYX8g00gjqL8xcJrt7Qsjph2wxdwj2Pq!-2059739984; c_sfbm=4g_1; ecs_acc=2ogxaBqvNhsV4IXgEOnLsk7UYRUiRpRBfa3If7cbVjqDGajNO8T/oMlUs5kQ99Qi+w8DE2tm12GQihXkMTowkZtQSCn9L/7lAlGJk7vdNdOEDcOAVh25fhZSvcyTsqFX/EEuDs2xVJ2gu51Gw4fTwkVU7TTDFYaQePhB4h2kgww='}
        url2 = 'https://m.client.10010.com/mobileService/query/queryNetWorkDetailContent.htm'
        data2 = {
            'menuId': '000200030004',
            'mobile_c_from': 'query',
            'tcyl_xd_back_flag': '1',
        }
        s = requests.post(
            url2,
            data=data2,
            cookies=cookies2,
            headers=headers)  # 总使用量
        if s.status_code == 200:
            get_html = s.text
        else:
            print('获取总量：请检查cookies')
        html = etree.HTML(get_html)
        num = html.xpath(
            '//*[@id="llxd"]/div[3]/div[4]/div[1]/div/div[2]/p[@class="news"]/span/text()')
        all_data = num[0].strip('\r\n \t')
        self.data['over'] = all_data
    # def Json_data(self):
    #     json_data = json.dumps(self.list_data, ensure_ascii=False, indent=4, separators=(',', ': '))
    #     return json_data  # 返回json数据

    def run(self):
        '''由于总量跟使用量页面时分开的，需要两个请求，所以开两个线程处理
        :return: 返回数据列表
        '''
        t1 = Thread(target=self.get())
        t2 = Thread(target=self.get_all())
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        return self.data
if __name__ == '__main__':
    x = NetQuery()
    x.run()
