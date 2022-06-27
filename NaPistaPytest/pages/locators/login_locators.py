from appium.webdriver.common.appiumby import AppiumBy


class LoginPageLocators(object):
    
    PROXIMO1 = (AppiumBy.ACCESSIBILITY_ID, 'Próximo')
    PROXIMO2 = (AppiumBy.ACCESSIBILITY_ID, 'Próximo')
    COMECAR = (AppiumBy.ACCESSIBILITY_ID, 'Vamos começar')
    JATENHO = (AppiumBy.ACCESSIBILITY_ID, 'Já tenho conta')
    EMAIL = (AppiumBy.CLASS_NAME, 'android.widget.EditText')
    SENHA = (AppiumBy.XPATH, '//android.widget.EditText[2]')
    ACESSAR = (AppiumBy.ACCESSIBILITY_ID, 'Acessar conta')
    BIOMETRIA = (AppiumBy.ACCESSIBILITY_ID, 'Não')
    LOGIN_ERROR_MESSAGE = (AppiumBy.CLASS_NAME, 'android.view.View')