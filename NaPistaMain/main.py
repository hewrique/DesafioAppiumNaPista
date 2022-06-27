# This sample code uses the Appium python client v2
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from lib2to3.pgen2 import driver
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from utils.credentials import *

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains

### CARREGANDO APLICATIVO ###



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


### DEFINIÇÕES ###

def esperar(tempo):
    driver.implicitly_wait(tempo)

def WelcomePage():
    PROXIMO1 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Próximo")
    PROXIMO1.click()

    PROXIMO2 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Próximo")
    PROXIMO2.click()
        
    COMECAR = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Vamos começar")
    COMECAR.click()

    CONFIRMAR = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Já tenho conta")
    CONFIRMAR.click()

def click_email():
    EMAIL = driver.find_element(by=AppiumBy.XPATH, value = '//android.widget.EditText[1]')
    EMAIL.click()

def inserir_email(self):
    ActionChains(driver).send_keys(self).perform()

def click_senha():
    SENHA = driver.find_element(by=AppiumBy.XPATH, value = '//android.widget.EditText[2]')
    SENHA.click()

def inserir_senha(self):
    ActionChains(driver).send_keys(self).perform()

def acessar_conta():
    CONTA = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Acessar conta")
    CONTA.click()        

def click_bio():
    BIOMETRIA = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Não")
    BIOMETRIA.click()


### MAIN ###

esperar(10)

WelcomePage()
click_email()
inserir_email(email_valido)
click_senha()
inserir_senha(senha_valida)
acessar_conta()
click_bio()

esperar(10)









 