# starwars2
import pygame
import time

pygame.init()

red = (255, 0, 0)
display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('starwars')
clock = pygame.time.Clock()


#make variable names more freindly so other can understand what it means

display_image = pygame.image.load('deathstar.png')
display_image = pygame.transform.scale(display_image, (display_width, display_height))

ship_image = pygame.image.load('Ship1.png')
lImg = pygame.image.load('laser.png')

#
enemy_image = pygame.image.load('tie.png')

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

# ship, laser, enemy, should be classes as they are objects.
# all these classes should contain methods/fucntions which contains behaviour.

def ship(x, y):
    gameDisplay.blit(ship_image, (x, y))


#you dont need to make 2 different l1 and l2 fucntion for same bullets/lasers.
# you can call same function twice with different x and y. and then update them.

def l1(x1, y1):
    gameDisplay.blit(lImg, (x1, y1))

def l2(x2, y2):
    gameDisplay.blit(lImg, (x2, y2))

def enemy(x3, y3):
    gameDisplay.blit(enemy_image, (x3, y3))

def enemy2(x4, y4):
    gameDisplay.blit(enemy_image, (x4, y4))

def enemy3(x5, y5):
    gameDisplay.blit(enemy_image, (x5, y5))

def enemy4(x6, y6):
    gameDisplay.blit(enemy_image, (x6, y6))

#make some exit also for game.
#for example on pressing escape key it should quit.
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

    shots = []
    intro=True

    while intro:
        for event in pygame.event.get():
            print(event)

            if event.type == pygame.QUIT:
                #on trying to quit it should quit the game by making intro - Flase. it ends the game loop on quit event and closes the game.
                #you can make game more gracefully if you want by making a game over function which exits with notifications and saying goodbye.
                intro = False
                #crashed does not do anything.
                #crashed=True
            #if event.type == pygame.:
            if event.type == pygame.KEYDOWN:

                #these movements are fine but can be done better with in class player or ship with an update method.
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                elif event.key == pygame.K_UP:
                    y_change = -5
                elif event.key == pygame.K_DOWN:
                    y_change = 5

                #same for this shoot event should have been done in a function in class ship.
                elif event.key == pygame.K_a:
                    shots.append(Laser(x, y))

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    y_change=0

        gameDisplay.blit(display_image, (0, 0))

        for item in shots:
            item.update() # makes the shot goes up
            if not item.on_screen: shots.remove(item)

        x += x_change
        y += y_change
        x1 += 0
        y1 += -1
        x2 += 0
        y2 += -1
        x3 += -1
        y3 += 0
        x4 += -1
        y4 += 0
        x5 += -1
        y5 += 0
        x6 += -1

        ## i can see you are changing a lot of co-ordinates here but you should be calling update method here and let class do these things.
        #these things should go in methods.
        if x3>=0:
            x3 += 1
        if x3<=1:
            x3 -= 1
        if x4>=0:
            x4 += 1
        if x4<=1:
            x4 -= 1
        if x5>=0:
            x5 += 1
        if x5<=1:
            x5 -= 1
        if x6>=0:
            x6 += 1
        if x6<=1:
            x6 -= 1
######################

    ##MAX_TIES = 10

# this creates MAX_TIES number of TIES each with random properties x, y, direction.
# x is a random number between 1 and screen_width - 1 (799)
# y is a random number between 1 and screen_height - 1 (599)
# d direction is either -1 (move left) or 1 (move right)
# t is the image of the enemy
##    ties = [{
##	'x' : random.randint(1, SCREEN_WIDTH - 1),
##	'y' : random.randint(1, SCREEN_HEIGHT - 1),
##	'd' : -1 if random.randint(0, 1) == 1 else 1,
##        't' : gameDisplay.blit(enemy_image, ('x', 'y'))
##	} for i in xrange(MAX_TIES)]
##
##
##    for t in ties:
### first test if moving the block will make it hit the sides of the display
##        if (t['x'] + t['d'] >= SCREEN_WIDTH) or (t['x'] + t['d'] <= 0):
##                t['d'] = -t['d'] # change the direction of the block
##			
##                t['x'] += t['d'] # block direction can be either 1 or -1 depending on the direction it is going
##		
##		# draw the tie to the display
##  
##        gameDisplay.blit(enemy_image, ('x', 'y'))
    ship(x, y)
    enemy(x3, y3)
    enemy(x4, y4)
    enemy(x5, y5)
    enemy(x6, y6)

        # to make enemies die we need to have clossions detection
        # for collission detection we need sprites.
        # we can add sprites here also but it will to confusing looking at the current condition of code.


        # my suggestion is start again and refactor this code in classes and add behaviour in methods. for help you can look at my code of spaceturds game.
        

    pygame.display.update()
    clock.tick(65)

game_loop()
pygame.quit()
quit()
