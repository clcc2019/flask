# coding:utf-8

from main.yaohuo_list import get_html

def data_t():
    cont = get_html.YaoH().run()
    content = cont[0]
    title = cont[1]
    author = cont[2]
    data = []
    for _ in range(len(title)):
        data1_ = {}
        data1_['标题'] = title[_]
        data1_['作者'] = author[_].strip('/')
        data1_['内容'] = content[_]
        data.append(data1_)
    # json = json.dumps(data, ensure_ascii=False, indent=4, separators=(',', ': '))
    return data
