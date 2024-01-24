import os


def new_report(test_report):
    lists = os.listdir(test_report)  # 列出目录的下所有文件和文件夹保存到lists
    print(lists)
    for i in lists:
        if i == 'index.html':
            file_new = i
            return file_new


new_report(r'E:\pycharm\PcAutomation\report\2023-08-28_16-15-53')