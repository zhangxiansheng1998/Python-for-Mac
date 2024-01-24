import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os
import tkinter as tk
from tkinter import filedialog

#选择文件夹
# 实例化
root = tk.Tk()
root.withdraw()

def file_ext(filename, level=1):
    return filename.split('.')[-level]

def _contain_file(path, extensions):
    assert os.path.exists(path), 'path must exist'
    assert os.path.isdir(path), 'path must be dir'

    if isinstance(extensions, str):
        extensions = [extensions]

    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            if (extensions is None) or (file_ext(file) in extensions):
                return True
    return False

def _process_extensions(extensions=None):
    if extensions is not None:
        if isinstance(extensions, str):
            extensions = [extensions]
        assert isinstance(extensions, (list, tuple)), \
            'extensions must be str or list/tuple of str'
        for ext in extensions:
            assert isinstance(ext, str), 'extension must be str'
    return extensions

def get_files(path, extensions=None, is_recursive=True):
    extensions = _process_extensions(extensions)
    files = []
    # get files in current path
    if not is_recursive:
        for name in os.listdir(path):
            fullname = os.path.join(path, name)
            if os.path.isfile(fullname):
                if (extensions is None) or (file_ext(fullname) in extensions):
                    files.append(fullname)
        return files
    # get files recursively
    for main_dir, _, sub_file_list in os.walk(path):
        for filename in sub_file_list:
            fullname = os.path.join(main_dir, filename)
            if (extensions is None) or (file_ext(fullname) in extensions):
                files.append(fullname)
    return files

if __name__ == '__main__':
    path = filedialog.askdirectory()

    files = get_files(path)
    print(files)

mail_host ='smtp.qq.com' #mail_host = 'smtp.qq.com'
port=465 #QQ邮箱是465
send_by = '1120620374@qq.com'
password = 'legbyrctuueyhggb'
username_recv = ["m15180381485@163.com", '596137586@qq.com'] # 收件人，多个收件人用逗号隔开

msg = MIMEMultipart() # 创建一个带附件的实例
msg["Subject"] = files[0].split('\\')[-1].split('.')[-2]+"自动发送"#修改邮件标题，自动取一个附件名称
msg["From"] = send_by
print(msg["Subject"] )
# ---文字部分---
part = MIMEText("这是自动发送的净值，请查收，谢谢！")
msg.attach(part)

# ---附件部分---
for each in files:
    part = MIMEApplication(open(each, 'rb').read())
    part.add_header('Content-Disposition', 'attachment', filename=each.split('\\')[-1])
    msg.attach(part)

# 要注意位置参数和关键字参数啊啊
smtp = smtplib.SMTP_SSL(mail_host, port, 'utf-8')#原博主使用的是smpt = smtplib.SMTP_SSL(mail_host, port, 'utf-8')，163邮箱会报错
smtp.login(send_by, password)
smtp.sendmail(send_by, username_recv, msg.as_string())
smtp.quit()
print("发送成功")
