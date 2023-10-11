#!/bin/env python3
"""Hello world Multi Linguas
    programa que mostra hello world!
    ira mostrar hello world de acordo com a lingua do ambiente configurado

como usar:
    tenha a variavel LANG configurado no seus sistema linux
    exemplo:
        export LANG=pt_BR.UTF-8

execuçao:
    python3 main.py
    ou
    ./main.py
"""
import os
__version__ = "0.1.2"
__author__ = "nicolas"

current_language = os.getenv("LANG", "en_US")[:5]
msg = {
    "pt_BR": "ola mundo!",
    "en_US": "hello world",
    "es_SP": "hola, mundo"
}
print(msg[current_language])
