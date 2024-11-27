import itertools

l1 = [1, 2, 3]
l2 = ['a', 'b', 'c', 'd', 'e']


def retorna_intercalado(l1, l2):
    resultado = []
    for _, elemento in itertools.zip_longest(l1, l2):
        if _ is not None:
            resultado.append(_)
        if elemento is not None:
            resultado.append(elemento)

    print(resultado)


retorna_intercalado(l1, l2)