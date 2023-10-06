from airtest import iOS

# 初始化 Airest
device = iOS()

# 连接设备
device.connect()

# 打开应用
device.open_app(bundle_id="com.example.app")

# 在应用中执行一些操作，比如点击按钮
device.tap(x=100, y=200)

# 断开设备连接
device.disconnect()
