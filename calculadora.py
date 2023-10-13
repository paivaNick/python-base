#!/usr/bin/env python3

"""calculadora que usar argumentos
uso:
    python3 calculadora num1=2 num2=3
    ou
    ./calculadora.py num1=2 num2=3

extras:
    grava os calculos no arquivo calcs.log
"""
import sys
import os
from datetime import datetime
__version__ = "0.1.2"
try:
    num1 = sys.argv[1]
    num2 = sys.argv[2]
    operacao = sys.argv[3]
    resultado  = None 
    print(f"{num1=}\n{num2=}\n{operacao=}")
    try: 
        num1_float = float(num1)
        num2_float = float(num2)
        if operacao == "soma":
            resultado = num1_float + num2_float
        elif operacao == "multi":
            resultado = num1_float * num2_float
        elif operacao == "sub":
            resultado = num1_float - num2_float
        elif operacao == "div":
            resultado = num1_float / num2_float
        print(f"o resultado é igual a {resultado}")
    except ValueError:
        print("digite um numero valido!!!!")
    path = os.curdir
    filepath = os.path.join(path, "calcs.log")
    timestamp = datetime.now().isoformat()
    user = os.getenv("USER", "anonymous")
    with open(filepath, "a") as file_:
        file_.write(f"{user}: {timestamp}-> {operacao}, {num1}, {num2} = {resultado}\n")
except IndexError:
    print("passe um numero de argumento")

