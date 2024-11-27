import re
import datetime
'''
Desafio 01
Crie uma função chamada ler_datas, que recebe um texto qualquer e extrai todas as datas que
estejam escritas no formato DD/MM/AAAA (como objetos datetime). Use o texto abaixo como
exemplo:
texto = """
A reunião está marcada para o dia 15/03/2023.
Lembre-se de entregar o relatório até 28/02/2023.
O evento acontecerá em 10/04/2023 no auditório principal.
"""



'''


texto = """
A reunião está marcada para o dia 15/03/2023.
Lembre-se de entregar o relatório até 28/02/2023.
O evento acontecerá em 10/04/2023 no auditório principal.
"""


def ler_datas(texto):
    padrao_data = '[0-9]{2}/[0-9]{2}/[0-9]{4}'
    todas_datas = re.findall(padrao_data, texto)
    datas = []
    for data in todas_datas:
        datas.append(datetime.datetime.strptime(data, '%d/%m/%Y'))

    return datas

print(list(ler_datas(texto)))