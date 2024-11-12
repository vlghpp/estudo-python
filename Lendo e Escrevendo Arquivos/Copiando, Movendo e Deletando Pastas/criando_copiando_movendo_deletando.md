# Usando PATHLIB e SHUTIL para copiar, mover e deletar pastas
Para utilizar da biblioteca basta importar: `form pathlib import Path` e instaciar a classe passando o caminho como parametro


## Criando Pastas

### caminho.mkdir()
Apenas passando o local onde quer criar e dando mkdir ele cria uma pasta

**`FLAGS IMPORTANTES:`**
- parents = True - Permite que seja possivel criar pastas com conteudos dentro, exemplo: pastas dentro de pastas.
- exists_ok = True - Permite com que o script identifique se a pasta já existe, se sim, não vai estourar nenhum erro e não vai criar uma pasta nova. Se não, vai criar no local pedido.

````python
from pathlib import Path

path_file = Path(__file__).parent
path_destination_file = path_file / 'create_dir_mkdir'
path_destination_file.mkdir()

````

## Movendo Pastas

### shutil.copytree()
É utilizado passando a origem da(s) pasta que vai ser movidas e o destino das mesmas.

````python

from pathlib import Path
import shutil

path_file = Path(__file__).parent
path_destination_file = path_file / 'create_dir_mkdir' / 'create_child'
shutil.copytree(path_file / 'create_dir_mkdir', path_file / 'create_test' / 'create_child')

````



## Deletando Pastas


### caminho.rmdir()
É utilizado para remover uma pasta, seja uma pasta pai ou uma filho. Apenas mostrando o caminho e dando .rmdir()

- `DELETA APENAS PASTAS VARIAS`

````python
from pathlib import Path
import shutil

path_file = Path(__file__).parent
path_remove = path_file / 'create_dir_mkdir'
path_remove.rmdir()

````

### shutil.removetree()
É utilizado para remover uma pasta que tem algum conteúdo, diferente do .rmdir(). Apenas passando o caminho da pasta.

````python
from pathlib import Path
import shutil

path_file = Path(__file__).parent
path_remove = path_file / 'create_dir_mkdir'
shutil.rmtree(path_remove)

````