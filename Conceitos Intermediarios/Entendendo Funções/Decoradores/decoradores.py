def repetir_duas_vezes(func):
    def meu_pacote(*args, **kwargs):
        _ = func(*args, **kwargs)
        retorno = func(*args, **kwargs)
        return retorno
    return meu_pacote

@repetir_duas_vezes
def printar(nome):
    print(f"Olá, {nome}")


printar = repetir_duas_vezes(func=printar)

print(printar("henrique"))


