#coding=utf-8
from appium import webdriver
#from selenium import webdriver
import time,os
#测试机魅族note2  小程序

desired_caps = {'platformName': 'Android',
'platformVersion': '5.1',
'deviceName': 'm2 note',
'app': '',
'appPackage': 'com.tencent.mm',
'appActivity':'.ui.LauncherUI',
'unicodeKeyboard': True,
'resetKeyboard': True,
'chromeOptions': {'androidProcess': 'com.tencent.mm:tools'}
}
#测试机 小米4
# desired_caps = {'platformName': 'Android',
# 'platformVersion': '6.0.1',
# 'deviceName': '小米4',
# 'app': '',
# 'appPackage': 'com.tencent.mm',
# 'appActivity':'.ui.LauncherUI',
# 'unicodeKeyboard': True,
# 'resetKeyboard': True,
# 'chromeOptions': {'androidProcess': 'com.tencent.mm:tools'}
# }


#启动软件

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

	

driver.implicitly_wait(10)



driver.find_element_by_xpath('//android.widget.RelativeLayout[3]').click() 
driver.find_element_by_xpath('//android.widget.RelativeLayout[3]').click() 
driver.find_element_by_xpath('//android.widget.ListView/android.widget.LinearLayout[7]').click()
driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.view.View/android.support.v7.widget.LinearLayoutCompat").click()
driver.find_element_by_name(u"搜索小程序").send_keys(u"凤凰优选配送中心")
command0 ='adb shell ime list -s'#列出手机所有的输入法
command1 ='adb shell ime set io.appium.android.ime/.UnicodeIME'#appium输入法
# command2 ='adb shell ime set com.sohu.inputmethod.sogou.xiaomi/.SogouIME'#搜狗输入法（小米）
command2 = 'adb shell ime set com.meizu.flyme.input/com.meizu.input.MzInputService'#魅族手机
os.system(command2)#使用输入法
time.sleep(10)
driver.keyevent(66)
print(driver.contexts)
driver.switch_to.context('WEBVIEW_com.tencent.mm:tools')
driver.switchTo().frame("__WeixinJSBridgeIframe_SetResult")
driver.find_element_by_xpath('//*[@id="__WeixinJSBridgeIframe_SetResult"]').click()

#driver.find_element_by_id("com.tencent.mm:id/jk").click()
time.sleep(10)

# driver.switch_to.context('WEBVIEW_com.tencent.mm:tools') #切换进入webview

# driver.find_element_by_xpath("/html/body/wx-view/wx-view[3]").click()
# #driver.find_element_by_xpath('/html/body/section/section/div/div[3]/ul/li[1]/a').click()
driver.quit()