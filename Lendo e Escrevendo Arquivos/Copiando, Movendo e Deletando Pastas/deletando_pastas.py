from pathlib import Path
import shutil

path_file = Path(__file__).parent
path_remove = path_file / 'create_dir_mkdir'
path_remove.rmdir()