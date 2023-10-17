#!/bin/env python3
"""Hello world Multi Linguas
    programa que mostra hello world!
    ira mostrar hello world de acordo com a lingua do ambiente configurado

como usar:
    tenha a variavel LANG configurado no seus sistema linux
    exemplo:
        export LANG=pt_BR.UTF-8

usando CLI:
    python3 main.py --lang=pt_BR
execuçao:
    python3 main.py
    ou
    ./main.py
"""
import os
import sys
__version__ = "0.1.2"
__author__ = "nicolas"
arguments = {
    "lang": None,
    "cout": 1  
}
for arg in sys.argv[1:]:
    # TODO - tratar value error
    key, value = arg.split("=")
    key = key.lstrip("-").strip()
    value = value.strip()
    if key not in arguments:
        print(f" opçao {key} invalida!")
        sys.exit()
    arguments[key] = value
msg = {
    "pt_BR": "ola mundo!. ",
    "en_US": "hello world. ",
    "es_SP": "hola, mundo. "
}
current_language = arguments["lang"]

if current_language is None:
    current_language = os.getenv("LANG", "en_US")[:5]


print(msg[current_language] *  int(arguments["cout"]))
