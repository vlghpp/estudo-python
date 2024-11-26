from pathlib import Path
import pandas as pd


caminho_atual = Path(__file__).parent

caminho_planilha = caminho_atual / "planilhas" / "clientes.xlsx"

if not (caminho_atual / "exercicios_separa_planilhas").exists():
    (caminho_atual / "exercicios_separa_planilhas").mkdir()

planilha_clientes: dict = pd.read_excel(caminho_planilha, sheet_name=None)


for key, value in planilha_clientes.items():
    open(caminho_atual / "exercicios_separa_planilhas" / f"{key}.xlsx", mode="w")
    value.to_excel(caminho_atual / "exercicios_separa_planilhas" / f"{key}.xlsx")
    caminho_arquivo_xlsx = pd.read_excel(caminho_atual / "exercicios_separa_planilhas" / f"{key}.xlsx")
    print()
    print(key, ": ", caminho_arquivo_xlsx.head(10))





