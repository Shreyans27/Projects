import pygame
import random
pygame.init()

shipX = 368
shipY = 450
shipX_change = 0
shipY_change = 0

bulletX = shipX + 20
bulletY = shipY - 20  
bulletX_change = 0
bulletY_change = -10

alien_no = []
number_of_alien = 5
i = 0  # checking condition to decrease y value of alien
j = 0  # calculate score
alienX_change = 10
alienY_change = 0
change = 10
for k in range(0,5):
    alienX = (int(round(random.randint(0, 730) / 10.0) * 10.0)) 
    alienY = (int(round(random.randint(50, 300) / 10.0) * 10.0))
    temp = [alienX,alienY,alienX_change,alienY_change,i]
    alien_no.append(temp)

state = ''
show = True
size = width, height = 800, 600

screen = pygame.display.set_mode(size)
sound = pygame.mixer.Sound('blast.mp3')
sound.set_volume(0.2)
pygame.display.set_caption('Space')
alien = pygame.image.load('alien.png')
bullet = pygame.image.load('bullet.png')
space_ship = pygame.image.load('spaceship.png')
background = pygame.image.load('space_background.png')
pygame.display.set_icon(space_ship)
clock = pygame.time.Clock()

# RGB VALUES
black = (0, 0, 0)
red = (213, 50, 80)
white = (255,255,255)
yellow = (255, 255, 102)

def spaceship(shipX,shipY):
     screen.blit(space_ship, (shipX,shipY))    

def bullet_body(bulletX,bulletY):
    screen.blit(bullet, (bulletX,bulletY))

def alien_body(alien_no):
    for k in alien_no:
        screen.blit(alien, (k[0],k[1]))
    
def score(j):
    myfont_1 = pygame.font.SysFont(None, 50)
    label_1 = myfont_1.render("Score: "+str(j), 1, yellow)
    screen.blit(label_1, (10, 10))
    
def gameover(j):
    myfont_1 = pygame.font.SysFont(None, 50)
    myfont_2 = pygame.font.SysFont(None, 100)
    label_1 = myfont_1.render("Score: "+str(j), 1, yellow)
    label_2 = myfont_2.render("GAMEOVER", 1, yellow)
    screen.blit(label_2, (200, 200))
    screen.blit(label_1, (340, 275))

def boundary():
    pygame.draw.line(screen, yellow, (0,450), (800,450))

def shoot_sound():
    sound.play()
    
leave = False
while not leave:
    
    screen.fill(black)
    screen.blit(background, (0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            leave = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                if show == True:
                    shipX_change = -10
                    shipY_change = 0
                else:
                    shipX_change = 0
                    shipY_change = 0
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                if show == True:
                    shipX_change = 10
                    shipY_change = 0
                else:
                    shipX_change = 0
                    shipY_change = 0
            
            if event.key == pygame.K_SPACE:
                if show == True:
                    bulletX = shipX + 20
                    bulletY = shipY - 20  
                    state = 'go'
                else: 
                    state = ''
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                shipX_change = 0
                shipY_change = 0
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                shipX_change = 0
                shipY_change = 0

        if event.type == pygame.QUIT:
            leave = True # quit if clicked on cross button
    
    # movement of ship
    shipX += shipX_change
    shipY += shipY_change
    
    # stop ship from going out of frame
    if shipX >= width - 64:
        shipX = width - 64
    if shipX <= 0:
        shipX = 0
    
    if state == 'go':
        bullet_body(bulletX,bulletY)
        # movement of bullet
        bulletX += bulletX_change
        bulletY += bulletY_change
    
    alien_body(alien_no)
    # movement of alien
    for k in alien_no:
        k[0] += k[2]  # increase alienX by alienX_change
        if k[4] == 1 : k[1] += k[3] # if i == 1, increase alienY by alienY_change
    
    # change values of k[2] = alienX_change, k[3] = alienY_change, k[4] = i
    for k in alien_no:
        # check if alien goes out of frame
        if k[0] >= width - 64: 
            k[4] = 0
            k[2] = -change # reverse alienX direction
            k[3] = 10      # decrease alienY level by 10
        if k[0] <= 0:     
            k[4] = 0       
            k[2] = change  # reverse alienX direction
            k[3] = 10      # decrease alienY level by 10
    
    for k in alien_no:
        if bulletX-2 <= k[0] + 64 and bulletX+2 >= k[0]: # check for same x level
            if bulletY == k[1] + 30 :  # check for same y level
                j = j + 1
                state = ''
                print("Score:",j,end=", ")
                print("Collision coords:",bulletX,k[1] + 30)
                shoot_sound()
                # generate new alien coordinates
                k[0] = (int(round(random.randint(0, 730) / 10.0) * 10.0))
                k[1] = (int(round(random.randint(50, 350) / 10.0) * 10.0))
                change += 1 # alien speed increase after a kill
                for k in alien_no: 
                    if k[2] >= 0 : k[2] = change
                    if k[2] <= 0 : k[2] = -change                 
                
    for k in alien_no:
        if k[1] + 60 == shipY:  # if 1 alien reaches shipY level
                gameover(j)
                show = False
                for k in alien_no:
                    k[2] = 0  # make alienX_change = 0 for all
                    k[3] = 0  # make alienY_change = 0 for all
        
    spaceship(shipX,shipY)
    if show == True: score(j)
    boundary()
    pygame.display.update()
    clock.tick(30) # FPS ( game speed/smoothness )
    for k in alien_no:
        k[4] += 1  # increase i count
    
pygame.quit()
