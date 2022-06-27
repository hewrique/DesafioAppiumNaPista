from pages.base import Base

from .locators.login_locators import *


class Intro(Base):
    def intro_login(self):
        btn_proximo1 = Base.inicio_busca(self.drive,LoginPageLocators.PROXIMO1)
        btn_proximo1.click()
        
        btn_proximo2 = Base.inicio_busca(self.drive,LoginPageLocators.PROXIMO2)
        btn_proximo2.click()
        
        btn_comecar = Base.inicio_busca(self.drive,LoginPageLocators.COMECAR)
        btn_comecar.click()
        
        btn_tenho = Base.inicio_busca(self.drive,LoginPageLocators.JATENHO)
        btn_tenho.click()
    def logando(self):
        btn_email = Base.inicio_busca(self.drive,LoginPageLocators.EMAIL)
        btn_email.click()
        
        btn_senha = Base.inicio_busca(self.drive,LoginPageLocators.SENHA)
        btn_senha.click()
        
        btn_acessar = Base.inicio_busca(self.drive,LoginPageLocators.ACESSAR)
        btn_acessar.click()
        
    def biomet(self):
        alerta_bio = Base.inicio_busca(self.drive,LoginPageLocators.BIOMETRIA)
        alerta_bio.click()
        