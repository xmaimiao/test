from suds.client import Client
from API2.common.config import config
from suds import WebFault
from API2.common.get_logs import loggings

logger = loggings(__name__)

def dohttp(url,data,method):
    # 处理传进来的url
    url_pre = config.get('api', 'pre_url')
    url = str(url_pre) + url

    try:
        client = Client(url)
        logger.info("傳入的url是：{}".format(url))
    except Exception as e:
        logger.error("检查url是否出错！{}".format(e))
        raise e
    # 處理傳進來的method
    try:
        #處理傳進來的data
        data = eval(data)
        # result = eval("Client({0}).service.{1}({2})".format(url,method,data))  #這樣寫不行= =
        result = eval('client.service.{1}({2})'.format(url,method,data))
        # result = client.service.__getattr__(method)(data)
        msg = str(result.retInfo)
    except WebFault as e:
        print(e.fault.faultstring)
        msg = str(e.fault.faultstring)

    return msg

# if __name__ == '__main__':
#     url ='/finance-user_info-war-1.0/ws/financeUserInfoFacade.ws?wsdl'
#     data = {'uid':'100011226','pay_pwd':'12345678','mobile':'18248797126','cre_id':'150008195002101005','user_name':'海明威','cardid':'18218813163566461145','bank_type':'1001','bank_name':'深圳南山區招商銀行分局','bank_area':'',bank_city'':''
#     print(dohttp(url,data,'bindBankCard'))


