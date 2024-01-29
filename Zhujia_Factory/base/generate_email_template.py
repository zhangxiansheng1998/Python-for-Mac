import re
from datetime import time
from Zhujia_Factory.base.E_mail import *
from Zhujia_Factory.runall.run_all import *
from Zhujia_Factory.data.login_page_element import *

now = time.strftime("%Y-%m-%d~%H-%M-%S")  # 获取当前时间
today = datetime.today()  # 获取当前日期
formatted_date = today.strftime("%Y-%m-%d")  # 格式化日期为字符串，例如："2024-01-12"

def create_folder_for_today_two():
    """在report目录下生成当天日期的目录"""
    # 获取当前日期
    today = datetime.today()
    # 格式化日期为字符串，例如："2024-01-12"
    formatted_date1 = today.strftime("%Y-%m-%d")

    # 构建目录路径
    folder_path = os.path.join('../report_email', formatted_date1)

    # 检查目录是否已经存在，如果不存在则创建
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"文件夹'{formatted_date1}'创建成功")

def extract_test_summary_with_regex(html_file):
    with open(html_file, 'r', encoding='utf-8') as file:
        content = file.read()

    # Define regular expressions
    total_tests_pattern = re.compile(r'"testAll": (\d+)')
    passed_tests_pattern = re.compile(r'"testPass": (\d+)')
    failed_tests_pattern = re.compile(r'"testFail": (\d+)')
    skipped_tests_pattern = re.compile(r'"testSkip": (\d+)')
    begin_time_pattern = re.compile(r'"beginTime": "(.*?)"')
    running_time_pattern = re.compile(r'"totalTime": "(.*?)"')

    # Match patterns in the content
    total_tests_match = total_tests_pattern.search(content)
    passed_tests_match = passed_tests_pattern.search(content)
    failed_tests_match = failed_tests_pattern.search(content)
    skipped_tests_match = skipped_tests_pattern.search(content)
    begin_time_match = begin_time_pattern.search(content)
    running_time_match = running_time_pattern.search(content)

    # Extract information
    total_tests = int(total_tests_match.group(1)) if total_tests_match else "正则表达式提取有误"
    passed_tests = int(passed_tests_match.group(1)) if passed_tests_match else "正则表达式提取有误"
    failed_tests = int(failed_tests_match.group(1)) if failed_tests_match else "正则表达式提取有误"
    skipped_tests = int(skipped_tests_match.group(1)) if skipped_tests_match else "正则表达式提取有误"
    begin_time_tests = begin_time_match.group(1) if begin_time_match else "正则表达式提取有误"
    running_time_tests = running_time_match.group(1) if running_time_match else "正则表达式提取有误"
    success_rate = "{:.1%}".format(passed_tests / total_tests if skipped_tests == 0 else passed_tests / (total_tests-skipped_tests))
    env = 'Prd' if website['url'] == 'http://admin.huijinwei.com' else 'Dev'

    return {
        '用例总数': total_tests,
        '用例通过': passed_tests,
        '用例失败': failed_tests,
        '用例跳过': skipped_tests,
        '开始时间': begin_time_tests,
        '运行时间': running_time_tests,
        '成功率': success_rate,
        '运行环境':env
    }


def generate_html(data):
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>WEB自动化测试报告</title>
    </head>
    <body>
    
    <style>
    .panel {{
                width: 600px;
                height: 530px;
                margin: auto 0;
                box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.3);
                border-radius: 5%;
                background-image: url("../background.jpg");
                background-size: cover;
                background-repeat: no-repeat;
            
    </style>
    
    <div class="panel">
        <div style="text-align: center;padding-top: 4%;">
            <div style="font-weight: bold;font-size: 25px;">筑家工厂-WEB自动化测试报告</div>
        </div>
        <div style="text-indent: 2em;padding-top: 1%;">
            <div style="padding-top: 1%;color: #0066FF;">测试框架：python+unittest+selenium</div>
            <div style="padding-top: 2%;color: #0066FF;">测试环境：{data['运行环境']}</div>
            <div style="padding-top: 2%;color: #0066FF;">浏览器名称：Chrome</div>
            <div style="padding-top: 2%;color: #0066FF;">浏览器版本：93.0.4577.82</div>
            <div style="padding-top: 2%;color: #0066FF;">用例总数: {data['用例总数']}</div>
            <div style="padding-top: 2%;color: #0066FF;">用例通过: {data['用例通过']}</div>
            <div style="padding-top: 2%;color: #0066FF;">用例失败: {data['用例失败']}</div>
            <div style="padding-top: 2%;color: #0066FF;">用例跳过: {data['用例跳过']}</div>
            <div style="padding-top: 2%;color: #0066FF;">成功率: {data['成功率']}</div>
            <div style="padding-top: 2%;color: #0066FF;">开始时间: {data['开始时间']}</div>
            <div style="padding-top: 2%;color: #0066FF;">运行时间: {data['运行时间']}</div>
            <div style="padding-top: 2%;color: red;font-size: 17px;">本邮件为自动发送，无需回复。如需查看详细内容，请下载附件！</div>
            <div style="padding-top: 1%;color: red;font-size: 17px;">提示：预览附件时，邮箱没有加载CSS样式，导致数据显示错乱！</div>
        </div>
        </div>
    </body>
    <script >
    </script>
    </html>
    """
    return html_content


def save_html(html_content, filename=f'{project_path}/report_email/{formatted_date}/{now}.html'):
    with open(filename, 'w') as file:
        file.write(html_content)

