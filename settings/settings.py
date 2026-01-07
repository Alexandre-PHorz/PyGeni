import json
import os

# Pega o caminho da pasta onde este arquivo (settings.py) está
BASE_DIR = os.path.dirname(__file__)

def sett(filename='setting.json') -> dict:
    # Cria o caminho completo: settings/setting.json
    path = os.path.join(BASE_DIR, filename)
    
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Erro ao carregar configurações: {e}")
        return {} # Retorna um dict vazio em vez de False para evitar erros de tipo