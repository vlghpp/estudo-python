from pathlib import Path
import shutil



path_file = Path(__file__).parent
name_archive = path_file / 'compactado.zip'
folder_descompress = path_file / 'descompactado'

shutil.unpack_archive(name_archive, folder_descompress, 'zip')