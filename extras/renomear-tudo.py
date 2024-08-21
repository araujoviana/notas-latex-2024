#!/usr/bin/env python3

import os
import datetime
import re

# Nome dos arquivos, definido pelo usuário
novo_nome = input("Renomear arquivos para: ")

data_atual = datetime.datetime.now().strftime("%Y-%m-%d")

contador = 1
# Padrão esperado: nome_contador_data.extensao
padrao = re.compile(rf"^{re.escape(novo_nome)}_(\d+)_{re.escape(data_atual)}\.[^.]+$")

for arquivo in os.listdir():
    if os.path.isfile(arquivo):
        nome, extensao = os.path.splitext(arquivo)
        
        # Verifica se o nome do arquivo já está no formato desejado
        if not padrao.match(f"{nome}{extensao}"):
            novo_nome_arquivo = f"{novo_nome}_{contador}_{data_atual}{extensao}"
            os.rename(arquivo, novo_nome_arquivo)
            contador += 1
        else:
            print(f"'{arquivo}' já está no formato correto.")

print("Renomeação concluída")
