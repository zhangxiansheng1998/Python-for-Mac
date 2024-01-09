import time
import atomac
import subprocess

start_time = time.time()

def start_appium():
    #atomac.launchAppByBundlePath("/Applications/Appium.app")
    atomac.launchAppByBundleId('io.appium.desktop')
    atomac.terminateAppByBundleId('io.appium.desktop')
    #subprocess.call(["open", "-a", "/Applications/Appium.app"])

def start_xcode():
    pass

start_appium()

end_time = time.time()
elapsed_time = round(end_time - start_time, 1)
print(f"Elapsed time: {elapsed_time} seconds")

