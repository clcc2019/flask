from main import html_data
from lxml import etree
import re, json
def json_data():
    '''
    格式化包名，大小，使用量，剩余量，返回json数据
    :return: json_data
    '''
    name = [] # 包名
    size = []
    use = []
    over = []
    list_data =[]
    get_data = html_data.get()
    # with open('query', 'r', encoding='utf-8') as f: # 测试时便重复请求页面，使用读文件方式
    # test_file = f.read()
    html = etree.HTML(get_data)
    packg_name = html.xpath('/html/body/div[2]/div/div[5]//div[@class="infopackage5"]/text()')  # 流量包名
    packg_size = html.xpath('/html/body/div[2]/div/div[5]//p[@class="TotleData"]/span[1]/text()')  # 包大小
    packg_use = html.xpath('/html/body/div[2]/div/div[5]//p[@class="TotleData"]/span[2]/text()')  # 已使用流量
    packg_over = html.xpath('/html/body/div[2]/div/div[5]//p[@class="lastData"]/span/text()|/html/body/div[2]/div/div[5]\
    //p[@class="lastData"]/span/span/text()')
    for _name in packg_name:
        if len(_name.strip('\r\n ')) == 0:
            continue
        else:
            name.append(_name.strip('\r\n  '))
    for _size in packg_size:
        size.append(_size.strip())
    for _use in packg_use:
        use.append(_use.strip())
    for _over in packg_over:  # 剩余量
        if len(_over.strip()) == 0:
            continue
        else:
            over.append(_over.strip())
    for _ in range(len(name)):  # 列表转json
        over_num = float(re.search(r'[0-9]{1,4}.[0-9]{2}', over[_]).group())  # 获取剩余量浮点数
        if over_num > 0:
            list_data.append({'包名': '{}'.format(name[_]),
                                   '大小': '{}'.format(size[_]),
                                   '已使用': '{}'.format(use[_]),
                                   '剩余': '{}'.format(over[_])})  # 导入list_data列表
        else:
            continue
    json_data = json.dumps(list_data, ensure_ascii=False, indent=4, separators=(',', ': '))
    # with open('data.json', 'w', encoding='utf-8') as f: # 测试将 json 写入文件
    #     f.write(json_data)  # 返回json文件
    return list_data
