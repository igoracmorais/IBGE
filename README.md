"""
# PNADcIBGE

Este pacote oferece ferramentas para manipular os microdados da PNAD Contínua disponibilizados pelo IBGE.

## Instalação

```bash
pip install pnadcibge
```

## Uso Básico

```python
from pnadcibge import download_pnadc, extract_zip, load_pnadc_txt, label_variables

# Baixar os microdados
zip_path = download_pnadc(2024, 1)

# Extrair os dados
extract_dir = extract_zip(zip_path, "data")

# Carregar os dados
df = load_pnadc_txt("data/PNADC_012024.txt", "data/Dicionario_PNADC_012024.txt")

# Rotular variáveis
label_dict = {"V2001": "Idade", "V2005": "Sexo"}
df = label_variables(df, label_dict)
```
"""
