import sys
sys.path.append('./')
print(sys.path)

import unittest
import HTMLTestRunnerNew
from API2.common import contants

suit = unittest.TestSuite()
loader = unittest.TestLoader()
discover = unittest.defaultTestLoader.discover(contants.test_dir,'test_*.py')
with open(contants.reports_dir +'/report.html','wb') as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                              title="PYTHON API TEST RESULT",
                                              description="webserver",
                                              tester="mai")
    runner.run(discover)