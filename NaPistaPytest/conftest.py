import pytest
from selenium import webdriver




@pytest.fixture(scope='class')
def setup_test():
  caps = {}
  caps["platformName"] = "Android"
  caps["appium:deviceName"] = "emulator-5554"
  caps["appium:app"] = "C:\\Users\\henrique\\Documents\\provas\\testestes\\setup\\apks\\app-release.apk"
  caps["appium:autoGrantPermissions"] = True
  caps["appium:ensureWebviewsHavePages"] = True
  caps["appium:nativeWebScreenshot"] = True
  caps["appium:newCommandTimeout"] = 3600
  caps["appium:connectHardwareKeyboard"] = True
  

  driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
  
  yield driver
  
  driver.quit()
  return setup_test