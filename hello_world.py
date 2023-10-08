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
__version__ = "0.1"
__author__ = "nicolas"
msg = "hello world!"
current_language = os.getenv("LANG", "en_US")[:5]
if current_language == "pt_BR":
    msg = "ola, mundo!"
elif current_language == "it_IT":
    msg = "ciao,mondo!";


print(msg)
