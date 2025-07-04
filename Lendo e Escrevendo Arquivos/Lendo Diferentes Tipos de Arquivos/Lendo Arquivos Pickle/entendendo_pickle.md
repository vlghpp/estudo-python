# Lendo e Escrevendo Arquivos Pickle

Pickle é uma forma muito utilizada para serializar objetos de Python. O que queremos falar como isso?

Ocorre em Python de às vezes queremos salvar objetos no nosso disco para uso posterior. Por exemplo, criamos um modelo de Machine Learning e demorou diversas horar para o processador conseguir treinar o modelo. Digamos que eu não queira perder o trabalho já feito, para isso podemos salvar nosso modelo treinado em um arquivo pickle. Ele salvará o objeto exatamente no estado atual que ele se encontra naquele momento. Isso pode ser muito útil e poupar bastante tempo.

Com pickle, podemos salvar objetos simples como listas e dicionários. Para isso, utilizamos o módulo pickle da biblioteca padão de Python:


```python
import pickle

minha_lista = [0, 1, 2]
meu_dict = {'a': 1, 'b': 2, 'c': 3}

with open('minha_lista.pickle', 'wb') as f:
	pickle.dump(minha_lista, f)

with open('meu_dict.pickle', 'wb') as f:
	pickle.dump(meu_dict, f)

```

O formato é similar a quando aprendemos a ler e escrever arquivos de texto. Isso por que pickle não passa de uma forma de escrever em bytes variáveis e objetos que estão namemória ram. Por isso, o modo utilizado é `wb`. Lembrando da aula de textos, o `w` é referente a escrita de um novo arquivo, já o `b` é referente a bytes, para informar que esse arquivo deve ser escrito como bytes, formando no final um arquivo que não é legível.

Para ler esses arquivos, o processo acaba sendo bem simples:

```python
import pickle

with open('minha_lista.pickle', 'rb') as f:
	minha_lista = pickle.load(f)

with open('meu_dict.pickle', 'rb') as f:
	meu_dict = pickle.load(f)

```

Podemos explorar pickle com tipos de dados mais complexos como dataframes ou classes em geral.


```python
import pickle

class Pessoa:
	def __init__(self, nome, idade):
		self.nome = nome
		self.idade = idade
	def quem_sou_eu(self):
		print(f'Eu sou {self.name} e tenho {self.idade} anos')

obj_pessoa = Pessoa('Carlos', 31)
obj_pessoa.quem_sou_eu()

with open('obj_pessoa.pickle', 'wb') as f:
	pickle.dump(obj_pessoa, f)

```


```python
import pickle

with open('obj_pessoa.pickle', 'wb') as f:
	obj_pessoa = pickle.load(f)

obj_pessoa.quem_sou_eu()

```


