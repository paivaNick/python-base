#!/usr/bin/env python3

"""calculadora que usar argumentos
uso:
    python3 calculadora num1=2 num2=3
    ou
    ./calculadora.py num1=2 num2=3
"""
import sys
__version__ = "0.1.0"
try:
    num1 = sys.argv[1]
    num2 = sys.argv[2]
    operacao = sys.argv[3]
    
    print(f"numero1= {num1} numero2= {num2} operacao {operacao}")
    try: 
        num1_float = float(num1)
        num2_float = float(num2)
        if operacao == "soma":
            soma = num1_float + num2_float
            print(soma)
        elif operacao == "multi":
            multi = num1_float * num2_float
            print(multi)
        elif operacao == "sub":
            sub = num1_float - num2_float
            print(sub)
        elif operacao == "div":
            div = num1_float / num2_float
            print(div)
    except ValueError:
        print("digite um numero valido!!!!")
        
except IndexError:
    print("passe um numero de argumento")

