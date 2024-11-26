import json
from pathlib import Path
from xml.etree.ElementTree import indent

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

data = json.loads(data_json) # Converte uma váriavel local pra um JSON (load's') para local -  (load) para arquivos de fora

## Abrindo arquivos json:



caminho_atual = Path(__file__).parent

with open(caminho_atual / "Arquivo JSON" / "assinantes.json") as file:
    dado_json = json.load(file)
    print(type(dado_json), "\n")
    print(type(json.dumps(dado_json)))
