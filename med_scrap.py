import os
import time
from pathlib import Path
import pandas as pd
import pyautogui
from playwright.sync_api import sync_playwright

# Instancia novo navegador
with sync_playwright() as p:
    # Abrir navegador com devtools
    navegador = p.chromium.launch(headless=False, devtools=True)
    page = navegador.new_page()

    # URL da página inicial
    base_url = "https://www.doctoralia.com.br/psiquiatra/florianopolis"

    # Acesso à página do Olos
    page.goto("https://www.doctoralia.com.br/psicologo/florianopolis")

    # Espera a página carregar completamente
    page.wait_for_load_state('networkidle')

    # Contador para controlar as iterações
    count = 0

    # Lista para armazenar os dados coletados
    data_list = []

    # Loop para coletar dados de todas as páginas
    while count < 50:
        names = page.query_selector_all('span[data-tracking-id="result-card-name"]')
        specializations = page.query_selector_all('span[data-test-id="doctor-specializations"]')
        crms = page.query_selector_all('span.h5.font-weight-normal.mb-0')
        addresses = page.query_selector_all(
            'xpath=/html/body/div[2]/div[3]/main/div[2]/div[1]/div[3]/div[4]/ul/li/div/div/div/div[1]/div[4]/div[2]/div[1]/div[2]/p[1]/span[1]')
        areas_de_atuacao = page.query_selector_all(
            'xpath=/html/body/div[2]/div[3]/main/div[2]/div[1]/div[3]/div[4]/ul/li[1]/div/div/div/div[1]/div[1]/div/div[2]/div[2]/span/span')
        # valores_consulta = page.query_selector_all(
        #     'xpath=/html/body/div[2]/div[3]/main/div[2]/div[1]/div[3]/div[4]/ul/li[1]/div/div/div/div[1]/div[4]/div[2]/div[2]/div[2]/p[2]')

        # Verificar se o número de elementos correspondentes é o mesmo para todos os seletores
        num_elements = min(len(names), len(specializations), len(crms), len(addresses), len(areas_de_atuacao))

        for i in range(num_elements):
            # Coletar os dados
            name_text = names[i].inner_text()
            specialization_text = specializations[i].inner_text()
            crm_text = crms[i].inner_text()
            address_text = addresses[i].inner_text()
            area_text = areas_de_atuacao[i].inner_text() if i < len(areas_de_atuacao) else ""

            # Adicionar os dados à lista
            data_list.append({
                "Nome": name_text,
                "Especialização": specialization_text,
                "CRM": crm_text,
                "Endereço": address_text,
                "Áreas de Atuação": area_text,
            })

            # Imprimir os dados para depuração
            print(f"Nome: {name_text}")
            print(f"Especialização: {specialization_text}")
            print(f"CRM: {crm_text}")
            print(f"Endereço: {address_text}")
            print(f"Áreas de Atuação: {area_text}")
            print()  # Adicionar uma linha em branco entre os registros

        # Incrementar o contador
        count += 1

        # Verificar se existe um elemento de paginação para avançar para a próxima página
        next_page_button = page.query_selector('span.d-none.d-md-inline-block.mr-0-5:text("Próximo")')

        if next_page_button:
            # Clicar no botão de próxima página
            next_page_button.click()
            # Esperar um momento para a próxima página carregar completamente (ajuste conforme necessário)
            page.wait_for_load_state("networkidle")
        else:
            # Se não houver mais páginas, sair do loop
            break

    # Salvar os dados em um arquivo de texto
    file_path = "dados_doctoralia.txt"
    with open(file_path, "w") as file:
        for data in data_list:
            file.write(f"Nome: {data['Nome']}\n")
            file.write(f"Especialização: {data['Especialização']}\n")
            file.write(f"CRM: {data['CRM']}\n")
            file.write(f"Endereço: {data['Endereço']}\n")
            file.write(f"Áreas de Atuação: {data['Áreas de Atuação']}\n")
            file.write("\n")  # Adicionar uma linha em branco entre os registros

    print(f"Dados salvos em '{file_path}'")

# Captura e exibe a posição do cursor
x, y = pyautogui.position()
print(f'Coordenadas: X={x}, Y={y}')
