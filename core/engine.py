import pygame
from model.chr import *
from model.block import *



class PyGeni:
    def __init__(self,title='My Game',geometry='768x768',tilesize='16x16',zoom='1'):
        self._config = {
            'GEOMETRY':geometry,
            'TITLE':title,
            'TILESIZE': tilesize,
            'ZOOM':zoom
        }
        self._display = None

        self.instances = []

    def start(self):
        pygame.init()
        self._display = pygame.display.set_mode(tuple(int(x) for x in self._config['GEOMETRY'].split('x')))
        pygame.display.set_caption(self._config['TITLE'])

    def AddInstance(self, instance):
        # Adiciona o objeto à nossa lista
        self.instances.append(instance)

    def DestroyInstance(self, instance):
        if instance in self.instances:
            self.instances.remove(instance)
            print(f"Instância de {getattr(instance, 'name', 'Objeto')} destruída.")

    def run(self,fps=60):
        rodando = True
        clock = pygame.time.Clock()
        
        while rodando:
            # 1. Delta Time (Importante para velocidade constante)
            dt = clock.tick(fps) / 1000.0 

            # 2. Captura de Eventos (Input)
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    rodando = False

            # 3. Limpeza da Tela
            self._display.fill((30, 30, 30))

            # 4. Lógica e Renderização Automática
            for obj in self.instances:
                # Se o objeto tiver lógica própria (como Walk), ele executa
                if hasattr(obj, 'update'):
                    obj.update(dt) # Passamos o delta time para o objeto
                
                # Se o objeto for o Player, podemos chamar os métodos específicos
                if hasattr(obj, 'Walk'):
                    obj.Walk()
                
                # Desenha o objeto na tela
                if hasattr(obj, 'draw'):
                    obj.draw(self._display)

            # 5. Atualização do Display
            pygame.display.flip()

        pygame.quit()

    