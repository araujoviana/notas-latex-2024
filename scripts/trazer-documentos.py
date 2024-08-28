#!/usr/bin/env python3

import shutil
import os
import glob


pasta_downloads = os.path.expanduser('~/Downloads')

pasta_atual = os.getcwd()

arquivos_tex = glob.glob(os.path.join(pasta_downloads, '*.tex'))
arquivos_pdf = glob.glob(os.path.join(pasta_downloads, '*.pdf'))

for arquivo in arquivos_tex:
    shutil.move(arquivo, pasta_atual)
    print(f'Movido {arquivo} para {pasta_atual}')

for arquivo in arquivos_pdf:
    shutil.move(arquivo, pasta_atual)
    print(f'Movido {arquivo} para {pasta_atual}')
    
print("Pronto")

    
