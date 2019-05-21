import logging
from API2.common import contants

def loggings(name):
    log = logging.getLogger(name)
    log.setLevel('INFO')
    fmt = logging.Formatter('%(asctime)s-%(levelname)s-%(name)s-日誌信息:%(message)s-[%(filename)s:%(lineno)d]')

    console_logger = logging.StreamHandler()
    console_logger.setFormatter(fmt)
    console_logger.setLevel('DEBUG')

    file_logger = logging.FileHandler(contants.logs_dir + '/case.log')
    file_logger.setFormatter(fmt)
    file_logger.setLevel('INFO')

    log.addHandler(console_logger)
    log.addHandler(file_logger)
    return log