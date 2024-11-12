from pathlib import Path
import shutil


path_file = Path(__file__).parent
folder_compress = path_file
name_archive = path_file / 'compactado'
shutil.make_archive(name_archive, 'zip', folder_compress)