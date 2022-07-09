from tkinter import *
import requests
from datetime import date

data = date.today()


def pegar_cotacoes():
    requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''

    texto_cotacoes['text'] = texto

master = Tk()
master.title('Cotação atual das moedas')
master.geometry('490x560+610+153')
master.resizable(width=1, height=1)

img_fundo = PhotoImage(file='imagens\\tela.png')
img_botao = PhotoImage(file='imagens\\botao.png')


lab_fundo = Label(master, image=img_fundo)
lab_fundo.pack()

data_atual = Label(master, text=f'Data:   {data.day} / {data.month} / {data.year}', font=('Open Sans', 11, 'bold'), fg='white', background='#2C735F')
data_atual.place(width=120, height=34, x=182, y=90)




botao = Button(master, image=img_botao, command=pegar_cotacoes)
botao.place(width=167, height=52, x=160, y=272)

texto_cotacoes = Label(master, text='', font=('Open Sans', 20, 'bold'), fg='white', background='#2C735F')
texto_cotacoes.place(width=270, height=158, x=101, y=350)





master.mainloop()
