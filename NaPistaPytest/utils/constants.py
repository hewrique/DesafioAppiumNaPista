from appium.webdriver.common.appiumby import AppiumBy

validemail = ("comprador@crystal.com")

credentials = {
    'valid_email': 'comprador@crystal.com',
    'valid_password_for_valid_email': '123qwe',
    'invalid_email': '123',
    'invalid_password': 'qwe',
    'error_message': 'Login ou senha incorretos',
    'error_message_nopass': 'Informativo Preencha os campos'
    
    
    
}

LOGIN_ERROR_MESSAGE = AppiumBy.CLASS_NAME, 'android.view.View'
