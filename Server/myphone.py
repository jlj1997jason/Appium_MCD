from appium import webdriver
from time import sleep

account = ''
password = ''
desired_caps = {
    'platformName': 'Android',
    'platformVersion': '12.0',
    'platform':'Android',
    'deviceName': 'RF8NA0XS6VW',
    'automationName': 'uiAutomator2',
    'appPackage': 'tw.com.mcddaily',
    'appActivity':'qqn.SJz'
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

def dailyQuest():

    sleep(5)
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
    sleep(4)
    driver.find_element(by='id', value="tw.com.mcddaily:id/tv_neg").click()
    sleep(1)

def currentTask():
    driver.find_element(by='id', value="tw.com.mcddaily:id/menu_task").click()
    sleep(4)

    driver.find_element(by='id', value="tw.com.mcddaily:id/ivBoom").click()
    sleep(1)

    driver.find_element(by='id', value="tw.com.mcddaily:id/btnClose").click()
    sleep(1)

    driver.find_element(by='xpath', value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                        ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget"
                        ".LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx"
                        ".recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.ImageView").click()
    sleep(1)

    driver.find_element(by='id', value="tw.com.mcddaily:id/btnNext").click()
    sleep(10)

    driver.find_element(by='id', value="pointer").click()
    sleep(4)

    driver.find_element(by='id', value="tw.com.mcddaily:id/btnClose").click()
    sleep(1)

#每日簽到
dailyQuest()
#每日任務
currentTask()