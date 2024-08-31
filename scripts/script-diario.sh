#!/usr/bin/bash

echo "Você fez alguma alteração no org?"
./scripts/adicionar-arquivos-pdf.py

# FIXME: Arrumar o git add . desse script
./scripts/git-auto.sh
firefox ./index.html
echo "Pronto"
