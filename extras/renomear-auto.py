#!/usr/bin/env python3

import os
import datetime

# Nome dos arquivos, definido pelo usuário
novo_nome = input("Renomear arquivos para: ")

data_atual = datetime.datetime.now().strftime("%Y-%m-%d")

contador = 1

for arquivo in os.listdir():
    if os.path.isfile(arquivo):

        nome, extensao = os.path.splitext(arquivo)

        novo_nome_arquivo = f"{novo_nome}_{contador}_{data_atual}{extensao}"

        os.rename(arquivo, novo_nome_arquivo)

        contador += 1

print("Renomeação concluída")
