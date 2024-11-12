from pathlib import Path
import shutil


pasta_atual: Path = Path(__file__).parent
pasta_arquivos_desafios: Path = pasta_atual / 'arquivos_desafios'



for arquivo in pasta_arquivos_desafios.glob('*'):
    if arquivo.name.endswith('.csv'):
        pasta_csv = pasta_atual / 'organizada' / 'csv'
        pasta_csv.mkdir(exist_ok= True)
        shutil.move(arquivo, pasta_csv)
    elif arquivo.name.endswith('.pdf'):
        pasta_pdf = pasta_atual / 'organizada' / 'pdf'
        pasta_pdf.mkdir(exist_ok= True)
        shutil.move(arquivo, pasta_pdf)
    elif arquivo.name.endswith('.py'):
        pasta_py = pasta_atual / 'organizada' / 'py'
        pasta_py.mkdir(exist_ok=True)
        shutil.move(arquivo, pasta_py)
    elif arquivo.name.endswith('.txt'):
        pasta_txt = pasta_atual / 'organizada' / 'txt'
        pasta_txt.mkdir(exist_ok=True)
        shutil.move(arquivo, pasta_txt)
    elif arquivo.name.endswith('.json'):
        pasta_json = pasta_atual / 'organizada' / 'json'
        pasta_json.mkdir(exist_ok=True)
        shutil.move(arquivo, pasta_json)
    elif arquivo.name.endswith('.html'):
        pasta_html = pasta_atual / 'organizada' / 'html'
        pasta_html.mkdir(exist_ok=True)
        shutil.move(arquivo, pasta_html)
    elif arquivo.name.endswith('.xlsx'):
        pasta_xlsx = pasta_atual / 'organizada' / 'xlsx'
        pasta_xlsx.mkdir(exist_ok=True)
        shutil.move(arquivo, pasta_xlsx)


pasta_compactada = pasta_atual / 'backup'
pasta_compactada.mkdir()
nome_arquivo = pasta_atual / 'backup' / 'backup'
shutil.make_archive(nome_arquivo, 'zip', pasta_compactada)

try:
    pasta_arquivos_desafios.rmdir()
except OSError:
    print("A PASTA AINDA NÃO ESTÁ VAZIA!")