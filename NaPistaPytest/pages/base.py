from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class Base(object):
    def __init__(self, drive):
        self.drive = drive

    def inicio_busca(self, element):
        """
        Esse metodo é responsavel por achar elementos (com presence_of_element_located condition)
        :param element: elemento a ser procurado
        :return: valor do elemento
        """
        wait = WebDriverWait(self, 10)
        value = wait.until(EC.presence_of_element_located((
            element
        )))
        return value