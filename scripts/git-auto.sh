#!/bin/bash

# Não verifica se realmente existem mudanças, só vai

# FIXME: . não é caminho certo!
git add .
git commit -m "Commit automático em $(date '+%Y-%m-%d %H:%M:%S')"
git push
