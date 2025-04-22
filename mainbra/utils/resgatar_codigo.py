from utils.utilitarios import click_input, click_click,aguardarItem
from time import sleep

def resgatar_codigo(driver,url_codigo, codigo):
    while True: # Tenta Colocar o Codigo, enquando não aparecer o local para colocar
    # Ir direto para a pagina de resgate
        driver.get("https://" + url_codigo)
    # Verificar se a teg esta na pagina, se não estiver descer na pagina e procurar novamente
    ##local do resgate 'Ler Arquivo de configuração com a posição'
        sleep(0.5)
        #Verificar se o código foi rescatado
        try:
            #Observa se o botão deParabéns, concluiu com êxito a troca!
            aguardarItem(driver, "//div[span[text() = 'Parabéns, concluiu com êxito a troca!']]",waitTime=1.5)
            print('Conta Já Resgatada')
            break
        except:
            print('Conta Não Resgatada')
            pass
        try:
            aguardarItem(driver, "//input[@placeholder='Introduza o código de resgate']", waitTime= 1)
            #Colocar o código
            click_input("//input[@placeholder='Introduza o código de resgate']", codigo, driver, delay=5)
            #Resgatar o código
            click_click("//button[@class='ui-button ui-button--success ui-button--normal']",driver, delay=2)
            sleep(1)
            break
        except:
            print('Tentando Clicar no banner para resgatar o código')
            tentativas = tentativas + 1
            if tentativas > 3:
                break
            pass