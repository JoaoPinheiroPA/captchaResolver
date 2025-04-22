from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
##
# from reconhecimento_img import encontrar_imagem
from time import sleep

import pyautogui as auto
###
from utils.login import login
from utils.navegador_options import options

#Posição Raiz da Guia
position_x = 0
position_y = 0

# #Lista de Contas -> Ler todas as contas disponiveis
# contas_saque = ler_txt_para_lista('../bra_1_contas_global_saque.txt')

while True:
    
    driver = options(position_x,position_y)

    user_name = "contaconta"
    user_key = "senhasenha"

    login(user_name, user_key, driver)
    sleep(3)
