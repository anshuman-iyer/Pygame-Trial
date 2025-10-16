import pygame

pygame.init()

running = True

## Standard Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Player Class Example")

#==============Player Class Definition===============

class Player:
    def __init__(self, x, y, width, height, speed):
        """Initializes the Player object."""
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = speed
        
        #===============Gravity Implementation===============
        self.vy = 0
        self.gravity = 0.01
        self.jump_strength = -2
        
        self.on_ground = False
        
    def groundCheck(self):
        
        if self.rect.bottom >= screen_rect.bottom:
            self.rect.bottom = screen_rect.bottom
            self.vy = 0 
            self.on_ground = True
            
        if self.rect.top < 0:
            self.rect.top = 0
            self.vy = 0
    
    def applyGravity(self):
        self.vy += self.gravity
        self.rect.y += self.vy
    
    def move(self, screen_rect):
        
        key = pygame.key.get_pressed()
        
        if key[pygame.K_a]:
            self.rect.x -= self.speed
        if key[pygame.K_d]:
            self.rect.x += self.speed
            
        if key[pygame.K_s]:
            self.rect.y += self.speed
        
        if key[pygame.K_SPACE or pygame.K_w] and self.on_ground:
            self.vy = self.jump_strength
            self.on_ground = False
        player.applyGravity()
        player.groundCheck()
        
        #===============Collision Check===============
        self.rect.clamp_ip(screen_rect)
            
    def draw(self, surface):
        
        pygame.draw.rect(surface, RED, self.rect)
    
    

player = Player(300, 250, 50, 50, 2)

screen_rect = screen.get_rect()

#===============Main Loop===============
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    
    player.move(screen_rect)

    screen.fill((0, 0, 0))
    
    player.draw(screen)
    
    pygame.display.update()
    
    
pygame.quit()