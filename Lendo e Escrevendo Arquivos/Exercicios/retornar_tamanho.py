import os
from pathlib import Path

# Dica:  os.path.getsize(caminho)

def returns_size_of_directories(path:Path, deep):
    for document in path.glob('**/*'):
        print(f"{document.name} is {os.path.getsize(document)/1000000:.0f}mb in size")




returns_size_of_directories(Path.home(), 1)