import os
from pathlib import Path

# 删除jtl文件
os.system("rm -rf /Volumes/Disk/apache-jmeter-5.1.1/jmeter/jtl/1.jtl")

# 删除report文件夹
os.system("rm -rf /Volumes/Disk/apache-jmeter-5.1.1/jmeter/report/1")

os.system(
    "jmeter -n -t /Volumes/Disk/PG4/NdhkApiGatewayTestScripts/TestData/JSFK-Login-100.jmx -l /Volumes/Disk/apache-jmeter-5.1.1/jmeter/jtl/1.jtl -e -o /Volumes/Disk/apache-jmeter-5.1.1/jmeter/report/1  -Jtime=5")

print("report path:" + Path('/Volumes/Disk/apache-jmeter-5.1.1/jmeter/report/1/index.html').as_uri())