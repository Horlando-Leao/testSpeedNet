import os
import csv
import time
from threading import Timer
from datetime import datetime

import speedtest

def reader_csv():
    with open('data.csv', 'r') as arquivo_csv:
        leitor = csv.DictReader(arquivo_csv, delimiter=';')
        data = []
        for coluna in leitor:
            data.append( '{0};{1};{2}'.format(coluna['data'],
            coluna['hora'], coluna['velocidade']))
    print(data[-1])

def write_rowc_vs(row:list):
    with open('data.csv', 'a') as arquivo_csv:
        escrever = csv.writer(arquivo_csv, delimiter=';', lineterminator='\n')
        escrever.writerow(row)

def speed_net(Intervaltime:int=30, output=False):

    s = speedtest.Speedtest()
    data_atual = datetime.now().strftime('%d/%m/%Y')
    hora_atual = datetime.now().strftime('%H:%M')
    velocidade = s.download(threads=None)*(10**-6)

    write_rowc_vs([data_atual, hora_atual, velocidade])
    reader_csv()

    Timer(Intervaltime, speed_net).start()

speed_net(Intervaltime=5, output=True)