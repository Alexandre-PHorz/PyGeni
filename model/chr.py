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
        
        # 1. Criamos um vetor de direção (x, y)
        direction = pygame.math.Vector2(0, 0)
        
        # 2. Capturamos o input
        if t[pygame.K_w] or t[pygame.K_UP]:
            direction.y -= 1
        if t[pygame.K_s] or t[pygame.K_DOWN]:
            direction.y += 1
        if t[pygame.K_a] or t[pygame.K_LEFT]:
            direction.x -= 1
        if t[pygame.K_d] or t[pygame.K_RIGHT]:
            direction.x += 1

        # 3. O SEGREDO: Normalização
        # Se o comprimento do vetor for maior que zero (ele está se movendo)
        if direction.length() > 0:
            # Faz o vetor ter tamanho 1, mantendo a direção
            direction = direction.normalize()
            
        # 4. Aplicamos a velocidade
        # Agora, na diagonal, o vetor será algo como (0.7, 0.7)
        # (0.7 * vel) + (0.7 * vel) resultará em uma velocidade final de exatamente 'vel'
        self.rect.x += direction.x * self.vel
        self.rect.y += direction.y * self.vel
    
    def Interact(self, reach=50):
        # 'self' aqui é o Player
        pos_player = pygame.math.Vector2(self.rect.center)
        
        for obj in self.game.instances: # Acessa a lista de instâncias do framework
            if obj == self: continue # Pula o próprio player
            
            # 1. Checa se o objeto tem a função 'isInteract'
            if hasattr(obj, 'isInteract'):
                
                # 2. Calcula a distância entre o centro do player e o objeto
                pos_obj = pygame.math.Vector2(obj.rect.center)
                distancia = pos_player.distance_to(pos_obj)
                
                # 3. Se estiver dentro do raio (reach)
                if distancia <= reach:
                    obj.isInteract() # Executa a função do objeto

# Adicione (Entity) aqui também
class NPC(Entity):
    def __init__(self, name: str, hp: int = 0, lv: int = 1, x=0, y=0):
        super().__init__(name, hp, lv, x, y)
        self.color = (0, 255, 0) # NPC será verde