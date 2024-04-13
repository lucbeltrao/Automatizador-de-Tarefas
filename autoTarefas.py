#pip install pyautogui
import pyautogui
import time

# pausa para executar cada comando
pyautogui.PAUSE = 0.5

# abrir o navegador (chrome)
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

# esperar loading para entrar no site
time.sleep(1)

# acessar o link 
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
pyautogui.write(link)
pyautogui.press('enter')

# esperar um tempo maior para loading da página
time.sleep(4)

#2 Fazer login
pyautogui.click(x=483, y=384)
pyautogui.write('pythonlogar@gmail.com')

# escrever a senha 
pyautogui.press('tab')
pyautogui.write('senhasupersecreta')
pyautogui.press('enter')

# importar a base de dados 
import pandas
tabela = pandas.read_csv('produtos.csv')

# cadastrar um produto
# selecionar primeiro campo
pyautogui.click(x=450, y=253)

# para cada linha da minha tabela
for linha in tabela.index:

    #código do produto
    pyautogui.click(x=450, y=253)
    codigo = tabela.loc[linha, 'codigo']
    pyautogui.write(str(codigo))
    pyautogui.press('tab')
    #marca do produto
    pyautogui.write(str(tabela.loc[linha, 'marca']))
    pyautogui.press('tab')
    #tipo do produto
    pyautogui.write(tabela.loc[linha, 'tipo'])
    pyautogui.press('tab')
    #categoria do produto
    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    pyautogui.press('tab')
    #preço unitário do produto
    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))  
    pyautogui.press('tab')
    #custo do produto do produto
    pyautogui.write(str(tabela.loc[linha, 'custo']))
    pyautogui.press('tab')
# observação do produto
# isna = checa se a linha está vazia
    obs = tabela.loc[linha, 'obs']
    if not pandas.isna(obs):
        pyautogui.write(obs)
    pyautogui.press('tab')
# scroll para topo da tela 
    pyautogui.press('enter')
    pyautogui.scroll(6000)

