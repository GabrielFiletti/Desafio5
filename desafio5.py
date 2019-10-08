#!/bin/python3

import sys

def numeroDeDias(ar):
    n = -1              # Numero de dias em que houve a morte de plantas
    morreu = True       # Indica se alguma planta morreu no dia atual

    # Este while conta o número de dias até que as plantas pararam de motter
    
    while morreu:
        print(ar)
        morreu = False          # Reseta o valor no começo de cada iteração
        indices_morreu = []     # Lista auxiliar para armazenar os índices a serem removidos

        for i in range(len(ar)):
            if i == 0: continue         # Evita que ocorra erro de lista out of bounds
            if ar[i] > ar[i-1]:
                morreu = True
                indices_morreu.append(i)


        for x in reversed(indices_morreu):
            ar.pop(x)
        n += 1
    return n

# Fim da função

# Começo do corpo principal do código

ar_count = int(input("Insira o número de elementos do vetor:"))
ar = [0] * ar_count

print("Insira os elementos do vetor (separados por espaços):")
ar_aux  = list(map(int, input().rstrip().split()))

if len(ar_aux) == ar_count:
    for i in range(len(ar)):
        ar[i] = ar_aux[i]
else:
    sys.exit("Erro! O número de elementos iseridos é diferente do tamanho do vetor")

result = numeroDeDias(ar)

print("Número de dias até que as plantas parem de morrer:")
print(result)
