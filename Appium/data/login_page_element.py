from selenium.webdriver.common.by import By
'''
    '': (By.XPATH,''),
    # 
'''
login_element = {
    'accept_protocol': (By.ID, 'paydar.huijinwei:id/btn_custom_privacy_sure'),
    # 协议同意按钮
    'refuse_protocol': (By.ID, 'aydar.huijinwei:id/btn_custom_privacy_cancel'),
    # 协议拒绝按钮
    'login_input': (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[3]/android.view.View/android.view.View/android.view.View/android.widget.EditText'),
    # 手机号输入框
    'login_accept_protocol': (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[6]/android.view.View'),
    # 我已阅读并同意XXX复选框
    'login_button': (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[5]'),
    # 登录/注册按钮
    'login_as_admin': (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[2]/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[4]/android.view.View[4]/android.view.View'),
    # 管理员账号
    'code': (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[2]/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[3]/android.view.View[7]/android.view.View/android.widget.EditText'),
    # 验证码
}
