import pygame
import sys
import random
from pygame.locals import *
 
pygame.init()
 
# Predefined some colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (99, 99, 99)

# storing attributes
HEIGHT = 768
WIDTH = 1366
FPS = 60
 
# storing fonts
HP_FONT = pygame.freetype.Font("NotoSans-Regular.ttf", 18)
ACTION_FONT = pygame.freetype.Font("NotoSans-Regular.ttf", 35)

# defining some stuff
FramePerSec = pygame.time.Clock()
FramePerSec.tick(FPS) 
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Backshot Roulette")

# defining game logic stuff
round_hp = random.randint(2, 4)
round_types = ["live", "blank"]

# the player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.hp = round_hp
 
    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.top > 0:
            if pressed_keys[K_UP]:
                self.rect.move_ip(0, -5)
        if self.rect.bottom < HEIGHT:
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0,5)
         
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
 
    def draw(self, surface):
        text_surface, rect = HP_FONT.render(f"vida atual: {self.hp}", WHITE)
        surface.blit(text_surface, (0, 0))

# the dealer class
class Dealer(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Dealer.png")
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, 160)
        self.hp = round_hp
        self.hitbox = Rect((self.rect.center[0] - 130,self.rect.center[1] - 100),(270,250))
    def update(self):
        pass

    def draw(self, surface):
        # player collide message
        if self.hitbox.collidepoint(pygame.mouse.get_pos()):
            text_surface , rect = ACTION_FONT.render("atirar no dealer", WHITE)
            surface.blit(text_surface,(WIDTH/2 - 105,HEIGHT/2 - 70))

        surface.blit(self.image, self.rect)
        text_surface, rect = HP_FONT.render(f"vida dealer: {self.hp}", WHITE)
        surface.blit(text_surface, (0, 20))
    
# the shotgun class
class Shotgun(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Shotgun.png")
        self.image = pygame.transform.scale_by(self.image, 0.7)
        self.image = pygame.transform.rotate(self.image, -43)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, 550)
        self.hitbox = Rect((self.rect.center[0] - 250,self.rect.center[1] - 60),(500,110))
    
    def update(self):
        pass

    def draw(self, surface):
        # player collide message
        if self.hitbox.collidepoint(pygame.mouse.get_pos()):
            text_surface , rect = ACTION_FONT.render("atirar em si mesmo", WHITE)
            surface.blit(text_surface,(WIDTH/2 - 130, HEIGHT - 130))
        
        surface.blit(self.image, self.rect)



# creating player, dealer and shotgun
player = Player()
dealer = Dealer()
shotgun = Shotgun()

# main game loop
while True:
    for event in pygame.event.get():
        pressed_keys = pygame.key.get_pressed()
        if event.type == QUIT or pressed_keys[K_ESCAPE]:
            pygame.quit()
            sys.exit()
    


    displaysurface.fill(GREY)
    shotgun.draw(displaysurface)
    player.draw(displaysurface)
    dealer.draw(displaysurface)


    pygame.display.update()
    FramePerSec.tick(FPS)

