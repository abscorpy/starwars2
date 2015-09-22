import pygame
import time

pygame.init()

red = (255, 0, 0)
display_width = 800
display_height = 600



gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('starwars')
clock = pygame.time.Clock()

dsImg = pygame.image.load('deathstar.png')
dsImg = pygame.transform.scale(dsImg, (display_width, display_height))
sImg = pygame.image.load('ship1.png')
lImg = pygame.image.load('laser.png')
tImg = pygame.image.load('tie.png')

x = (display_width*.5)
y = (display_height*.7)
x1 = (x)
y1 = (y)
x2 = (display_width*.6)
y2 = (display_height*.7)
x_change = 0
y_change = 0
shots = []
class Laser():
    x = (display_width*.5)
    y = (display_height*.7)
    x1 = (x)
    y1 = (y)
    x2 = (display_width*.6)
    y2 = (display_height*.7)
    x3 = (display_width*.6)
    y3 = (display_height*.1)
    def __init__(self, x, y):

        self.x = int(x)
        self.y = int(y)
        self.on_screen = True
        self.x1 = self.x - 40
        self.x2 = self.x + 40

        self.vel = 5

    def update(self):
        self.y -= self.vel # Shot up

        l1(self.x1, self.y)
        l2(self.x2, self.y)
        if self.y < 0: self.on_screen = False
def ship(x, y):
    gameDisplay.blit(sImg, (x, y))
def l1(x1, y1):
    gameDisplay.blit(lImg, (x1, y1))
def l2(x2, y2):
    gameDisplay.blit(lImg, (x2, y2))
def enemy(x3, y3):
    gameDisplay.blit(tImg, (x3, y3))
def enemy2(x4, y4):
    gameDisplay.blit(tImg, (x4, y4))
def enemy3(x5, y5):
    gameDisplay.blit(tImg, (x5, y5))
def enemy4(x6, y6):
    gameDisplay.blit(tImg, (x6, y6)) 

def enemies(elist):
    for x,y in elist:
        gameDisplay.blit(tImg,(x,y))


    
def game_loop():
    x = (display_width*.5)
    y = (display_height*.7)
    x1 = (x)
    y1 = (y)
    x2 = (display_width*.6)
    y2 = (display_height*.7)
    x3 = (display_width*.5)
    y3 = (display_height*.1)
    x4 = (display_width*.7)
    y4 = (display_height*.05)
    x5 = (display_width*.2)
    y5 = (display_height*.15)
    x6 = (display_width*.8)
    y6 = (display_height*.2)

    x_change = 0
    y_change = 0
    derecha=True
    shots = []
    intro=True
    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                crashed=True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                elif event.key == pygame.K_UP:
                    y_change = -5
                elif event.key == pygame.K_DOWN:
                    y_change = 5
                elif event.key == pygame.K_a:
                    shots.append(Laser(x, y))
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    y_change=0

                
        gameDisplay.blit(dsImg, (0, 0))

        for item in shots:
            item.update() # makes the shot goes up
            if not item.on_screen: shots.remove(item)
            

        x += x_change
        y += y_change
        x1 += 0
        y1 += -1
        x2 += 0
        y2 += -1
        ##x3 += -1
        ##y3 += 0
        ##x4 += -1
        ##y4 += 0
        ##x5 += -1
        ##y5 += 0
        ##x6 += -1
        if derecha==True:
            if x3<800:
                x3+=3
            else:
                derecha=False
        else:
            if x3>1:
                x3-=3
            else:
                derecha=True
        if derecha==True:
            if x4<800:
                x4+=3
            else:
                derecha=False
        else:
            if x4>1:
                x4-=3
            else:
                derecha=True
        if derecha==True:
            if x5<800:
                x5+=3
            else:
                derecha=False
        else:
            if x5>1:
                x5-=3
            else:
                derecha=True
        if derecha==True:
            if x6<800:
                x6+=3
            else:
                derecha=False
        else:
            if x6>1:
                x6-=3
            else:
                derecha=True
        ship(x, y)
        enemies(((x3,y3),(x4,y4),(x5,y5),(x6,y6)))
        #enemy(x3, y3)
        #enemy(x4, y4)
        #enemy(x5, y5)
        #enemy(x6, y6)
        pygame.display.update()
        clock.tick(65)

    
game_loop()
pygame.quit()
quit()

