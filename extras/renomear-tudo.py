#!/usr/bin/env python3                                                                                                                                                                                                                       

import os
import datetime
import re

# Nome dos arquivos, definido pelo usuário                                                                                                                                                                                                   
novo_nome = input("Renomear arquivos para: ")

# Data atual formatada                                                                                                                                                                                                                       
data_atual = datetime.datetime.now().strftime("%Y-%m-%d")

contador = 1
# Padrão esperado: nome_contador_data.extensao                                                                                                                                                                                               
padrao = re.compile(rf"^{re.escape(novo_nome)}_(\d+)_{re.escape(data_atual)}\.[^.]+$")

for arquivo in os.listdir():
    if os.path.isfile(arquivo):
        # Obtem a data de criação/modificação do arquivo                                                                                                                                                                                    
        data_modificacao = datetime.datetime.fromtimestamp(os.stat(arquivo).st_mtime).strftime("%Y-%m-%d")
        
        # Verifica se o arquivo foi criado/modificado hoje                                                                                                                                                                                  
        if data_modificacao == data_atual:
            nome, extensao = os.path.splitext(arquivo)
            
            # Verifica se o nome do arquivo já está no formato desejado                                                                                                                                                                       
            if not padrao.match(f"{nome}{extensao}"):
                novo_nome_arquivo = f"{novo_nome}_{contador}_{data_atual}{extensao}"
                os.rename(arquivo, novo_nome_arquivo)
                contador += 1
            else:
                print(f"'{arquivo}' já está no formato correto.")
        else:
            print(f"'{arquivo}' foi criado/modificado em {data_modificacao}, não será renomeado.")

print("Renomeação concluída")
