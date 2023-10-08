#!/usr/bin/env python3


# teoria dos conjuntos para resolver problemas de complexidade.
#

lista_numeros1 = [1,2,3,4]
lista_numeros2 = [3,2,5,4]

# big O(n) -> O(4)
for n1 in lista_numeros1:
    if n1 in lista_numeros2:
        print(f"{n1} esta dentro da lista_numero2")


#big O(1) -> constante melhor performance
set1 = set(lista_numeros1)
set2 = set(lista_numeros2)

print(set1.intersection(set2))

