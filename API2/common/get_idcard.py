import random
from datetime import date
from datetime import timedelta
from API2.common.context import Context

def getidcard():

    city = {11: "北京", 12: "天津", 13: "河北", 14: "山西", 15: "内蒙古", 21: "辽宁", 22: "吉林", 23: "黑龙江 ", 31: "上海", 32: "江苏",
            33: "浙江", 34: "安徽", 35: "福建", 36: "江西", 37: "山东", 41: "河南", 42: "湖北 ", 43: "湖南", 44: "广东", 45: "广西",
            46: "海南", 50: "重庆", 51: "四川", 52: "贵州", 53: "云南", 54: "西藏 ", 61: "陕西", 62: "甘肃", 63: "青海", 64: "宁夏",
            65: "新疆", 71: "台湾", 81: "香港", 82: "澳门", 91: "国外 "}
    factor = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]  # 加權因子
    parity = [1, 0, 'X', 9, 8, 7, 6, 5, 4, 3, 2]  # 校驗位
    city_code=random.choice(list(city.keys()))
    eara_code=str(random.randint(0,40))
    if len(eara_code) == 2:
        id = str(city_code) + '000' + eara_code[-1]        #地區編碼
    else:
        id = str(city_code) + '00' + eara_code[-2:-1]
    id = id + str(random.randint(1930, int(date.today().strftime('%Y'))))  # 年份项
    da = date.today() + timedelta(days=random.randint(1, 366))  # 月份和日期项
    id = id + da.strftime('%m%d')
    id = id + str(random.randint(100, 300))  # ，顺序号简单处理

    count = 0
    for i in range(0,len(id)):
        count = count + int(factor[i])*int(id[i])
    mod = count%11
    id = id + str(parity[mod])  # 算出校验码
    setattr(Context,'id_card',id)


if __name__ == '__main__':
    c = getidcard()
    print(c)


