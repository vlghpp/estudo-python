# Lendo e Escrevendo Json

Json é um formato de dados muito utilizado para armazenamento e, principalmente, envio de dados. Grande maioria das API utilizadas na internet utilizarão JSons como formato padrão para armazenamento de dados.

Json significa JavaScript Object Notation e, apesar de ter começado com JavaScript, hoje é uma formatação independente e todas as linguagens passaram a utilizá-lo de alguma forma.

É muito utilizado para arquivos de configuração, por ter um formato fácil de parsear e de entender.

Você perceberá que o Json é muito similar a um dicionário em Python, o que já nos dá uma 
familiaridade com o tipo de dado.

## Lendo e Escrevendo da memória

Digamos que recebemos um arquivo Json através de uma API. Para começar a utilizá-lo e manipulá-lo em Python, a melhor forma e decodificando ele utilizando o módulo json da biblioteca padrão. Ele transformará nosso arquivo json (que para o Python é lido como um string) para um dicionário, bem mais fácil de ser trabalhado. A leitura se daria da seguinte forma:

```python
import json

data_json = '''
{
  "assinantes" : [
    {
      "nome": "Adriano Soares",
      "telefone": "51 99999999",
      "email": "adriano@email.com",
      "em_dia": true
    },
    {
      "nome": "Juliano faccioni",
      "telefone": "51 99999999",
      "email": "juliano@email.com",
      "em_dia": false
    }
    ],
  "data_extração": "2023/08/22"
}
'''

data = json.loads(data_json)

```

Já para retornarmos ao formato Json, caso queiramos reenviar essa informação através de uma API, por exemplo. Podemos fazer da seguinte forma:

```python

data_json = json.dumps(data)
print(data_json)

```

Podemos utilizar o argumento indent para indentá-lo de uma forma que se torne mais fácil de ler:

```python

data_json = json.dumps(data, indent=2)
print(data_json)

```
## Lendo e escrevendo arquivos Json

Abrimos o arquivo com a função with da mesma forma que trabalhamos arquivos texto.

```python
import json

with open('config.json') as f:
	data = json.load(f)

print(data)
print(type(data))

```

Para salvar o arquivo novamente em json, a seguinte forma é utilizada:

```python

with open('config_copia.json') as f:
	json.dump(data, f, indent=2)

print(data)
print(type(data))

```
