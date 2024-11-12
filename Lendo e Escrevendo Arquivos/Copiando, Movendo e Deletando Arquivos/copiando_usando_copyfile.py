from pathlib import Path
import shutil



# Copiando arquivo com copyfile

current_dir = Path(__file__).parent
path_file = current_dir / 'text_copy.txt'
path_destination_file = current_dir / 'diretorio01' / 'text_copyfile.txt'

shutil.copyfile(path_file, path_destination_file)