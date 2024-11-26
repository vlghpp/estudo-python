
'''
Desafio 01

Converta o loop abaixo para uma compreensão de lista

valores = [30, 50, 100, 120]
triplos = []

for valor in valores:
    triplos.append(valor * 3)

print(triplos)

'''

valores = [30, 50, 100, 120]
triplos = [valor*3 for valor in valores]
print(triplos)