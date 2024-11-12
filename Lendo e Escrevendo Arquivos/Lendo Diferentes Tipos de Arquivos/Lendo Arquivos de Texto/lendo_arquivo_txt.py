from pathlib import Path

current_folder = Path(__file__).parent


'''
usando o .read() para ler o arquivo inteiro

with open(current_folder / 'compras.txt') as lista_compras:
   print(lista_compras.read())
'''


'''
usando o .readlines() para ler linha a linha, mas tendo que iterar para ler todas as linhas

with open(current_folder / 'compras.txt') as lista_compras:
    linha = lista_compras.readline()
    while linha != '':
        print(linha, end = '')
        linha = lista_compras.readline()
        
'''

'''
Usando o readlines() para retornar cada linha em um array

with open(current_folder / 'compras.txt') as lista_compras:
    print(lista_compras.readlines())
'''



#Refazendo a lista de compras com os itens que já tenho e reescrevendo só com os itens que não tenho


itens_ja_comprados = ['Abacaxi', 'Kiwi', 'Cenoura']

with open(current_folder / 'compras.txt', mode='r') as lista_compras:
    itens_lista = lista_compras.readlines()

with open(current_folder / 'lista_de_compras_atualizadas.txt', mode='w') as lista_atualizada:
    for item in itens_lista:
        if not item.replace('\n', '') in itens_ja_comprados:
            lista_atualizada.write(item)


