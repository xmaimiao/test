#參考，多個sql寫成字典的取值方式，實際上不建議這麼寫，太繁瑣
import unittest
from API2.common.get_username import UserName
from API2.common.do_excel import DoExcel
from API2.common import contants
from ddt import ddt,data
from API2.common.do_sql import DoMysql
from API2.common.context import replace,Context
from API2.common.do_http import dohttp
from API2.common import get_idcard
from API2.common.mobliephone import Mobile
import re

@ddt
class TestverifyUserAuth(unittest.TestCase):

    unit = unittest.TestCase()
    do_excel = DoExcel(contants.cases_dir, 'verifyUserAuth')
    cases = do_excel.read_excel()
    UserName().user_name()
    get_idcard.getidcard()

    @classmethod
    def setUpClass(cls):
        cls.domysql = DoMysql()
        cls.mobile=Mobile()
        cls.mobile.user_mobile()

    @data(*cases)
    def testverifyUserAuth(self,case):
        print(Context.__dict__)
        case.data = replace(case.data)
        print("傳入的參數data是:", case.data)

        # 查询实名认证前的数据库行数
        if case.sql is not None:
            if 'sql_count' in case.sql:
                before_count = self.domysql.get_fetchone(eval(case.sql)['sql_count'])[0]
                print("數據庫現有數據量：", before_count)
            elif 'sql_fuid' in case.sql:
                case.sql = replace(case.sql)
                print("傳入的case.sql：{}".format(eval(case.sql)['sql_fuid']))
                fuid = self.domysql.get_fetchone(eval(case.sql)['sql_fuid'])[0]
                print("得到的uid：",fuid)
                print("得到的uid類型：",type(fuid))
                setattr(Context,'fuid',fuid)                     # 'UserInfoFacadeImplService.UserInfoFacadeImplPort.verifiedUserAuth'

        actual = dohttp(case.url, case.data, case.method)

        try:
            self.unit.assertEqual(case.expect,actual)
            self.do_excel.write_excel(case.case_id+1,actual,'PASS')

        except Exception as e:
            self.do_excel.write_excel(case.case_id+1,actual,'FALSE')
            raise e

        if case.sql is not None :
            if 'sql_count' in eval(case.sql).keys():
                '''查询实名认证成功后数据库最大行数'''
                sql = eval(case.sql)
                print(sql)
                after_count = self.domysql.get_fetchone(eval(case.sql)['sql_count'])[0]
                print(after_count)
                self.unit.assertEqual(1, after_count - before_count)
            else:
                self.mobile.make_code(eval(case.sql)['sql_code'])
                print("反射類中的mobile_code是：", getattr(Context, 'mobile_code'))

    @classmethod
    def tearDownClass(cls):
        cls.domysql.close()