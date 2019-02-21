from main import re_json
from decimal import Decimal
import re
def use():
    '''过滤定向包，统计所有可用流量
    :param self:
    :return: 可用通用流量
    '''
    list_data = re_json.json_data()
    sum_over = 0
    for _ in list_data:
        if re.search(r'定向', _['包名']) != None:  # 去掉定向包
            list_data.remove(_)
    for _ in list_data:  # Decimal解决浮点数计算精度问题
        _over = Decimal(re.search(r'[0-9]{1,3}.[0-9]{1,2}', _['剩余']).group())
        sum_over = sum_over + _over  # 剩余可用
    # lot = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) # 时间
    return sum_over
