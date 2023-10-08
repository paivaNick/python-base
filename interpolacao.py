#!/usr/bin/env python2

clientes = ["nick", "penelope", "aurora"]

email_template = """
- olá %(nome)s tudo bem?
  gostaria de adquirir um %(produto)s
  pro apenas %(preco)d so possui apenas %(qtd) no estoque.
"""

for cliente in clientes:
    print(email_template % (
        {
            "nome": cliente,
            "produto": "ps5",
            "preco": 1350,
            "qtd": 2
        }
    ))
