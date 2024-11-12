import os
from pathlib import Path

# Dica:  os.path.getsize(caminho)

def returns_size_of_directories(path: Path, deep):
    if deep == 1:
        print("\n=== Lista de Diretórios e Tamanhos ===\n")
        for document in path.glob('*'):
            print(f"| {document.name:<30} | {os.path.getsize(document) / 1000000:>5.0f} MB |")
        print("\n=====================================\n")



returns_size_of_directories(Path.home(), 1)