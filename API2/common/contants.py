import os

base_dir = os.path.dirname(os.path.dirname(__file__))
# print(base_dir)
cases_dir = os.path.join(base_dir,'data','webserver_cases2.xlsx')
global_dir = os.path.join(base_dir,'config','global.cfg')
dev_dir = os.path.join(base_dir,'config','dev.cfg')
uat_dir = os.path.join(base_dir,'config','uat.cfg')
test_dir = os.path.join(base_dir,'testcases')
reports_dir = os.path.join(base_dir,'reports')
logs_dir = os.path.join(base_dir,'logs')
