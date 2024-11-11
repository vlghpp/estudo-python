from pathlib import Path

caminho = Path('primeira_pasta/segunda_pasta')

for name in ["arquivo.txt", "arquivo2.txt", "arquivo3.txt"]:
    print(caminho / name)


