from pathlib import Path
import shutil



# Copiando arquivo com copyfile

current_dir = Path(__file__).parent
path_file = current_dir / 'text.txt'
path_destination_file = current_dir / 'diretorio01'

shutil.move(path_file, path_destination_file)




