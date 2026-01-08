import pygame

class Block:
    def __init__(
            self,name='Block',
            x:float=0,
            y:float=0,
            width:int=50,
            height:int=50,
            on_interact_callback=None,
            isSolid:bool=True,
            solidColor:tuple=(100,100,100)
            ):
        self.name = str(name)
        try:
            self.rect = pygame.Rect(x, y, width, height) 
        except:
            self.rect = pygame.Rect(1, 1, 10, 10) 
        # Agora o bloco tem corpo físico
        self.interact_action = on_interact_callback
        try:
            self.isSolid = isSolid
        except:
            self.isSolid = False

        self.color = solidColor # Cor cinza para blocos

    def isInteract(self):
        if self.interact_action:
            self.interact_action()
        else:
            pass
    
    def draw(self, surface):
        try:
            pygame.draw.rect(surface, self.color, self.rect)
        except:
            pygame.draw.rect(surface, (255,0,0), self.rect)






