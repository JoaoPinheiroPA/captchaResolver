from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#
from utils.iaKit.dataSetIcones.salvarIcones import salvar_icones
from utils.utilitarios import click_input, click_click,aguardarItem

def login(user_name, user_key, driver):
    #Click Login
    click_click("//span[text()='Login']", driver)
    #Digite sua Conta
    click_input('//input[@placeholder="Digite o Conta"]',user_name,driver)
    #Digite sua Senha
    click_input('//input[@placeholder="Inserir Senha"]',user_key,driver)
    #Login
    click_click('//button[@class="ui-button ui-button--primary ui-button--normal ui-button--block"]',driver)
    #Chamar algo que vai salvar o icone img do capth
    print(salvar_icones(driver))
    #Aguardar estar logado
    # aguardarItem(driver,"//span[text()='Agente']")
    # print('FIM')