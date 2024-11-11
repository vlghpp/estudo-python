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



## Path.cwd() -> corrent work directory

É utilizado para pegar o diretório atual. Tipo o `pwd` do Linux.

## Path.home()

É utilizado para encontrar a home do usuário.
