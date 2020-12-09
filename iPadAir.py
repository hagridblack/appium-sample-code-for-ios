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
        self.dc['udid'] = 'dxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxb'
        self.dc['platformName'] = 'ios'
        #self.dc['bundleId'] = 'com.google.chrome.ios'
        self.dc['automationName'] = 'XCUITest'
        self.dc['platformVersion'] = '12.4.8'
        self.dc['xcodeOrgId'] = 'xxxxxxxxxx'
        self.dc['xcodeSigningId'] = 'iPhone Developer'
        #self.dc['browserName'] = 'Safari'
        self.dc['deviceName'] = 'iPad4,1'
        self.dc['noReset'] = 'true'
        self.dc['autoAcceptAlerts'] = 'true'
        
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',self.dc)
        #self.driver.implicitly_wait(60) 
        #self.driver.set_page_load_timeout(60000)

    def testUntitled(self):
        # Demo1: home to chrome
        self.driver.swipe(1109, 1526, 138, 1526, 100)

        time.sleep(3)
        self.driver.find_element_by_xpath("xpath=//*[@text='Chrome']").click()

        # Demo2: launch chrome
        time.sleep(3)
        self.driver.find_element_by_xpath("xpath=//*[@text='搜尋或輸入網址']").send_keys('yahoo')
        self.driver.find_element_by_xpath("xpath=//*[@text='搜尋或輸入網址' and @class='UIAStaticText']").click()


    def tearDown(self):
        self.driver.quit()
        
if __name__ == '__main__':
    unittest.main()

