
from pathlib import Path

#linkname=Path('/Volumes/Disk/MyProject/Zhujia_Factory/report/2023-10-05_10-55-31.html').as_uri() #本地文件设为超链接

#linkname = '\n测试已全部完成, 可打开 {} 查看报告'.format(Path('/Volumes/Disk/MyProject/Zhujia_Factory/report/2023-10-05_10-55-31.html').as_uri())
linkname = Path('文件路径').as_uri()

print("已生成测试报告，具体内容可查看",linkname)

