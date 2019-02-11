import requests, time
from lxml import etree

def get_all():
    '''
    获取本月使用总量，总量需要在详细
    :param self:
    :return:
    '''
    headers = {
        'Referer': 'https://m.client.10010.com/mobileService/operationservice/queryOcsPackageFlowLeft.htm?menuId=000200020004&mobile_c_from=null&Accesstype=null&activiChannel=null',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; 16th Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.110 Mobile Safari/537.36; unicom{version:android@6.002,desmobile:17628371896};devicetype{deviceBrand:Meizu,deviceModel:16th}',
    }
    cookies = {
        'Cookie': 'MUT_S=android8.1.0; city=081|826; u_type=11; login_type=01; login_type=01; u_account=17628371896; c_version=android@6.002; d_deviceCode=866778030276749; random_login=0; cw_mutual=6ff66a046d4cb9a67af6f2af5f74c32174fc1e297e76168e140c26396069181bb5093f93a2493075bed75308d98158aa97b535ca6d125c1bf4d1aadc3d753b9f; c_mobile=17628371896; wo_family=0; u_areaCode=826; req_mobile=17628371896; req_serial=; req_wheel=ssss; ecs_acc=gn8fM47Y78NCM6d0r0USrYAwRWuu+5Fwjg8W7GCnUJBCD/fnC1hi4UENUkDW/pf2NOxhTkJaLRlVWWBHSyFX96pEXRWJ1o87yxHQCO9WJjlmAcLf+P40nNirCTeFq0w95RjauFmrqQHHaKZJ/lxDtqffQIRsM9UUQYb+/IKiMHw=; c_sfbm=4g_1; req_mobile=17628371896; req_serial=; req_wheel=ssss; mobileServicecb=d07ffd33ac27e8cc1776be6f409034ef; on_info=b7ebdc40ed1791ad2f844a90b2dc06c5; on_token=dc905cb7f093b99cb9cc335eb2c59cd4; mobileService=M0FpcRYKmGLYv6nVpJnpydZTkM1D5gNnQqyjcsHnp0bQm8t00Mvk!-2059739984; route=55f54410e8db5be50a8dbc21f26a6e18; quickNews=a8d1ba6ebe63380d1148174fe979297e; clientid=36|360; a_token=eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1NDk0Mzk5ODYsInRva2VuIjp7ImxvZ2luVXNlciI6IjE3NjI4MzcxODk2IiwicmFuZG9tU3RyIjoieWhlM2I4ZDAxNTQ4ODM1MTg2In0sImlhdCI6MTU0ODgzNTE4Nn0.db1gI__m-TyC562XYz2HJ2qL7Ug4SvMAdX7VSVt0TuJF2i3vkQA1qw-XziQJkKq7W8RoNlRNG8uKGjWFtx2fHA; c_id=df10e205697ed15809b9c96eb2d505370f601dcd6f9ea658ba928ed171523629; enc_acc=2ogxaBqvNhsV4IXgEOnLsk7UYRUiRpRBfa3If7cbVjqDGajNO8T/oMlUs5kQ99Qi+w8DE2tm12GQihXkMTowkZtQSCn9L/7lAlGJk7vdNdOEDcOAVh25fhZSvcyTsqFX/EEuDs2xVJ2gu51Gw4fTwkVU7TTDFYaQePhB4h2kgww=; ecs_acc=2ogxaBqvNhsV4IXgEOnLsk7UYRUiRpRBfa3If7cbVjqDGajNO8T/oMlUs5kQ99Qi+w8DE2tm12GQihXkMTowkZtQSCn9L/7lAlGJk7vdNdOEDcOAVh25fhZSvcyTsqFX/EEuDs2xVJ2gu51Gw4fTwkVU7TTDFYaQePhB4h2kgww=; t3_token=96aaf3ef29d525729b9383c5bb055d1f; invalid_at=359d12e1fa11317224f4641747768160dce280c9f98c5a3b2b3cb9ef2972c04c; third_token=eyJkYXRhIjoiMTMyYzJlNGFmOTFiOWU0ZTRmMmMyMDQwOWVkNWU5NDI1NjMxM2RiYzM5ZWEzNTBlODViOGNjZDIxYmNkYTg1N2ZiNzUzYWI4NmM4OGMwZmY5ZTI3Mzk0ZmVhY2JkYjMyMGNjMWRhMWEzMDYyMGIzOTM2MjgwNTQ2NjBkY2U4NTk3OTVkNWYxNGYxNTE0NTNkNmQ4NmQ1ZTllNzkyMjI1MCIsInZlcnNpb24iOiIwMCJ9; ecs_token=eyJkYXRhIjoiNWVjMzc1MzNjZDhiYmJhZTEwYWQ1NDMzYjIyNDJkODc1YThhMjBiZmJjYWIwZDNhOTI4NTNkYTcwODBmZGRlYjA0ZDg3YTRlNTZlNzEwMmI5YWVkYjY1MjZhNDNlNjIzMGExZDZhMDlkOWVjYWNiMDk1NmRjYzU2ZGRiN2UxZDU2NDE2MWNhZGIwOWQ0MmU0ZjA5OWFmOTFjYmI3YTcwNGVjYzhhODAyMWY4NmEzYzBhYjFmNmIxMTU2MDM2Mjc1IiwidmVyc2lvbiI6IjAwIn0=; jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtb2JpbGUiOiIxNzYyODM3MTg5NiIsInBybyI6IjA4MSIsImNpdHkiOiI4MjYiLCJpZCI6IjI2MTM3MjYxMmNmMjViZDI2YjcyZTg0N2I5OWJhY2FmIn0.EKLjjJYBMiN5SWATUKmoFYcXAHoljHo6owRtvOvr1ww; mobileService=12FccRZTJ1nPvZNVnyTYsYX8g00gjqL8xcJrt7Qsjph2wxdwj2Pq!-2059739984; c_sfbm=4g_1; ecs_acc=2ogxaBqvNhsV4IXgEOnLsk7UYRUiRpRBfa3If7cbVjqDGajNO8T/oMlUs5kQ99Qi+w8DE2tm12GQihXkMTowkZtQSCn9L/7lAlGJk7vdNdOEDcOAVh25fhZSvcyTsqFX/EEuDs2xVJ2gu51Gw4fTwkVU7TTDFYaQePhB4h2kgww='}
    url_total = 'https://m.client.10010.com/mobileService/query/queryNetWorkDetailContent.htm'
    data = {
        'menuId': '000200030004',
        'mobile_c_from': 'query',
        'tcyl_xd_back_flag': '1',
    }
    response = requests.post(url_total, data=data, cookies=cookies, headers=headers)
    if response.status_code == 200:
        response.encoding = 'utf-8'
        html_data = response.text
    else:
        print('请检查cookies')
    html = etree.HTML(html_data)
    num = html.xpath('//*[@id="llxd"]/div[3]/div[4]/div[1]/div/div[2]/p[@class="news"]/span/text()') # 总量
    total_data = num[0].strip('\r\n \t')
    return total_data
