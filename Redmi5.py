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
        self.dc['udid'] = 'xxxxxxxxxxxxx'
        self.dc['platformName'] = 'android'
        self.dc['noReset'] = 'true'
        self.dc['autoAcceptAlerts'] = 'true'

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',self.dc)
        #self.driver.implicitly_wait(60) 
        #self.driver.set_page_load_timeout(60000)

    def testUntitled(self):
        # Demo1: click to chrome
        time.sleep(3)
        self.driver.find_element_by_xpath("xpath=//*[@contentDescription='Chrome' and @class='android.widget.RelativeLayout']").click()

        time.sleep(3)
        self.driver.find_element_by_xpath("xpath=//*[@text='搜尋或輸入網址']").send_keys('yahoo')
        self.driver.find_element_by_xpath("xpath=(//*[@id='key_pos_ime_action']/*[@class='android.widget.ImageView'])[1]").click()

    def tearDown(self):
        self.driver.quit()
        
if __name__ == '__main__':
    unittest.main()

