from appium import webdriver
from time import sleep

account = ''
password = ''
desired_caps = {'platformName': 'Android', 
                'platformVersion': '13', 
                'noReset' : True,
                'deviceName': 'emulator-5554', 
                'automationName': 'uiAutomator2', 
                'appPackage': 'tw.com.mcddaily', 
                'appActivity': 'qqn.SJz', 
                'deviceUDID': 'emulator-5554', 
                'deviceApiLevel': 33, 
                'deviceScreenSize': '1080x2280', 
                'deviceScreenDensity': 440, 
                'deviceModel': 'sdk_gphone64_x86_64', 
                'deviceManufacturer': 'Google', 
                'pixelRatio': 2.75, 'statBarHeight': 83, 
                }
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

def login():

    sleep(5)
    driver.find_element(by="id", value="com.android.permissioncontroller:id/permission_deny_button").click()
    sleep(1)
    #不允許通知
    driver.find_element(by="id", value="tw.com.mcddaily:id/btnLeft").click()
    sleep(1)
    driver.find_element(by="id", value="tw.com.mcddaily:id/btnNext").click()
    sleep(1)
    driver.find_element(by="id", value="tw.com.mcddaily:id/btnNext").click()
    sleep(1)
    driver.find_element(by="id", value="tw.com.mcddaily:id/btnNext").click()
    sleep(1)
    driver.find_element(by="id", value="tw.com.mcddaily:id/btnNext").click()
    sleep(1)
    driver.find_element(by='id', value="tw.com.mcddaily:id/etPhone").send_keys(account)
    sleep(1)
    driver.find_element(by='id', value="tw.com.mcddaily:id/btnNext").click()
    sleep(1)
    driver.find_element(by='id', value="tw.com.mcddaily:id/etPwd").send_keys(password)
    sleep(1)
    driver.find_element(by='id', value="tw.com.mcddaily:id/btnNext").click()
    sleep(20)
    driver.find_element(by='id', value="tw.com.mcddaily:id/tv_neg").click()
    sleep(1)

def dailyQuest():
    sleep(4)
    driver.find_element(by='id', value="tw.com.mcddaily:id/menu_task").click()
    sleep(4)

    driver.find_element(by='id', value="tw.com.mcddaily:id/ivBoom").click()
    sleep(1)

    driver.find_element(by='id', value="tw.com.mcddaily:id/btnClose").click()
    sleep(1)


def currentTask():
    driver.find_element(by='xpath', value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                        ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget"
                        ".LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx"
                        ".recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.ImageView").click()
    sleep(3)

    driver.find_element(by='id', value="tw.com.mcddaily:id/btnNext").click()
    sleep(7)
    driver.get_screenshot_as_base64()

    driver.find_element(by='xpath', value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.widget.TextView[2]").click()
    sleep(5)

    driver.find_element(by='id', value="tw.com.mcddaily:id/btnClose").click()
    sleep(1)

# 登入
# login()
# 每日簽到
dailyQuest()
# 每日任務
currentTask()