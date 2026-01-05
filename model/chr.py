import pygame

class Entity:
    def __init__(self, name: str, hp: int = 0, lv: int = 1, x=0, y=0):
        self.name = name
        self.hp = hp
        self.lv = lv
        # O rect guarda o x e o y automaticamente
        self.rect = pygame.Rect(x, y, 50, 50) 
        self.color = (255, 255, 255) # Cor padrão branca

        self.debug = False

    def draw(self, surface):
        # Usa a cor da instância e o rect da instância
        pygame.draw.rect(surface, self.color, self.rect)

# Adicione (Entity) para herdar as propriedades
class Player(Entity):
    def __init__(self, name: str, hp: int = 0, lv: int = 1, x=0, y=0):
        super().__init__(name, hp, lv, x, y)
        self.color = (0, 0, 255) # Player será azul
        self.vel = 5 # Velocidade que faltava definir

    def Walk(self):
        t = pygame.key.get_pressed()
        # No Pygame, mexemos no self.rect.x ou self.rect.y
        if t[pygame.K_w] or t[pygame.K_UP]:
            self.rect.y -= self.vel
        if t[pygame.K_s] or t[pygame.K_DOWN]:
            self.rect.y += self.vel
        if t[pygame.K_a] or t[pygame.K_LEFT]:
            self.rect.x -= self.vel
        if t[pygame.K_d] or t[pygame.K_RIGHT]:
            self.rect.x += self.vel
    
    def Interact(self):
        t = pygame.key.get_just_pressed()
        if t[pygame.K_KP_ENTER] or t[pygame.K_e]:
            print('Interagio')

# Adicione (Entity) aqui também
class NPC(Entity):
    def __init__(self, name: str, hp: int = 0, lv: int = 1, x=0, y=0):
        super().__init__(name, hp, lv, x, y)
        self.color = (0, 255, 0) # NPC será verde