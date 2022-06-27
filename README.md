**Automação do aplicativo NaPista (Login page)**

Esse projeto visa automatizar a indrodução do aplicativo até a sua autenticação de login;

Foram usados 2 maneiras de teste, uma de forma mais limpa e outra de forma mais "crua".

Nesse README iremos tratar apenas da primeira maneira de teste.

Mais informações nas **Considerações Finais**

___

**Estrutura do projeto:**

Utilizando a estrutura pytest nós obtemos o esqueleto a seguir:

```
NaPistaMain/
  pages/
      locators/
          login_locators.py
      base.py
      home.py
      login.py
  setup/
      DeviceId.py
      apks/
          app_release.apk
  tests/
      test_NaPista.py
  utils/
      constants.py
```

🗂 **Explicando cada pasta:**

Pages >> PageObjects, um arquivo .py para cada funcionalidade.

Setup >> Aqui obtemos o arquivo APK que foi usado e seu numero de serie que está no arquivo .py -> (DeviceId.py).

Tests >> Sequencia de testes.

Utils >> Utilidades do projeto, como suas constantes (constants.py).
___

**Programas**

🎯  I am using here:

Python<br>
Pytest<br>
Appium-Python-Client<br>
Appium-Inspector<br>
Selenium<br>

🛠 Como instalar?

Apenas rode requirements.txt usando o seguinte comando no terminal da sua IDE:

```
pip install -r requirements
```
___

💻  **Test environment setup**

A pasta de aplicação e o número de série do produto Android estão registados na pasta /setup. 
Basta inserir o seu número de série (dispositivos adb) em DeviceId.py.

Para inciar o projeto, digite pytest<br> no terminal:

```
pytest
```
Para inciar o projeto NaPistaMain, é só incializar em sua IDE de preferencia.
___

💿 ** Considerações finais **

De acordo com a bateria de testes, aparentemente os campos de inserir e-mail e de inserir senha foram feitos de uma maneira onde o parametro "send_keys()" não consegue ser executado Apenas o parametro ActionsChains, que, por sua vez, é estritamente preso ao modulo "Driver" e eu não encontrei maneiras de puxar esse metodo sem ter conflito com os demais. Por conta disso, foi desenvolvido outro arquivo de teste que está nesse repositório como "NaPistaMain".
