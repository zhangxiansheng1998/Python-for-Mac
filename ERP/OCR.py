from selenium import webdriver
from PIL import Image
import pytesseract
import io

driver = webdriver.Chrome()
driver.get("http://zkcjcx.jxeea.cn/zkcjcx/")
driver.maximize_window()


def code_verify(x,y,width,height):
    while True:
        screenshot = driver.get_screenshot_as_png()
        screenshot_img = Image.open(io.BytesIO(screenshot))

        left = x
        upper = y
        right = x + width
        lower = y + height
        image_cropped = screenshot_img.crop((left, upper, right, lower))

        # 保存裁剪后的图片
        image_cropped.save('cropped_image.png')

        # 使用OCR库识别图片中的内容
        captcha_text_raw = pytesseract.image_to_string(image_cropped)
        captcha_text = captcha_text_raw.strip()     # 去除验证码中的空白字符，这个方法仅能删除字符串开头和结尾的空白字符

        if captcha_text.isalnum() is True:
            print("OCR识别成功，对应的验证码是", captcha_text)
            break
        else:
            print("OCR识别失败，正在重新识别")
            break


code_verify(824, 742,140, 48)

# 关闭浏览器
driver.quit()