import random,string
from API2.common.context import Context,replace
from API2.common.do_http import dohttp
from API2.common.do_sql import DoMysql

class Mobile:
    def user_mobile(self):
        codelist= [random.choice(string.digits) for i in range(8)]
        mobile = ''.join(codelist)
        user_mobile = '182'+ mobile
        setattr(Context,'user_mobile',user_mobile)
        setattr(Context,'user_mobile_db_xx',user_mobile[-2:])
        setattr(Context,'user_mobile_info_x',user_mobile[-3])
        return user_mobile

    # def make_code(self,url, data, method, sql):
    def make_code(self,sql):
        sql = replace(sql)
        print("替換后的sql是:",sql)
        mobile_code = DoMysql().get_fetchone(sql)[0]
        setattr(Context, 'mobile_code', mobile_code)
        return mobile_code

if __name__ == '__main__':
    mobile = Mobile().make_code('select Fverify_code from sms_db_24.t_mvcode_info_9 where Fmobile_no =18258129924')
    print(mobile)