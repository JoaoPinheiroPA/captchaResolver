from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options

def click_click(elemento: str, driver: webdriver, delay = 100, by = By.XPATH):
    tentativas = 0
    while True:
        tentativas = tentativas + 1
        if tentativas > 3:
            break
        try:
            element = WebDriverWait(driver, delay).until(
            EC.presence_of_element_located((by, elemento))
            )
            element.click()
            break
        except:
            pass

def element_value(elemento: str, driver: webdriver, delay = 100, by = By.XPATH):
    tentativas = 0
    while True:
        tentativas = tentativas + 1
        if tentativas > 3:
            break
        try:
            element = WebDriverWait(driver, delay).until(
            EC.presence_of_element_located((by, elemento))
            )
            return element.get_attribute("src")
        except:
            pass

def click_input(elemento: str,input: str, driver: webdriver, delay = 100):
    tentativas = 0
    while True:
        tentativas = tentativas + 1
        if tentativas > 3:
            break
        try:
            element = WebDriverWait(driver, delay).until(
            EC.presence_of_element_located((By.XPATH, elemento))
            )
            element.send_keys(input)
            break
        except:
            pass

def clear_cache(driver):
    # Limpar cookies
    driver.delete_all_cookies()

    # Limpar cache usando o protocolo CDP do Chrome
    driver.execute_cdp_cmd("Network.clearBrowserCache", {})
    driver.execute_cdp_cmd("Network.clearBrowserCookies", {})
    print("Cache e cookies limpos.")

def remove_items_da_lista2_que_estejam_lista1(lista_saque,lista_contas): #Entrada (lista_saque, lista_contas)
    nova_lista = []
    for item in lista_contas: #contas
        if item not in lista_saque:
            nova_lista.append(item)
    return nova_lista

def filtra_listas(array1, array2):
    # Converter listas em conjuntos para utilizar operações de diferença simétrica
    set1 = set(array1)
    set2 = set(array2)

    # Usar a diferença simétrica para obter os elementos exclusivos entre os dois conjuntos
    elementos_exclusivos = set1.symmetric_difference(set2)

    # Converter o resultado de volta para uma lista (opcional)
    resultado = list(elementos_exclusivos)
    return resultado

def aguardarItem(driver, elemento, by=By.XPATH, waitTime = 120):
    if(WebDriverWait(driver, waitTime).until(EC.presence_of_element_located(
    (By.XPATH, elemento)))):
        return True
    else:
        return False