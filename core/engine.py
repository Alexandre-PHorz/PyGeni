import pygame
from settings import configs
from model.chr import *
from model.block import *

class PyGeni:
    def __init__(self, title=None, geometry=None):
        # Se não passar argumentos, usa o que está no JSON
        self._config = {
            'TITLE': title if title else configs.display.title,
            'GEOMETRY': geometry if geometry else configs.display.resolution
        }
        
        self._display = None
        self.instances = []
        self.solids = []

        # Puxa o objeto que criamos no settings/__init__.py
        self.display = configs.display 

    def start(self):
        pygame.init()
        # Usa a largura e altura direto do objeto display que você criou!
        res = (self.display.x, self.display.y)
        
        # Ativa VSync se estiver no JSON
        vsync_on = 1 if getattr(configs.display, 'vsync', False) else 0
        
        self._display = pygame.display.set_mode(res, pygame.SCALED, vsync=vsync_on)
        pygame.display.set_caption(self._config['TITLE'])

    def AddInstance(self, instance):
        self.instances.append(instance)
        # Verifica se o objeto é um bloco sólido para a lista de colisão
        if hasattr(instance, 'isSolid') and instance.isSolid:
            self.solids.append(instance)

    def DestroyInstance(self, instance):
        if instance in self.instances: self.instances.remove(instance)
        if instance in self.solids: self.solids.remove(instance)

    def run(self, fps=60):
        rodando = True
        clock = pygame.time.Clock()
        
        while rodando:
            dt = clock.tick(fps) / 1000.0 

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    rodando = False

            self._display.fill((30, 30, 30))

            # Renderização e Lógica
            for obj in self.instances:
                # 1. Update genérico
                if hasattr(obj, 'update'):
                    obj.update(dt)
                
                # 2. Movimentação (passando os sólidos para colisão)
                if hasattr(obj, 'Walk'):
                    obj.Walk(self.solids)
                
                # 3. Desenho
                if hasattr(obj, 'draw'):
                    obj.draw(self._display)

            pygame.display.flip()

        pygame.quit()