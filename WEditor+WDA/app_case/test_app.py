import wda
import unittest
from time import sleep


class TestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('\n程序开始')
        # tidevice -u 9dde9a1c9c3c01a1cbac0dd36339278a527f7235 wdaproxy -B com.facebook.WebDriverAgentRunnerForZhangXianSheng.xctrunner --port 8100
        # python3 -m weditor
        cls.c = wda.Client('http://localhost:8100')  # 8100为启动WDA设置的端口号

    @classmethod
    def tearDownClass(cls):
        print('程序结束')

    def test_1_login(self):
        """登录付哒系统"""
        self.c.xpath('//*[@label="付哒"]').click()
        self.c.xpath('//*[@label="请输入手机号"]').set_text('18662832373')
        self.c.xpath('//*[@label="完成"]').click()
        sleep(3)
        self.c.xpath('//*[@label=""]').click()
        sleep(3)
        self.c.xpath('//*[@label="登录/注册"]').click()
        sleep(3)
        self.c.xpath('//*[@label="pages/login/code/code[3]"]/StaticText[3]').set_text('1\n')
        self.c.tap(100, 200).set_text('1\n')  # 通过X、Y轴坐标定位元素
        self.c.xpath('//*[@label=""]').click()
        # self.c.xpath('//*[@label="pages/login/selectAccount/selectAccount[4]"]/Other[1]').click()


if __name__ == '__main__':
    unittest.main()
