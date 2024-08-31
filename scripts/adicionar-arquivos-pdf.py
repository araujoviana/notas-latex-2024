#!/usr/bin/env python3

# Esse arquivo adiciona os PDFs ao arquivo HTML

# Essa biblioteca veio instalada na minha versão do python então
# não incluí requirements.txt

from bs4 import BeautifulSoup
import os

RESET = "\033[0m"
VERMELHO = "\033[31m"
VERDE = "\033[32m"

# TODO: Parte da direita não é mais necessária pra essa implementação, remover.
# Esquerda: Nome no arquivo org/html
# Direita: Nome do diretório
mapa_secao_diretorio = {
    "Banco de dados": "banco-de-dados",
    "Estrutura de dados I": "estrutura-de-dados-I",
    "Modelagem Matemática I": "modelagem-matematica-I",
    "Organização de Computadores": "organizacao-de-computadores",
    "Projeto e Análise de Algoritmos": "projeto-e-analise-de-algoritmos",
}

# FIXME: O caminho relativo ../ faz com que o script não funcione se o usuário não está em scripts/
arquivo_html = "./index.html"

# Não sei se funcionaria de um dos symlinks scr,
# mas de dentro da pasta real scripts/ deve dar certo
diretorio_base = "../"

print("Começando...")

with open(arquivo_html, "r", encoding="utf-8") as arquivo:
    arquivo_html_soup = BeautifulSoup(arquivo, "html.parser")

# Encontra os arquivos .pdf de cada matéria
for base, dirs, arquivos in os.walk(diretorio_base):
    for arquivo in arquivos:
        if arquivo.endswith(".pdf"):

            print(f"{VERDE}PDF {arquivo} encontrado!{RESET}")

            # Pega(?) o caminho relativo do arquivo
            caminho_pdf = os.path.relpath(
                os.path.join(base, arquivo), start=diretorio_base
            )

            for nome_secao, nome_diretorio in mapa_secao_diretorio.items():
                if nome_diretorio in base:

                    print(f"Verificando diretório {nome_diretorio}")

                    print(f"Encontrando div com classe {nome_secao}")
                    # Acha a secao correta em html
                    secao = arquivo_html_soup.find("div", class_=nome_diretorio)
                    if secao:

                        print(f"Verificando seção {secao}")

                        # Evita links duplicados
                        existe_link = secao.find_next("a", href=caminho_pdf)
                        if existe_link:
                            print(f"{VERMELHO}Pulando link repetido...{RESET}")
                            continue

                        print(f"{VERDE}Seção correspondente encontrada{RESET}")

                        # Cria tag <a> com o link
                        tag_a = arquivo_html_soup.new_tag("a", href=caminho_pdf)
                        tag_a.string = arquivo
                        print(f"Tag <a> criada: {tag_a}")

                        secao.insert_after(tag_a)
                        print("Tag <a> inserida")

                        # Pula linha para que cada link esteja separado
                        tag_br = arquivo_html_soup.new_tag("br")
                        secao.insert_after(tag_br)
                    else:
                        # Comentário ruim
                        print(
                            f"{VERMELHO}Verificado seção {secao}, sem sucesso...{RESET}"
                        )
        else:
            print(f"{VERMELHO}Arquivo {arquivo} não é pdf{RESET}")

with open(arquivo_html, "w", encoding="utf-8") as arquivo:
    arquivo.write(str(arquivo_html_soup))

print("Pronto")
