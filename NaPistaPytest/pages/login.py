from selenium.common.exceptions import NoSuchElementException
from pages.base import Base
from .locators.login_locators import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait




class Login(Base, object):
    def mensagem_erro(self):
        
        wait = WebDriverWait(self.drive, 10)
        value = wait.until(EC.presence_of_all_elements_located((
            AppiumBy.XPATH, '//android.view.View[@content-desc="Informativo Login ou senha incorretos"]'
        )))
        return value.text
    
    def menssagem_erro_semalgo(self):
        
        wait = WebDriverWait(self.drive, 10)
        value = wait.until(EC.presence_of_all_elements_located((
            AppiumBy.XPATH, '//android.view.View[@content-desc="InformativoPreencha os campos"]'
            
        )))
        return value.text
        
    def inserir_email(self, email):
        
        wait = WebDriverWait(self.drive, 10)
        name = wait.until(EC.presence_of_all_elements_located((
            AppiumBy.XPATH, '//android.widget.EditText'
        )))
        name[0].send_keys(email)[0]
        
    def inserir_senha(self, senha):
    
        wait = WebDriverWait(self.drive, 10)
        name = wait.until(EC.presence_of_all_elements_located((
            AppiumBy.XPATH, '//android.widget.EditText[2]'
        )))
        
        name.send_keys(senha)
        
    def clicar_acessar(self):
        wait = WebDriverWait(self.drive, 10)
        self = wait.until(EC.presence_of_all_elements_located((
             AppiumBy.XPATH, '//android.widget.Button[@content-desc="Acessar conta"]'
            
         )))

        
    
    def na_tela_de_login(self):
        
        try:
            wait = WebDriverWait(self.drive, 10)
            wait.until(EC.presence_of_all_elements_located((
                AppiumBy.XPATH, '//android.widget.Button[@content-desc="Acessar conta"]'
            )))
        except NoSuchElementException:
            return False
        return True
        
    def esta_logado(self):
        
        try:
           wait = WebDriverWait(self.drive, 10)
           wait.until(EC.presence_of_all_elements_located((
               AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[3]/android.view.View/android.view.View'
           )))
           
        except NoSuchElementException:
            return False
        return True

    