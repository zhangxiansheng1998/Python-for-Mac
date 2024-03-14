import logging


def Zhujia_Factory_log():
    # 日志器  创建日志器
    logger = logging.getLogger()

    # 设置级别
    logger.setLevel(logging.DEBUG)

    # 指定日志信息显示在哪里 处理器
    sh = logging.StreamHandler()

    # 把日志信息添加到控制台
    logger.addHandler(sh)

    fh = logging.FileHandler('Zhujia_Factory.log')
    logger.addHandler(fh)

    # 格式器
    formatter = logging.Formatter('%(asctime)s %(filename)s %(funcName)s %(levelno)s %(message)s')
    fh.setFormatter(formatter)

    return logger