from __future__ import division, print_function, unicode_literals
 
import sys, os, pygame, pyglet, random
from pygame.locals import *
from pyglet.window import key
 
 
player = pygame.image.load('Ship1.png')
playerRect = player.get_rect()
 
tImg = pygame.image.load('tie.png')
tImgRect = tImg.get_rect()
#images for player and enemy ship
 
 
#Player class
class Player(pygame.sprite.Sprite):
    def __init__(self, *groups):
#placed in sprite groups 
        super(Player, self).__init__(*groups)
     
        self.image = player
    self.rect = playerRect
        self.rect.center = ((h *.8),(w * .6))
#declares position of image when game starts
 
 
 
    def update(self, dt):
 
#keyboard presses
        key = pygame.key.get_pressed()
    if key[pygame.K_SPACE]:
#I set the spacebar as the laser instead of 'a'
            laserSprites.add(Laser(self.rect.center))
#adds laser image to the center of ship, u can alter this to whatever section of the ship u want the laser to be shot from
 
 
 
        if key[pygame.K_LEFT]:
            self.rect.x -= 300 * dt
        if key[pygame.K_RIGHT]:
            self.rect.x += 300 * dt
    if key[pygame.K_UP]:
            self.rect.y -= 300 * dt
        if key[pygame.K_DOWN]:
            self.rect.y += 300 * dt
#movement of ship
 
 
    if self.rect.x > w-60:
        self.rect.x = w-60
    if self.rect.x < 0:
        self.rect.x = 0
    if self.rect.y > h-100:
        self.rect.y = h-100
    if self.rect.y < 0:
        self.rect.y = 0
#keeps ship within the bounds of the screen
 
 
 
 
#Enemy class
class Enemy (pygame.sprite.Sprite): 
     def __init__(self, centerx):
        pygame.sprite.Sprite.__init__(self)
        self.image = tImg
    self.rect = tImgRect
    self.rect.center = (550,50)
#Declares position of enemy ship when game starts
 
     def update(self):
         self.rect.x -= 2
         self.rect.y += 2
#enemy ship moves downwards when game starts
 
 
 
 
#Laser class
class Laser(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('laser.png')
    self.rect = pygame.rect.Rect((1, 1), self.image.get_size())
        self.rect.center = pos
 
     
    def update(self):
        if self.rect.x < 0:
           self.kill()
 
        else:    
            self.rect.move_ip(0, -10)
#direction of laser
 
 
 
class Game(object):
      
     def main(self, screen):
    clock = pygame.time.Clock()
    pygame.display.set_caption("Starwars")
     
    background_img = pygame.Surface(screen.get_size())
    background_img = pygame.image.load('deathstar.png').convert()
 
        global laserSprites, enemySprites, sprites
    laserSprites = pygame.sprite.RenderPlain(())
    enemySprites = pygame.sprite.RenderPlain(())
    enemySprites.add(Enemy(1))
        sprites = pygame.sprite.Group()
        player = Player(sprites)
 
        while 1:
        dt = clock.tick(30)
        counter = 0
        screen.blit(background_img, (0, 0))
 
                laserSprites.update()
        laserSprites.draw(screen)
        enemySprites.update()
        enemySprites.draw(screen)
        sprites.update(dt / 1000.)
        sprites.draw(screen)
 
 
                for hit in pygame.sprite.groupcollide(enemySprites, sprites, 0, 0):
                                sys.ext()
                  #collision detection between player and enemy ship
 
 
                for hit in pygame.sprite.groupcollide(enemySprites, laserSprites, 1, 0):
                                break
                       #collision detection between laser and enemy ship
 
 
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                sys.exit()
                       #game quits if esc button is pressed or 'x' is clicked
                pygame.display.flip()
 
 
 
 
if __name__ == '__main__':
   pygame.init()
   w, h = 800, 600
   screen = pygame.display.set_mode((w, h))
   Game().main(screen)