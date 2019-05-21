from API2.common.config import config
from API2.common.do_sql import DoMysql
import configparser
import re


class Context:
    id_card = None    #注意这里的id_card要和用例里的参数相同
    user_mobile = None
    user_mobile_db_xx = None
    user_mobile_info_x = None
    mobile_code = None
    username = None
    fuid = None
    r_test_times = 1

def replace(data):
    p='#(.*?)#'
    while re.search(p,data):   #这里匹配不到返回None
        data_new =re.search(p,data).group(1)
        try:
            if 'sql' in data_new:
                sql = config.get('data',data_new)   #根據文件取配置文件裡面的值
                da = DoMysql().get_fetchone(sql)
                da = str(da[0])                  #從數據庫取出來的id是int
            else:
                da = config.get('data', data_new)
                # da=UserName().replace_name(data_new)
        except configparser.NoOptionError as e:
            if hasattr(Context,data_new):
                da= str(getattr(Context,data_new))
            else:
                print("找不到参数信息！")
                raise e
        data = re.sub(p, str(da), data, count=1)
    return data


if __name__ == '__main__':
    # r=replace("{'uid':'#sql_uid#','true_name':'#true_username#','cre_id':''}")
    r=replace("{'sql_count':'select count(*) from sms_db_#user_mobile_db_x#.t_mvcode_info_#user_mobile_info_xx#','sql_code':'select Fverify_code from sms_db_#user_mobile_db_x#.t_mvcode_info_#user_mobile_info_xx# where Fmobile_no =#user_mobile#'}")
    print(r)


