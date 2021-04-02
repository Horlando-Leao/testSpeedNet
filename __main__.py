import os
import csv
import time
from threading import Timer
from datetime import datetime

import speedtest

def write_rowc_vs(row:list):
    with open('data.csv', 'a') as arquivo_csv:
        escrever = csv.writer(arquivo_csv, delimiter=';', lineterminator='\n')
        escrever.writerow(row)

def speed_net(Intervaltime:int=30):

    s = speedtest.Speedtest()
    data_atual = datetime.now().strftime('%d/%m/%Y')
    hora_atual = datetime.now().strftime('%H:%M')
    velocidade = s.download(threads=None)*(10**-6)
    write_rowc_vs([data_atual, hora_atual, velocidade])

    Timer(Intervaltime, speed_net).start()

speed_net(Intervaltime=1)