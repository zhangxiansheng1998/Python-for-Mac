from bs4 import BeautifulSoup
import os


def generate_summary(file_path):
    # 确保文件存在
    if os.path.isfile(file_path):
        # 打开文件并读取内容
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # 使用BeautifulSoup解析HTML
        soup = BeautifulSoup(content, 'html.parser')

        with open("../../ERP/summary.txt", "w", encoding="utf-8") as file:
            # 找到所有的文本并打印
            for text in soup.stripped_strings:
                if text!='筑家工厂-WEB自动化测试报告' and text!='本邮件为自动发送，无需回复。如需查看详细内容，请下载附件！' and text!='提示：预览附件时，邮箱没有加载CSS样式，导致数据显示错乱！':
                    #print(text)
                    text_to_save = str(text) + "\n"
                    file.write(text_to_save)
    else:
        print("文件不存在")


generate_summary("/Users/macbook_air/Desktop/MyProject/Zhujia_Factory/report_email/2024-03/2024-03-25/2024-03-25~11-17-47.html")