#!/usr/bin/bash

echo "Você fez alguma alteração no org?"
./adicionar-arquivos-pdf.py

# FIXME: Arrumar o git add . desse script
./git-auto.sh
firefox ../index.html
echo "Pronto"
