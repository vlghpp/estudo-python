'''
Desafio 02

Crie uma compreensão de dicionarios a partir de uma lista de palavras.
 No dicionario resultante, cada chave é a palavra em letras minusculas, e cada valor é
 associado é o numero de caracteres da palavra, sem contar espaços em branco

Exemplo:

palavras = ["Olá", "Python", "Henrique", "Asimov"]

dict_caracteres = {
    "olá": 3,
    "python": 6,
    "henrique": 8,
    "asimov": 6
}
'''

palavras = ["Olá", "Python", "Henrique", "Asimov"]

dict_caracteres = {k.lower(): len(k) for k in palavras}


print(dict_caracteres)