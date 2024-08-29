#!/usr/bin/bash

echo "Você fez alguma alteração no org?"
./adicionar-arquivos-pdf.py
./git-auto.sh
echo "Pronto"
