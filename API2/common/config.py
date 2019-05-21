from configparser import ConfigParser
from API2.common import contants

class Config:
    cf = ConfigParser()
    cf.read(contants.global_dir, encoding='utf-8')
    if cf.getboolean('global','switch'):   #注意这里要getboolean,get只会取得str
        cf.read(contants.dev_dir, encoding='utf-8')
    else :
        cf.read(contants.uat_dir, encoding='utf-8')

    def get(self,session,option):
        return self.cf.get(session,option)

config = Config()