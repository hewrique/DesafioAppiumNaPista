import pytest
from pages.home import Intro
from pages.login import Login
from utils import constants
from selenium import webdriver
@pytest.mark.usefixtures('setup_test')
class TestNaPista(object):
    
    def teste_campos_vazios(self, setup_test):
        
          home = Intro(setup_test)
          home.intro_login()
          home.logando()
          login = Login(setup_test)
          login.clicar_acessar()
          login.menssagem_erro_semalgo
         
            
    def teste_login_valido(self, setup_test):
        
          home = Intro(setup_test)
          home.intro_login()
          login = Login(setup_test)
          home.logando()
          login.inserir_email(constants.credentials['valid_email'])
          login.inserir_senha(constants.credentials['valid_password_for_valid_email'])
          login.clicar_acessar()
          home.biomet()
          esta_logado = login.esta_logado()
          if esta_logado:
             assert True
          else:
            assert False
            
            
    def teste_login_invalido(self, setup_test):
         home = Intro(setup_test)
         home.intro_login()
         login = Login(setup_test)
         login.inserir_email(constants.credentials['invalid_email'])
         login.inserir_senha(constants.credentials['invalid_password'])
         login.clicar_acessar()
         message = login.mensagem_erro()
         assert message == constants.credentials['error_message'], "Login ou senha incorretos"
        
        
        
    def teste_campo_sem_senha(self, setup_test):
        
         home = Intro(setup_test)
         home.intro_login()
         login = Login(setup_test)
         login.inserir_email(constants.credentials['valid_email'])
         login.clicar_acessar()
         message = login.menssagem_erro_semalgo()
         assert message == constants.credentials['error_message_nopass'], "Informativo Preencha os campos"
        
    def teste_campo_sem_email(self, setup_test):
        
         home = Intro(setup_test)
         home.intro_login()
         login = Login(setup_test)
         login.inserir_senha(constants.credentials['valid_password_for_valid_email'])
         login.clicar_acessar()
         message = login.menssagem_erro_semalgo()
         assert message == constants.credentials['error_message_nopass'], "Informativo Preencha os campos"
    