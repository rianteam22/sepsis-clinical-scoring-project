# clean_data.py
import pandas as pd

def clean_data(data):
    # Preenchendo valores ausentes com zeros ou o valor mais frequente, conforme necessário
    data.fillna(0, inplace=True)

    # Normalizando colunas específicas (conversão de unidades ou tipos de dados)
    data['temperature'] = pd.to_numeric(data['temperature'], errors='coerce')
    data['map'] = pd.to_numeric(data['map'], errors='coerce')
    
    # Removendo ou tratando linhas com dados inválidos
    data.dropna(subset=['temperature', 'map', 'heart_rate'], inplace=True)

    return data
