'''
Desafio 02
Imagine que você tem um restaurante com os seguintes itens no seu menu:

    comidas = {
        'Prato Feito': 24.90,
        'Salada': 21.90,
        'Strogonoff': 29.90,
        'Feijoada': 32.90,
    }

    bebidas = {
        'Água': 3.90,
        'Refrigerante': 5.90,
        'Suco': 7.90,
    }

Crie um novo dicionário chamado combos onde cada chave é uma tupla contendo (comida,
bebida), e o seu respectivo valor é o preço daquela combinação de comida e bebida.


'''
from itertools import combinations

comidas = {
'Prato Feito': 24.90,
'Salada': 21.90,
'Strogonoff': 29.90,
'Feijoada': 32.90,
}

bebidas = {
'Água': 3.90,
'Refrigerante': 5.90,
'Suco': 7.90,
}

combos = {}
for key_comidas, value_comidas in comidas.items():
    for key_bebidas, value_bebidas in bebidas.items():
        chave_combo = (key_comidas, key_bebidas)
        value_combo = value_bebidas + value_bebidas
        combos[chave_combo] = value_combo


print(combos)
