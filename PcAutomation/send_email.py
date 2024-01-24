from PcAutomation.base.E_mail import *
from PcAutomation.config.conf import *
from test_cases.test_case_jsfk_01 import *


def runall():
    run()


def Email():
    NewReport = new_report(report_path)
    send_mail(NewReport)


if __name__ == '__main__':
    runall()
    Email()


