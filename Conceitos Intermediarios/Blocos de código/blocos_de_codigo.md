# Blocos de código


## Identidade e operador is

Pergunta rápida: estas listas são iguais?
````python
lista_a = [1, 2, 3, 4, 5]
lista_b = [1, 2, 3, 4, 5]
````

Do ponto de vista de Python, elas são sim iguais…
````python
lista_a = [1, 2, 3, 4, 5]
lista_b = [1, 2, 3, 4, 5]
print(lista_a == lista_b)
# output: True
````

Porém elas não são a mesma lista: no momento em que altero a lista_a, elas deixam de ser
iguais:

````python
lista_a = [1, 2, 3, 4, 5]
lista_b = [1, 2, 3, 4, 5]
lista_a.append(6)
print(lista_a == lista_b)
# output: False
````


### Operador is

No exemplo anterior, cada lista é considerada um objeto próprio. Ou seja, a identidade da lista_a
não é a mesma que a identidade da lista_b, ainda que ambas possam possuir exatamente os
mesmos valores.
Podemos testar a identidade em Python com o operador is. Note que as duas listas nunca terão a
mesma identidade:
````python
lista_a = [1, 2, 3, 4, 5]
lista_b = [1, 2, 3, 4, 5]
print(lista_a is lista_b)
# output: False
````

Uma forma de entendermos identidade em Python é pensando em bolos. Dois bolos podem ser
exatamente idênticos, porém não são o mesmo objeto: quando eu corto um dos bolos, o outro não é
automaticamente cortado também!

````python
bolo1 = {
    'sabor': 'chocolate',
    'tamanho': 'grande',
    'preço': 50,
}

bolo2 = {
    'sabor': 'chocolate',
    'tamanho': 'grande',
    'preço': 50,
}

print(bolo1 == bolo2)
# output: True
print(bolo1 is bolo2)
# output: False
bolo1['preço'] = 80
print(bolo1 == bolo2)
# output: False
print(bolo1 is bolo2)
# output: False


````