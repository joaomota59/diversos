#https://pypi.org/project/get-html/ link da documentação da lib
from get_html import create_renderer #carrega a página após ser renderizada com JS
#from get_html import HtmlRenderer
#import asyncio
from bs4 import BeautifulSoup
#import requests

async def manipulate(page):#Função usada para processar algo antes de renderizar a página 
    return
    # https://github.com/miyakogi/pyppeteer/issues/205#issuecomment-470886682
    page2=page
    #await page.cookie({'timeframeSelect':'1'})
    await page.select('select#timeframeSelect','M5')
    #await page.select('#pares', 'Todos')
    #await page.setCookie({'timeframeSelect':'1'})
    #await page.evaluate('{window.scrollBy(0, document.body.scrollHeight);}')

    

with create_renderer() as renderer:
    # use the renderer. The underlying browser will be instanciated on first call to render
    #cookies = dict([cname='timeframeSelect',cvalue='1',exdays='7')
    #s = requests.Session()
    #s.cookies.update({'timeframeSelect':'1'})
    #response = s.get('https://catalogador.ml/')  # Automatically uses the session cookies
    #response = renderer.render(url='https://catalogador.ml/', cookies=s.cookies,keep_page=True)
    response = renderer.render(url='https://catalogador.ml/', manipulate_page_func=manipulate)
    #s = requests.Session()
    #s.cookies.update({'timeframeSelect':'1'})
    #response = s.get('https://catalogador.ml/')  # Automatically uses the session cookies

soup = BeautifulSoup(response.text, 'html.parser')
#print(soup.prettify()) printa o html renderizado plo JavaScript
def getEstrategias():#selecionando estratégias que estão em tags internas do DOM
    for i in soup.select("div.estrategiaContainer div.parInfo div.estrategiaInfo p.estrategiaName"):
        print(i.get_text())
getEstrategias()
