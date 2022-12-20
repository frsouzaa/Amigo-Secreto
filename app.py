from pyautogui import press, hotkey, moveTo, click
from webbrowser import open
from time import sleep
from random import shuffle


NOME_HOST: str = ""
# Exemplo: NOME_HOST: str "Felipe"
NUMERO_HOST: str
# Exemplo: NUMERO_HOST: str = "5511000000000"


def mandarMensagem(nome: str, numero: int):

    url = f'https://web.whatsapp.com/send?phone={numero}&text=Você%20tirou%20o/a:%20{nome}'

    open(url)
    sleep(10)
    press('enter')
    sleep(2)
    if numero != NUMERO_HOST:
        apagarMensagem()
    hotkey('ctrl', 'w')
    sleep(2)
    press('enter')


def apagarMensagem():
    for x,y in [(1758, 959), (1694, 895), (1165, 627)]:
        moveTo(x=x, y=y, duration=0.3)
        click()
    sleep(6)

# Pode ser colocado um numero ilimitado de pessoas
pessoas = [
    {'nome': NOME_HOST, 'numero': NUMERO_HOST},
    {'nome': 'Pessoa2', 'numero': "5511000000000"},
    {'nome': 'Pessoa3', 'numero': "5511000000000"},
    {'nome': 'Pessoa4', 'numero': "5511000000000"},
]

shuffle(pessoas)

for i in range(len(pessoas)):
    mandarMensagem(pessoas[i-1]["nome"], pessoas[i]["numero"])
    