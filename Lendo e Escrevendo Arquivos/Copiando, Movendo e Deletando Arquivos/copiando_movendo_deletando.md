# Usando PATHLIB e SHUTIL para copiar, mover e deletar arquivos
Para utilizar da biblioteca basta importar: `form pathlib import Path` e instaciar a classe passando o caminho como parametro


## Copiando Arquivos (copyfile, copy)

### shutil.copyfile(src, destino)
O copyfile copia um arquivo passando o caminho atual dele e passando o destino para onde quer enviar a cópia. Não mantém as restrições de arquivo, exemplo: apenas leitura, modo editor, etc.

````python

from pathlib import Path
import shutil

# Copiando arquivo com copyfile

current_dir = Path(__file__).parent
path_file = current_dir / 'text_copy.txt'
path_destination_file = current_dir / 'diretorio01' / 'text_copyfile.txt'

shutil.copyfile(path_file, path_destination_file)
````

### shutil.copy(src, destino)
O copy assim como o copyfile faz a cópia de um arquivo do caminho atual dele para um destino. Mas existem algumas diferenças tais como:
 - O copy mantém as restrições de arquivo (editar, apenas leitura)
 - O copy não passa o nome do arquivo no destino, apenas o diretório onde que armazena-lo

````python
from pathlib import Path
import shutil

# Copiando arquivo com copy

current_dir = Path(__file__).parent
path_file = current_dir / 'text_copy.txt'
path_destination_file = current_dir / 'diretorio02' #Passa apenas o diretório da onde quer que ele copie

shutil.copy(path_file, path_destination_file)
````


## Movendo Arquivos (move)


### shutil.move(src, destino)
Assim como os métodos de copiar, o shutil.move() serve para mover um arquivo para um diretório.

````python

from pathlib import Path
import shutil

current_dir = Path(__file__).parent
path_file = current_dir / 'text.txt'
path_destination_file = current_dir / 'diretorio01'

shutil.move(path_file, path_destination_file)
````



## Deletando arquivos - os.remove()
Para deletar é simples e fácil, só dar os.remove() mas é importante verificar se o arquivo existe antes de remover para não estourar uma exceção
````python

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
````

