'''
Desafio 02
Crie uma função chamada diff_tempo, que aceita dois strings no formato HH:MM:SS e retorna a
diferença de tempo entre eles em um string de mesmo formato.

Exemplo de uso:

inicio = '08:34:21'
fim = '13:55:09'
diff = diff_tempo(inicio, fim)
print(diff)
# output:
# 5:20:48


'''
import datetime

inicio = '08:34:21'
fim = '13:55:09'

def diff_temp(inicio, fim):
    formato = '%H:%M:%S'
    inicio = datetime.datetime.strptime(inicio, formato)
    fim = datetime.datetime.strptime(fim, formato)
    diferenca = fim - inicio
    return str(diferenca)


print(diff_temp(inicio, fim))
