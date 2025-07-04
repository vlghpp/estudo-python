# 19. Lendo e Escrevendo Arquivos XML

XML são similares a html. Os arquivos são estruturados a partir de tags que contem os dados armazenados. Segue abaixo um exemplo de arquivo xml.

```xml
<?xml version="1.0"?>
<catalogo>
   <livro id="bk101">
      <autor>Gambardella, Matthew</autor>
      <titulo>XML Developer's Guide</titulo>
      <genero>Computer</genero>
      <preco>44.95</preco>
      <data_publicacao>2000-10-01</data_publicacao>
      <descricao>An in-depth look at creating applications 
      with XML.</descricao>
   </livro>
   <livro id="bk102">
      <autor>Ralls, Kim</autor>
      <titulo>Midnight Rain</titulo>
      <genero>Fantasy</genero>
      <preco>5.95</preco>
      <data_publicacao>2000-12-16</data_publicacao>
      <descricao>A former architect battles corporate zombies, 
      an evil sorceress, and her own childhood to become queen 
      of the world.</descricao>
   </livro>
</catalogo>
```

Arquivos xml são ainda mais poderosos que json, e formam a estrutura de grande parte dos sites. Muito do armazenamento de dados da web se baseia em arquivos xml ou similares. Por isso é importante já termos uma primeira visualização do que se trata esse dado, como podemos fazer manipulações simples nele e como escrevê-los novamente.

Essa apresentação será introdutória, até por ser uma estrutura de dados mais complexa e, consequentemente, o tratamento desse dado em Python é mais complexo.

Segue a forma de ler arquivos

```python
import xml.dom.minidom
from pathlib import Path

pasta_atual = Path(__file__).parent
domtree = xml.dom.minidom.parse( 'livros.xml')

group = domtree.documentElement
livros = group.getElementsByTagName('livro')

for livro in livros:
    print(livro.getElementsByTagName('autor')[0].childNodes[0].nodeValue)
```


No caso, utilizamos `xml.dom` para abrir o arquivo xml. O que ele faz a transformação do arquivo em elementos de DOM. Caso você não conheça, DOM é uma representação padrão de dados e compõe a estrutura e conteúdo de um documento Web. Através dele, podemos tanto representar arquivos HTML quanto XML.

Para aqueles que estão acostumado com DOM e programação em JavaScript, deve ter notado as familiaridades das funções que utilizamos. O método getElementsByTagName é padrão dentro de DOM, e o nome utilizado dentro de Python é exatamente o mesmo.

Não vamos abordar extensivamente os métodos de DOM, até por que não é escopo desse curso.

Deixo aqui mais uma breve explicação externa de DOM: [clique aqui](https://developer.mozilla.org/pt-BR/docs/Web/API/Document_Object_Model/Introduction)


Para escrever arquivos xml é simples:

```python
with open(pasta_atual / 'xmls' / 'livros_copia.xml', 'w') as f:
    domtree.writexml(f)
``` 