#!/usr/bin/bash

echo "Você fez alguma alteração no org?"
./adicionar-arquivos-pdf.py
./git-auto.sh
firefox ../index.html
echo "Pronto"
