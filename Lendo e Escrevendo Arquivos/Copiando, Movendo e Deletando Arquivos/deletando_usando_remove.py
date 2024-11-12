from pathlib import Path
import shutil
import os

# Primeiro faço uma cópia do arquivo para diretorio03 (Treino)
current_dir = Path(__file__).parent
path_file = current_dir / 'text.txt'
path_destination_file = current_dir / 'diretorio03' / 'copy_text.txt'
shutil.copyfile(path_file, path_destination_file)


# Agora removo com o os.remove(caminho do aquivo)
# Verificando antes se o arquivo existe, caso exista ele apaga
if path_destination_file.exists():
    os.remove(path_destination_file)



