# -*- coding: utf-8 -*-

import unittest
import time
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class Untitled(unittest.TestCase):
    reportDirectory = 'reports'
    reportFormat = 'xml'
    dc = {}
    testName = 'Untitled'
    driver = None

    def setUp(self):
        self.dc['reportDirectory'] = self.reportDirectory
        self.dc['reportFormat'] = self.reportFormat
        self.dc['testName'] = self.testName
        self.dc['udid'] = 'd4d6437b0eb9a48a90b3b98ae541ac636ff8746b'
        #self.dc['udid'] = 'dc854c02217bc02909cb3fdd7f7c54142098107e'
        self.dc['platformName'] = 'ios'
        #self.dc['bundleId'] = 'com.google.chrome.ios'
        self.dc['automationName'] = 'XCUITest'
        self.dc['platformVersion'] = '12.4.8'
        self.dc['xcodeOrgId'] = '87222P5M9E'
        self.dc['xcodeSigningId'] = 'iPhone Developer'
        #self.dc['browserName'] = 'Safari'
        self.dc['deviceName'] = 'iPad4,1'
        self.dc['noReset'] = 'true'
        self.dc['autoAcceptAlerts'] = 'true'

        #driver.manage().timeouts().implicitlyWait(50,TimeUnit.SECONDS);
        #driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);  
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',self.dc)
        #Sself.driver = webdriver.Remote('http://192.168.20.163:4723/wd/hub',self.dc)
        #self.driver.implicitly_wait(60) 
        #self.driver.set_page_load_timeout(60000)

    def testUntitled(self):

        #time.sleep(3)
        #self.driver.find_element_by_xpath("xpath=//*[@text='重新載入']").click()


        # Demo1: home to chrome
        self.driver.swipe(1109, 1526, 138, 1526, 100)

        time.sleep(3)
        self.driver.find_element_by_xpath("xpath=//*[@text='Chrome']").click()

        #time.sleep(3)
        #self.driver.find_element_by_xpath("xpath=//*[@text='搜尋或輸入網址']").send_keys('yahoo')
        #self.driver.find_element_by_xpath("xpath=//*[@text='搜尋或輸入網址']").send_keys('http://staging-fms-lite.nxai.io')

        #time.sleep(3)
        #self.driver.find_element_by_xpath("xpath=//*[@text='Go']").click()

        # Demo2: launch chrome
        #time.sleep(3)
        #self.driver.find_element_by_xpath("xpath=//*[@text='搜尋或輸入網址']").send_keys('staging')
        #self.driver.find_element_by_xpath("xpath=//*[@text='搜尋或輸入網址']").send_keys('yahoo')
        #self.driver.find_element_by_xpath("xpath=//*[@text='搜尋或輸入網址']").send_keys('yahoo.tw')
        #self.driver.find_element_by_xpath("xpath=//*[@text='搜尋或輸入網址']").send_keys('https://tw.yahoo.com')
        #self.driver.find_element_by_xpath("xpath=//*[@text='搜尋或輸入網址']").send_keys('192.168.23.68')
        #self.driver.find_element_by_xpath("xpath=//*[@text='搜尋或輸入網址']").send_keys('stackoverflowjdkskfjlknvlsgenrtiufeiurfnwo4ueurfn')
        #input_el = self.driver.find_element_by_xpath("xpath=//*[@text='搜尋或輸入網址']").click()
        #input_el.send_keys('http://staging-fms-lite.nxai.io/')
        #self.driver.find_element_by_xpath("xpath=//*[@text='搜尋或輸入網址' and @class='UIAStaticText']").click()



        #self.driver.find_element_by_xpath("xpath=//*[@text='搜尋或輸入網址']").click()
        #time.sleep(3)
        #urlStr = 'http://staging-fms-lite.nxai.io'
        #urlStr = 'staging-fms-lite.nxai.io'
        #for s in list(urlStr):
        #    self.driver.find_element_by_xpath("xpath=//*[@text='"+ s +"']").click()
            

        #self.driver.find_element_by_xpath("xpath=//*[@text='h']").click()
        #self.driver.find_element_by_xpath("xpath=//*[@text='t']").click()
        #self.driver.find_element_by_xpath("xpath=//*[@text='t']").click()
        #self.driver.find_element_by_xpath("xpath=//*[@text='p']").click()
        #self.driver.find_element_by_xpath("xpath=//*[@text=':']").click()
        #self.driver.find_element_by_xpath("xpath=//*[@text='/']").click()
        #self.driver.find_element_by_xpath("xpath=//*[@text='/']").click()

        #self.driver.find_element_by_xpath("xpath=//*[@placeholder='搜尋或輸入網址']").send_keys("http://staging-fms-lite.nxai.io/")

        #time.sleep(3)
        #self.driver.find_element_by_xpath("xpath=//*[@text='Go']").click()



        time.sleep(8)
        self.driver.find_element_by_xpath("xpath=//*[@class='UIAView' and @y=1026 and @height>0 and ./*[@id='']]").click()
        self.driver.find_element_by_xpath("xpath=//*[@class='UIAView' and @y=1026 and @height>0 and ./*[@id='']]").click()

        #toolList = self.driver.find_elements_by_xpath("xpath=//*[@class='UIAView' and @x=0 and @height>0 and ./*[@text='']]")
        #print(len(toolList))
        #toolList[0].click()

        time.sleep(3)
        #self.driver.find_element_by_xpath("xpath=//*[@class='UIAView' and @y=1164 and @height>0 and ./*[@text='']]").click()
        self.driver.find_element_by_xpath("xpath=//*[@class='UIAView' and @y=1164 and @height>0 and ./*[@id='']]").click()
        self.driver.find_element_by_xpath("xpath=//*[@class='UIAView' and @y=1164 and @height>0 and ./*[@id='']]").click()
        #toolList[1].click()


        
        #self.driver.find_element_by_xpath("xpath=((//*[@class='UIAView' and ./parent::*[@class='UIAView' and ./parent::*[@class='UIAView']]]/*[@class='UIAView'])[9]/*[@class='UIAView'])[2]").click()
        #self.driver.find_element_by_xpath("((//*[@class='UIAView' and ./parent::*[@class='UIAView' and ./parent::*[@class='UIAView']]]/*[@class='UIAView'])[9]/*[@class='UIAView'])[2]").send_keys('http://staging-fms-lite.nxai.io/')
        

        #self.driver.find_element_by_xpath("xpath=//*[@text='搜尋或輸入網址' and @class='UIAStaticText']").click()
        #self.driver.find_element_by_xpath("xpath=//*[@placeholder='搜尋或輸入網址']").send_keys("http://staging-fms-lite.nxai.io/")

        #self.driver.find_element_by_xpath("xpath=//*[@text='NTPHomeFakeOmniboxAccessibilityID']").send_keys('http://staging-fms-lite.nxai.io')
        #self.driver.find_element_by_xpath("xpath=//*[@text='NTPHomeFakeOmniboxAccessibilityID']").click()
        #self.driver.find_element_by_xpath("xpath=//*[@text='搜尋或輸入網址']").send_keys('http://staging-fms-lite.nxai.io')
        

        #self.driver.execute_script("seetest:client.sendText(\"http://staging-fms-lite.nxai.io\")")


        #self.driver.execute_script("seetest:client.deviceAction(\"Enter\")")

        #send_keys('http://staging-fms-lite.nxai.io/')

        


        #self.driver.execute_script("seetest:client.deviceAction(\"Enter\")")
        #self.driver.switch_to.context("NATIVE_APP")
        
        #input_el = self.driver.find_element_by_xpath("xpath=(//*[@text='搜尋或輸入網址' and @class='UIAButton'])")
        #input_el.click()
        #input_el.send_keys('http://staging-fms-lite.nxai.io/')
        #self.driver.find_element_by_xpath("//*[@text='搜尋或輸入網址']").send_keys('http://staging-fms-lite.nxai.io/')
        #self.driver.find_element_by_id("//*[@id='realbox']").send_keys('http://staging-fms-lite.nxai.io/')
        #time.sleep(5)
        #self.driver.find_element_by_xpath("//*[@text='Go']").click()
        #self.driver.get("http://staging-fms-lite.nxai.io/")

        #((//*[@class='UIAView' and ./parent::*[@class='UIAView' and ./parent::*[@class='UIAView']]]/*[@class='UIAView'])[9]/*[@class='UIAView'])[2]
        #self.driver.execute_script("seetest:client.sendText(\"http://staging-fms-lite.nxai.io\")")
        #self.driver.execute_script("seetest:client.deviceAction(\"Enter\")")
        #self.driver.find_element_by_xpath("xpath=(//*[@text='Go'])[1]").click()
        #self.driver.find_element_by_xpath("xpath=//*[@text='h']").click()

        #self.driver.find_element_by_xpath("xpath=//*[@text='' and @class='UIAImage' and ./*[@class='UIAStaticText']]")[1].click()

        #self.driver.find_element_by_xpath("xpath=//*[@text='' and @class='UIAImage' and ./*[@class='UIAStaticText']]")[2].click()

        time.sleep(8)

        #self.driver.swipe(1313, 1463, 180, 1473, 333)
        #self.driver.swipe(100, 100, 50, 100, 500)
        #self.driver.find_element_by_xpath("xpath=//*[@text='Chrome' and (./preceding-sibling::* | ./following-sibling::*)[@text='提示']]").click()
        #self.driver.find_element_by_xpath("xpath=//*[@text='NTPHomeFakeOmniboxAccessibilityID']").click()
        #WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@text='staging-fms-lite.nxai.io/task']")))
        #self.driver.find_element_by_xpath("xpath=//*[@text='staging-fms-lite.nxai.io/task']").click()
        #WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,'//*[@text='' and @class='UIAImage' and ./*[@class='UIAStaticText']]')))
        #self.driver.find_element_by_xpath("xpath=//*[@text='' and @class='UIAImage' and ./*[@class='UIAStaticText']]").click()
        #WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH,'//*[@text='' and @class='UIAImage' and ./*[@class='UIAStaticText']]')))
        #self.driver.find_element_by_xpath("xpath=//*[@text='' and @class='UIAImage' and ./*[@class='UIAStaticText']]").click()
        #self.driver.find_element_by_xpath("xpath=//*[@text='' and @class='UIAImage' and ./*[@class='UIAStaticText']]").click()
        #self.driver.find_element_by_xpath("xpath=//*[@class='UIAView' and @width>0 and @height>0 and ./*[@text='']]").click()
        #WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH,'//*[@text='關閉分頁']')))
        #self.driver.find_element_by_xpath("xpath=//*[@text='關閉分頁']").click()
        #WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH,'//*[@text='關閉分頁']')))
        #self.driver.find_element_by_xpath("xpath=//*[@text='關閉分頁']").click()
        #WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,'//*[@text='關閉分頁']')))
        #self.driver.find_element_by_xpath("xpath=//*[@text='關閉分頁']").click()
        #self.driver.execute_script("seetest:client.deviceAction(\"Home\")")

    def tearDown(self):
        self.driver.quit()
        
if __name__ == '__main__':
    unittest.main()

