from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

brave_path = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"

# Configurar opções do Chrome
def options(position_x,position_y)->webdriver:
    options = Options()
    # options.binary_location = brave_path
    options.add_argument("--app=https://bra.vip/home/event?id=206063709&eventCurrent=1")
    options.add_argument("--force-device-scale-factor=1")
    options.add_argument(f"--window-size={384},{520}")
    options.add_argument(f"--window-position={position_x},{position_y}")
    # options.add_experimental_option("mobileEmulation", {
    #     "deviceName": "Galaxy S5"  # Substitua pelo dispositivo desejado
    # })
    options.add_argument("--mute-audio")
    options.add_argument("--disable-application-cache")  # Desabilitar cache
    options.add_argument("--disable-cache")  # Desabilitar cache adicionalmente
    options.add_argument("--incognito") #Guianonima
    options.add_argument("--disk-cache-size=0")  # Definir o cache em disco para zero
    options.add_argument("--no-sandbox")  # Evitar problemas de permissões
    #Otimização de recursos
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-plugins")
    options.add_argument("--disable-software-rasterizer")  # Reduz o uso de CPU para gráficos
    # options.add_argument("--disable-gpu")
    # options.add_experimental_option("excludeSwitches", ["enable-automation"])
    # options.add_experimental_option('useAutomationExtension', False)

    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)