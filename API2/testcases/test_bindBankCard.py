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
from API2.common.get_logs import loggings

logger = loggings(__name__)

@ddt
class TestbindBankCard(unittest.TestCase):

    unit = unittest.TestCase()
    do_excel = DoExcel(contants.cases_dir, 'bindBankCard')
    cases = do_excel.read_excel()
    UserName().user_name()
    get_idcard.getidcard()

    @classmethod
    def setUpClass(cls):
        logger.info("准备测试前置！")
        cls.domysql = DoMysql()
        cls.mobile=Mobile()
        cls.mobile.user_mobile()

    @data(*cases)
    def testbindBankCard(self,case):
        logger.info('開始測試：{}'.format(case.title))
        case.data = replace(case.data)

        # 查询实名认证前的数据库行数
        if case.sql is not None:
            if 'count(*)' in case.sql:
                before_count = self.domysql.get_fetchone(case.sql)[0]
                logger.debug("數據庫現有數據量：{}".format(before_count))

        actual = dohttp(case.url, case.data, case.method)
        logger.info("用例測試的結果是：{}".format(actual))
        logger.info("Excel里期望的結果：{}".format(case.expect))
        logger.info("傳入的參數是：{}".format(case.data))

        try:
            self.unit.assertEqual(case.expect,actual)
            self.do_excel.write_excel(case.case_id+1,actual,'PASS')

        except Exception as e:
            self.do_excel.write_excel(case.case_id+1,actual,'FALSE')
            logger.error("出错了！{}".format(e))
            raise e

        try:
            if case.sql is not None :
                if 'count(*)' in case.sql:
                    #查询实名认证成功后数据库最大行数
                    after_count = self.domysql.get_fetchone(case.sql)[0]
                    logger.info("數據庫最後數據量：{}".format(after_count))
                    self.unit.assertEqual(1, after_count - before_count)
                elif 'Fverify_code' in case.sql:
                    self.mobile.make_code(case.sql)
                    logger.debug("反射類中的mobile_code是：{}".format(getattr(Context, 'mobile_code')))
                elif 'Fuid' in case.sql:
                    case.sql = replace(case.sql)
                    fuid = self.domysql.get_fetchone(case.sql)[0]
                    setattr(Context, 'fuid', fuid)
        except Exception as e:
            logger.error('報錯了,請檢查sql是否有誤！{}'.format(e))
            raise e
        logger.info('結束測試：{}'.format(case.title))

    @classmethod
    def tearDownClass(cls):
        logger.info("测试后置处理！")
        cls.domysql.close()