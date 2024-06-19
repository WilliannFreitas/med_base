import time
import pyautogui
from playwright.sync_api import sync_playwright

# Instancia novo navegador
with sync_playwright() as p:
    # Abrir navegador coom devtools
    navegador = p.chromium.launch(headless=False, devtools=True)
    page = navegador.new_page()

    # Acesso à página do Olos
    page.goto("https://www.doctoralia.com.br/psicologo/florianopolis")

    # Espera a página carregar completamente
    page.wait_for_load_state('networkidle')

    #Clicar na aba Network
    pyautogui.moveTo(1020, 177, duration=1)  # Move o cursor para (x2, y2) em 1 segundo
    pyautogui.click()

    #clicar em
    pyautogui.moveTo(1038, 213, duration=1)  # Move o cursor para (x2, y2) em 1 segundo
    pyautogui.click()


    # # Manter o navegador aberto para inspeção
    # input("Pressione Enter para fechar...")
    # navegador.close()


    time.sleep(8)

    # Captura e exibe a posição do cursor
    x, y = pyautogui.position()
    print(f'Coordenadas: X={x}, Y={y}')




    
    ##Preenche o campo 'Usuário' e 'Senha' com as credencias
    # page.fill("input[name='UserTxt']",'pessoalize.monitoracao')
    # page.fill("input[name='Password']",'@Pslz2023Planj')
    # page.click("input[name='BtnOK']")
    #
    # ##Acessa os campos do menu conforme os nomes das variáveis
    # selectRelatorio = page.locator('#ctl00_PageMenu_LinkButton4')
    # selectRelatorio.click()
    #
    # selectModulosRelatorio = page.locator('#PageMenu_lblMenuLatReports')
    # selectModulosRelatorio.click()
    #
    # selectVisaoAgente = page.locator('#PageMenu_menu1__labelMenuTitle_reports_agent_view')
    # selectVisaoAgente.click()
    #
    # selectAgente = page.locator('#PageMenu_menu1_submenu_reports_agent_agent')
    # selectAgente.click()
    #
    # ##page.fill("input[name='ctl00$PageContent$search1$StartDate']", 'data_atual')
    #
    # ##Preenche o campo 'Data Inicial *' com o variável 'data_formatada'
    # DataInicial = page.locator('#PageContent_search1_StartDate')
    # DataInicial.fill(data_formatada)
    #
    # ##Preenche o campo 'Data Final *' com o variável 'data_formatada'
    # DataInicial = page.locator('#PageContent_search1_EndDate')
    # DataInicial.fill(data_formatada)
    #
    # ##Seleciona o campo template, clica seta para baixo até chegar na opção: 'Dados Faturamento CA v2' e clica Enter.
    # selectTemplate = page.locator('#PageContent_search1_DDTemplate')
    # selectTemplate.click()
    # page.press('#PageContent_search1_DDTemplate', 'ArrowDown')
    # page.press('#PageContent_search1_DDTemplate', 'ArrowDown')
    # page.press('#PageContent_search1_DDTemplate', 'ArrowDown')
    # page.press('#PageContent_search1_DDTemplate', 'ArrowDown')
    # page.press('#PageContent_search1_DDTemplate', 'ArrowDown')
    # page.press('#PageContent_search1_DDTemplate', 'Enter')
    #
    # ##Seleciona o campo Organização, clica seta para baixo até chegar na opção: 'Pessoalize' e clica Enter.
    # selectTemplate = page.locator('#PageContent_search1_DDCompany')
    # selectTemplate.click()
    # page.press('#PageContent_search1_DDCompany', 'ArrowDown')
    # page.press('#PageContent_search1_DDCompany', 'ArrowDown')
    # page.press('#PageContent_search1_DDCompany', 'Enter')
    #
    # page.wait_for_timeout(5000)