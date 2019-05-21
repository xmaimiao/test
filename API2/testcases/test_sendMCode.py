import unittest
from API2.common.do_excel import DoExcel
from API2.common.do_sql import DoMysql
from API2.common.context import Context
from API2.common import contants
from ddt import ddt,data
from API2.common.context import replace
from API2.common.do_http import dohttp
from API2.common.mobliephone import Mobile
from API2.common.get_logs import loggings

logger = loggings(__name__)
@ddt
class TestsendMCode(unittest.TestCase):

    unit = unittest.TestCase()
    do_excel = DoExcel(contants.cases_dir, 'sendMCode')
    cases = do_excel.read_excel()

    @classmethod
    def setUpClass(cls):
        logger.info("准备测试前置！")
        cls.domysql = DoMysql()
        cls.mobile=Mobile()
        cls.mobile.user_mobile()

    @data(*cases)
    def testsendMCode(self,case):
        logger.info('開始測試：{}'.format(case.title))
        #處理data、sql中需要替換的值
        case.data = replace(case.data)
        logger.debug("反射到類中的手機號碼：{}".format(getattr(Context,'user_mobile')))
        #查詢數據庫，獲得傳入測試數據前的數據行數
        if case.sql is not None:
            case.sql = replace(case.sql)
            before_count = self.domysql.get_fetchone(eval(case.sql)['sql_count'])[0]
            logger.debug("數據庫現有數據量：{}".format(before_count))
        actual = dohttp(case.url,case.data,case.method)
        logger.info("用例測試的結果是：{}".format(actual))
        logger.info("Excel里期望的結果：{}".format(case.expect))
        logger.info("傳入的參數是：{}".format(case.data))

        try:
            self.unit.assertEqual(case.expect,actual)
            self.do_excel.write_excel(case.case_id+1,actual,'PASS')
        except Exception as e:
            self.do_excel.write_excel(case.case_id+1,actual,'FALSE')
            raise e

        #查詢數據庫，獲得傳入測試數據后的數據行數，校驗數據庫傳參成功
        if actual == 'ok'and case.sql is not None:
            try:
                after_count = self.domysql.get_fetchone(eval(case.sql)['sql_count'])[0]
                logger.info("數據庫最後數據量：{}".format(after_count))
                self.unit.assertEqual(1, after_count - before_count)
            except Exception as e:
                logger.error('報錯了,請檢查sql是否有誤！{}'.format(e))
                raise e
        logger.info('結束測試：{}'.format(case.title))


    @classmethod
    def tearDownClass(cls):
        logger.info("测试后置处理！")
        cls.domysql.close()

