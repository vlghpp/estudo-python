from pathlib import Path
import shutil


path_file = Path(__file__).parent
path_destination_file = path_file / 'create_test'
path_destination_file.mkdir()
