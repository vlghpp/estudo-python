from pathlib import Path
import shutil


path_file = Path(__file__).parent
path_destination_file = path_file / 'create_dir_mkdir' / 'create_child'
shutil.copytree(path_file / 'create_dir_mkdir', path_file / 'create_test' / 'create_child')