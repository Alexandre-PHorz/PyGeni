# settings/__init__.py
from .settings import sett

# Carrega os dados uma única vez
data = sett()

# Cria constantes ou objetos prontos para a engine
class Config:
    def __init__(self, d):
        for key, value in d.items():
            if isinstance(value, dict):
                setattr(self, key, Config(value))
            else:
                setattr(self, key, value)
        
        # Se for a parte de display, adiciona suporte a .x e .y
        if 'resolution' in d:
            res = d['resolution'].split('x')
            self.x = int(res[0])
            self.y = int(res[1])

# Exporta o objeto de configuração pronto
configs = Config(data)