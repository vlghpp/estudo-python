# Usando PATHLIB para acessar caminhos

Para utilizar da biblioteca basta importar: `form pathlib import Path` e instaciar a classe passando o caminho como parametro



## Caminhos relativos e Caminhos Absolutos

- **_Caminhos relativos_** são aqueles que estão relativamente ao diretório atual, por exemplo: para acessar esse README.md você precisa ter acesso ao Construindo Caminhos Com PATHLIB/primeira_pasta.<br>
Ou seja, você precisa estar dentro de `primeira_pasta`, então tudo que estiver como filho dessa classe a partir dela é acessável, mas o que vem antes não é.
```
    Exemplo: Lendo e Escrevendo Arquivos\Construindo Caminhos com PATHLIB
```

- **_Caminhos absolutos_** é o endereço completo de um arquivo ou diretório, começando pela raiz do sistema, o que permite localizá-lo de qualquer lugar no sistema. Ele especifica todo o caminho desde a pasta raiz até o destino

```
    Exemplo de Caminho Absoluto:
       Em Windows: C:\Users\Henrique\Documentos\arquivo.txt
       Em Linux/Mac: /home/henrique/documentos/arquivo.txt
```
Esse tipo de caminho é útil quando queremos garantir que o arquivo seja acessado, independentemente da pasta em que estamos atualmente.


## Como transformar um caminho relativo num caminho absoluto?
Utilizando o método `__file__` do próprio python, ele retorna o caminho absoluto do arquivo em que está sendo executado.
Em conjuto com o método `.parent` para retornar o diretório que está sendo armazenado esse arquivo (`__file__`). Veja abaixo:

````python
from pathlib import Path
print(__file__) # Retorna o caminho absoluto que o arquivo está 
print(Path(__file__).parent) # Retorna o caminho absoluto até o diretório pai de onde está esse arquivo
print(Path(__file__).parent / 'primeira_pasta') #Faz o caminho do diretório pai do arquivo 
````

## Validar informações sobre caminhos path


### Path.cwd().**_is_absolute()_**
É utilizado para verificar se um caminho (Path) é absoluto ou não.


### (Path).**_exists()_**
É utilizado para verificar se o caminho ou diretório existe. (JÁ É UMA FUNÇÃO DO PYTHON, NÃO É DO PATHLIB)

### Path(caminho).**_is_file()_**
É utilizado para verificar se o caminho passado é um arquivo.

### Path(caminho).**_is_dir()_**
É utilziado para verificar se o caminho passado é um diretório

## Retornar informações específicas de um caminho passado

## Path.cwd() -> corrent work directory
É utilizado para pegar o diretório atual. Tipo o `pwd` do Linux.

### Path.home()
É utilizado para encontrar a home do usuário.

### Path(__file__).anchor 
É utilizado para pegar o C:\, ou seja, o inicio do caminho, em que hd ele está armazenado.

### Path(__file__).parent
É utilizado para retornar o diretório pai do arquivo onde está sendo executado.

### Path(__file__).parents[indice]
É utilizado para retornar a quantidade de diretórios pais que foi passado pelo indice e evitar o: `Path(__file__).parent.parent.parent.parent` até onde queria chegar.

### Path(__file__).name
É utilizado para retornar o nome do arquivo que está sendo executado.

### Path(__file__).stem 
É utilizado para retornar o nome do arquivo sem a extensão dele (.py)

### Path(__file__).suffix
É utilizado para retornar o sufixo do arquivo, ou seja, a extensão



## Listar arquivos dentro de pastas

### list(Path(caminho).glob('*'))
É utilizado para fazer um ls dentro do caminho desejado e retornar uma lista deles já com o caminho absoluto dos mesmos.

````python

from pathlib import Path

print(Path.cwd().glob('*')) # Retorna todos os arquivos e pastas dentro do caminho, mas não retorna o conteúdo de pastas aninhadas
print(Path.cwd().glob('*.py')) # Retorna todos os arquivos.py   
````

### list(Path(caminho).glob('**/*.txt'))
É utilizado para cobrir o que o ultimo comando não cobre. Ou seja, lista tudo dentro de pastas dentro de pastas.

`````python
from pathlib import Path

print(Path.cwd().glob('**/*')) # Retorna todos os arquivos e pastas dentro do caminho até o fim (mesmo que tenha pastas dentro de pastas)
print(Path.cwd().glob('**/*.py')) # Retorna todos os arquivos.py que tem no diretório até seu último filho 
`````
