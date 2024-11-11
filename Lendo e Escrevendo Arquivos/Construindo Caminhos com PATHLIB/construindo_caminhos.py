from pathlib import Path
print(f"ESTOU NESSE DIRETÓRIO: \n {Path.cwd()}")
print(__file__) # Retorna o caminho absoluto que o arquivo está
print(Path(__file__).parent) # Retorna o caminho absoluto até o diretório pai de onde está esse arquivo
print((Path(__file__).parent / 'primeira_pasta').exists()) #Cria apenas uma representação do caminho para 'primeira_pasta', mas não cria a pasta fisicamente.

caminho_arquivo = Path(__file__)

print(caminho_arquivo.anchor)