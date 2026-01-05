import pygame
from model.chr import *
from model.block import *



class PyGeni:
    def __init__(self,title='My Game',geometry='768x768'):
        self._config = {
            'GEOMETRY':geometry,
            'TITLE':title
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

    def run(self):
        rodando = True
        clock = pygame.time.Clock()
        while rodando:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    rodando = False

            self._display.fill((30, 30, 30))

            # Dentro do while rodando da classe Game:
            for obj in self.instances:
                if isinstance(obj, Player): # Se o objeto for o Player, ele pode andar
                    obj.Walk()
                    obj.Interact()
                
                if hasattr(obj, 'draw'):
                    obj.draw(self._display)

            pygame.display.flip()
            clock.tick(60) # Mantém a 60 FPS
        pygame.quit()

    