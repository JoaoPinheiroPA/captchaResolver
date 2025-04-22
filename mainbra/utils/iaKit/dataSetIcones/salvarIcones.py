import os
import requests
from PIL import Image, ImageChops
from io import BytesIO

from selenium import webdriver
from selenium.webdriver.common.by import By

from utils.utilitarios import element_value


def salvar_icones (driver):
    html_img = element_value("(//img[contains(@src, 'https://static.')])[1]", driver)
    baixar_e_renomear_imagem(html_img)


def imagem_ja_existe(imagem_bytes, pasta_destino):
    # Abre a imagem que estamos comparando
    nova_img = Image.open(BytesIO(imagem_bytes))

    # Se a imagem tiver transparência (canal alfa), converte para RGB
    if nova_img.mode == 'RGBA':
        nova_img = nova_img.convert('RGB')  # Remove o canal alfa

    nova_img_resized = nova_img.resize((100, 100))  # Redimensionando para comparação mais rápida

    for nome_arquivo in os.listdir(pasta_destino):
        caminho = os.path.join(pasta_destino, nome_arquivo)
        
        try:
            img_existente = Image.open(caminho)

            # Se a imagem existente tiver transparência, converte para RGB também
            if img_existente.mode == 'RGBA':
                img_existente = img_existente.convert('RGB')

            # Redimensiona a imagem existente
            img_existente_resized = img_existente.resize((100, 100))

            # Compara os dados de pixels das imagens redimensionadas
            if list(nova_img_resized.getdata()) == list(img_existente_resized.getdata()):
                return True, caminho  # As imagens são iguais, retorna o caminho da imagem existente
        except Exception as e:
            print(f"Erro ao comparar com {nome_arquivo}: {e}")

    return False, None  # Caso as imagens não sejam iguais

def baixar_e_renomear_imagem(url_imagem, pasta_destino='imagens_referencia'):
    os.makedirs(pasta_destino, exist_ok=True)

    response = requests.get(url_imagem)
    if response.status_code != 200:
        raise Exception(f"Erro ao baixar imagem: {response.status_code}")

    imagem_bytes = response.content

    # # Verifica se a imagem já existe
    # existe, caminho_existente = imagem_ja_existe(imagem_bytes, pasta_destino)
    # if existe:
    #     print(f"A imagem já existe: {caminho_existente}")
    #     return

    imagem = Image.open(BytesIO(imagem_bytes))
    nome_temporario = "imagem_temp.png"
    caminho_temp = os.path.join(pasta_destino, nome_temporario)
    imagem.save(caminho_temp)
    imagem.show()

    novo_nome = input("Digite o novo nome da imagem (sem extensão): ").strip()
    novo_caminho = os.path.join(pasta_destino, f"{novo_nome}.png")

    os.rename(caminho_temp, novo_caminho)
    print(f"Imagem salva como: {novo_caminho}")