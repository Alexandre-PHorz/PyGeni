import pygame

class Entity:
    def __init__(self, name: str, hp: int = 0, lv: int = 1, x=0, y=0):
        self.name = name
        self.hp = hp
        self.MHP = hp
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
    def __init__(self, name: str, hp: int = 100, lv: int = 1, x=0, y=0, speed = 4):
        super().__init__(name, hp, lv, x, y)
        self.color = (0, 0, 255) # Player será azul
        self.vel = speed # Velocidade que faltava definir
        self.pos = pygame.math.Vector2(self.rect.center)

    def Walk(self, walls):
        t = pygame.key.get_pressed()
        direction = pygame.math.Vector2(0, 0)

        if t[pygame.K_w] or t[pygame.K_UP]: direction.y -= 1
        if t[pygame.K_s] or t[pygame.K_DOWN]: direction.y += 1
        if t[pygame.K_a] or t[pygame.K_LEFT]: direction.x -= 1
        if t[pygame.K_d] or t[pygame.K_RIGHT]: direction.x += 1

        if direction.length() > 0:
            direction = direction.normalize()

        # MOVIMENTO E COLISÃO EIXO X
        self.pos.x += direction.x * self.vel
        self.rect.centerx = round(self.pos.x)
        for wall in walls:
            if wall.isSolid and self.rect.colliderect(wall.rect):
                if direction.x > 0: self.rect.right = wall.rect.left
                if direction.x < 0: self.rect.left = wall.rect.right
                self.pos.x = self.rect.centerx

        # MOVIMENTO E COLISÃO EIXO Y
        self.pos.y += direction.y * self.vel
        self.rect.centery = round(self.pos.y)
        for wall in walls:
            if wall.isSolid and self.rect.colliderect(wall.rect):
                if direction.y > 0: self.rect.bottom = wall.rect.top
                if direction.y < 0: self.rect.top = wall.rect.bottom
                self.pos.y = self.rect.centery
        
    
    def Interact(self, reach=50):
        # 'self' aqui é o Player
        pos_player = pygame.math.Vector2(self.rect.center)
        
        for obj in self.game.instances: # Acessa a lista de instâncias do framework
            if obj == self: continue # Pula o próprio player
            
            # 1. Checa se o objeto tem a função 'isInteract'
            if hasattr(obj, 'isInteract'):
                t = pygame.key.get_pressed()
                # 2. Calcula a distância entre o centro do player e o objeto
                pos_obj = pygame.math.Vector2(obj.rect.center)
                distancia = pos_player.distance_to(pos_obj)
                
                # 3. Se estiver dentro do raio (reach)
                if distancia <= reach and t[pygame.K_e]:
                    obj.isInteract() # Executa a função do objeto

# Adicione (Entity) aqui também
class NPC(Entity):
    def __init__(self, name: str, hp: int = 0, lv: int = 1, x=0, y=0):
        super().__init__(name, hp, lv, x, y)
        self.color = (0, 255, 0) # NPC será verde