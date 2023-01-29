from appium import webdriver
from time import sleep
import os


account = ''
password = ''
desired_caps = {'platformName': 'Android',
                'platformVersion': '13',
                'noReset': True,
                'deviceName': 'emulator-5554',
                'automationName': 'uiAutomator2',
                'appPackage': 'tw.com.mcddaily',
                'appActivity': 'qqn.SJz',
                }

def startEvn():
    #conda env start
    print("Starting conda virtual environment..")
    os.system("conda activate RobotFramework_Appium")
    #env python
    os.system("C:/Users/j/anaconda3/envs/RobotFramework_Appium/python.exe c:/Users/j/Desktop/Vscode/Appium/Server/emulator_pixel_4.py")

def startEmulator():
    if os.system("adb devices")==0:
        print("starting emulator...")
        os.system("start cmd /k emulator -avd Pixel_4_API_33")
        print("please wait 20 seconds...")
        sleep(5)
        print("please wait 15 seconds...")
        sleep(5)
        print("please wait 10 seconds...")
        sleep(5)
        print("please wait 5 seconds...")
        sleep(5)
        print("finish!")

startEmulator()



print("starting Appium Server")
os.system("start cmd /k appium -a 127.0.0.1 -p 4723")
sleep(7)


driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)


def login():

    sleep(5)
    driver.find_element(
        by="id", value="com.android.permissioncontroller:id/permission_deny_button").click()
    sleep(1)
    # 不允許通知
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
    driver.find_element(
        by='id', value="tw.com.mcddaily:id/etPhone").send_keys(account)
    sleep(1)
    driver.find_element(by='id', value="tw.com.mcddaily:id/btnNext").click()
    sleep(1)
    driver.find_element(
        by='id', value="tw.com.mcddaily:id/etPwd").send_keys(password)
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

    driver.find_element(
        by='xpath', value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.widget.TextView[2]").click()
    sleep(5)

    driver.find_element(by='id', value="tw.com.mcddaily:id/btnClose").click()
    sleep(1)



def startApp():
    print("staring automatic control APP...")
    # 登入
    # login()
    # 每日簽到
    dailyQuest()
    # 每日任務
    currentTask()
    print("Finish！")

startApp()