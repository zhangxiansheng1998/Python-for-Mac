"""
E_mail.py 配置收发邮件
"""
import os
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import time
from datetime import datetime
from Zhujia_Factory.base.generate_email_template import *
from Zhujia_Factory.runall.run_all import *

now = time.strftime("%Y-%m-%d~%H-%M-%S")  # 获取当前时间
reportname = now + ".html"
today = datetime.today()  # 获取当前日期
formatted_date = today.strftime("%Y-%m-%d")  # 格式化日期为字符串，例如："2024-01-12"


def send_mail(report):
    f = open(report, "rb")
    mail_body = f.read()
    f.close()

    username = "1120620374@qq.com"  # 发件箱用户名
    password = "legbyrctuueyhggb"  # 发件箱密码（授权码）
    sender = "1120620374@qq.com"  # 发件人邮箱
    receivers = ["m15180381485@163.com", '596137586@qq.com']  # 收件人邮箱

    msg = MIMEMultipart(_subtype='html', _charset='utf-8')
    email_att = MIMEApplication(open('{B}/{C}'.format(B=report_path, C=reportname), 'rb').read())
    email_att.add_header('Content-Disposition', 'attachment', filename=reportname)
    msg.attach(email_att)

    # 使用测试报告的结果生成一个邮件模板，可以查看测试用例的执行结果
    NewReport = new_report(report_path)
    data = extract_test_summary_with_regex(NewReport)
    html_content = generate_html(data)

    # 创建 MIMEText 对象并将 HTML 内容添加到邮件中
    html_part = MIMEText(html_content, "html")
    msg.attach(html_part)

    # 邮件对象
    msg["Subject"] = "WEB自动化测试报告"
    msg['From'] = '1120620374@qq.com'  # 发件人
    msg['To'] = "m15180381485@163.com,596137586@qq.com"  # 收件人,使用逗号隔开输入即可
    msg["date"] = time.strftime("%a,%d %b %Y %H:%M:%S %z")
    # 发送邮件
    smtp = smtplib.SMTP()
    smtp.connect("smtp.qq.com")  # 邮箱服务器
    smtp.login(username, password)  # 登录邮箱
    smtp.sendmail(sender, receivers, msg.as_string())  # 发送者和接收者
    smtp.quit()
    print("邮件已发出,请注意查收!")


def new_report(test_report):
    """查找测试目录，找到最新生成的测试报告文件======"""
    lists = os.listdir(test_report)  # 列出目录的下所有文件和文件夹保存到lists
    lists.sort(key=lambda fn: os.path.getmtime(test_report + fn))  # 按时间排序
    file_new = os.path.join(test_report, lists[-1])  # 获取最新的文件保存到file_new
    return file_new
