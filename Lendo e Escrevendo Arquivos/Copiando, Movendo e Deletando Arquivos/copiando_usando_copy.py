from pathlib import Path
import shutil

# Copiando arquivo com copy

current_dir = Path(__file__).parent
path_file = current_dir / 'text_copy.txt'
path_destination_file = current_dir / 'diretorio02' #Passa apenas o diretório da onde quer que ele copie

shutil.copy(path_file, path_destination_file)