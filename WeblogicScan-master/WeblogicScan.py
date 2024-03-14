#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

'''
 ____       _     _     _ _   __  __           _
|  _ \ __ _| |__ | |__ (_) |_|  \/  | __ _ ___| | __
| |_) / _` | '_ \| '_ \| | __| |\/| |/ _` / __| |/ /
|  _ < (_| | |_) | |_) | | |_| |  | | (_| \__ \   <
|_| \_\__,_|_.__/|_.__/|_|\__|_|  |_|\__,_|___/_|\_\

'''
from config.config_banners import banner
from config.config_console import Weblogic_Console


def run():
    print(banner)
    print('Welcome To WeblogicScan !!!')
    Weblogic_Console()


if __name__ == '__main__':
    run()
    # 筑家工厂-python3.8 WeblogicScan.py -u 47.103.201.199 -p 80
    # 近视防控-python3.8 WeblogicScan.py -u 47.96.196.116 -p 443
    # Jenkins-python3.8 WeblogicScan.py -u 203.189.205.234 -p 8888
