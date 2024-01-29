"""打开当天生成的ERP订单截图目录，并且单选中，后面只需要手动单击右键选择【共享】-【隔空投送】"""
import subprocess


def run_applescript(script):
    try:
        result = subprocess.run(['osascript', '-e', script], capture_output=True, text=True, check=True)
        output = result.stdout.strip()  # 获取脚本执行的输出并去除首尾的空格和换行符
        return output
    except subprocess.CalledProcessError as e:
        print("Error:", e)
        return None


# 定义要执行的AppleScript代码
applescript_code = """
    -- 生成今天的日期并格式化为 yyyy-mm-dd 格式
    set currentDate to do shell script "date +'%Y-%m-%d'"
    
    set folderPath to "/Volumes/Disk/MyProject/ERP/picture/" & currentDate
    
    tell application "Finder"
        set folderToOpen to POSIX file folderPath as alias
        open folderToOpen
        
        -- 等待一段时间以确保Finder窗口打开
        delay 2
        
        -- 切换到打开的窗口并激活
        activate
        
        -- 获取打开的窗口列表
        set openWindows to every window
        
        -- 最小化除了打开的窗口之外的其他窗口
        repeat with aWindow in openWindows
            if index of aWindow is not 1 then
                set collapsed of aWindow to true
            end if
        end repeat
        
        -- 选中目录下的所有PNG文件
        set selectedItems to every item of folderToOpen whose name extension is "png"
        select selectedItems
        
        -- 模拟右键单击操作
        tell application "System Events"
            keystroke " " using {control down}
        end tell
    end tell

"""

# 执行AppleScript脚本并获取结果
result = run_applescript(applescript_code)
