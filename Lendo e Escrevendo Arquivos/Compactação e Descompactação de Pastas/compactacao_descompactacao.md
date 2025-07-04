# Compactando e Descompactando Pastas

Podemos também utilizar o shutil para compactar e descompactar arquivos. Isso é uma funcionalidade interessante para caso queiramos criar um script para fazer backup de nossos dados por exemplo. Poderíamos semanalmente rodar, compactar os arquivos que nos são de interesse e enviá-lo para um disco externo por exemplo, mantendo nesse disco um cópia segura de nossos dados.

```python
import shutil
from pathlib import Path

pasta_atual = Path( __file__ ).parent
nome_do_arquivo = pasta_atual / 'compactado'
pasta_que_sera_compactada = pasta_atual


shutil.make_archive(nome_do_arquivo, 'zip', pasta_que_sera_compactada)
```

Para descompactar, podemos utilizar o seguinte método

```python
import shutil
from pathlib import Path

pasta_atual = Path( __file__ ).parent.absolute()
nome_do_arquivo = pasta_atual / 'compactado.zip'
pasta_que_sera_descompactada = pasta_atual / 'descompactado'


shutil.unpack_archive(nome_do_arquivo, pasta_que_sera_descompactada, 'zip')
```