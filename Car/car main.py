import pygame
import random
pygame.init()

carX = 368
carY = 450
carX_change = 0
carY_change = 0

block_no = []
number_of_block = 10
i = 0  # checking condition to decrease y value of alien
j = 0  # calculate score
blockX_change = 0
blockY_change = 5
change = 0.3
for k in range(0,number_of_block):
    blockX = (int(round(random.randint(0, 534) / 10.0) * 10.0)) 
    blockY = (int(round(random.randint(0, 200) / 10.0) * 10.0))
    temp = [blockX,blockY,blockX_change,blockY_change,i]
    block_no.append(temp)

state = 'go'
show = True
size = width, height = 600, 600

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Car')
car = pygame.image.load('car.png')
car1 = pygame.image.load('car1.png')
background = pygame.image.load('road.png')
pygame.display.set_icon(car)
clock = pygame.time.Clock()

# RGB VALUES
black = (0, 0, 0)
red = (213, 50, 80)
white = (255,255,255)
yellow = (255, 255, 102)

def car_body(carX,carY):
     #pygame.draw.rect(screen,red,[carX,carY,64,64]) 
     screen.blit(car, (carX,carY))    

def block_body(block_no):
    for k in block_no:
         #pygame.draw.rect(screen,white,[k[0],k[1],32,32]) 
         screen.blit(car1, (k[0],k[1]))  
    
def score(j):
    myfont_1 = pygame.font.SysFont(None, 50)
    label_1 = myfont_1.render("Distance: "+str(j)+"m", 1, yellow)
    screen.blit(label_1, (10, 10))
    
def gameover(j):
    myfont_1 = pygame.font.SysFont(None, 50)
    myfont_2 = pygame.font.SysFont(None, 100)
    label_1 = myfont_1.render("Distance: "+str(j)+"m", 1, yellow)
    label_2 = myfont_2.render("GAMEOVER", 1, yellow)
    screen.blit(label_2, (100, 200))
    screen.blit(label_1, (180, 275))

leave = False
while not leave:
    
    screen.fill(black)
    screen.blit(background, (0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            leave = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    carX_change = -10
                    carY_change = 0
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    carX_change = 10
                    carY_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                    carX_change = 0
                    carY_change = -10
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    carX_change = 0
                    carY_change = 10
                            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    carX_change = 0
                    carY_change = 0
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    carX_change = 0
                    carY_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                    carX_change = 0
                    carY_change = 0
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    carX_change = 0
                    carY_change = 0

        if event.type == pygame.QUIT:
            leave = True # quit if clicked on cross button
    
    if state == 'go':
        # movement of car
        carX += carX_change
        carY += carY_change
    
    # stop car from going out of frame
    if carX >= width - 64:
        carX = width - 64
    if carX <= 0:
        carX = 0
    if carY <= 0:
        carY = 0
    if carY >= height - 64:
        carY = height - 64
    
    for k in block_no:
        k[1] += k[3]
    
    for k in block_no:
        if k[1] >= height:
            k[0] = (int(round(random.randint(0, 534) / 10.0) * 10.0))
            k[1] = (int(round(random.randint(0, 200) / 10.0) * 10.0))
            k[3] += change
        
    for k in block_no:
        if carX + 17 >= k[0] + 17 and carX + 17 <= k[0] + 64 - 17 or carX + 64 - 17 >= k[0] + 17 and carX + 64 - 17 <= k[0] + 64 - 17: # check for same x level
            if carY >= k[1] + 7 and carY <= k[1] + 58 or k[1] + 7 >= carY and k[1] <= carY + 58: # check for same y level
                # if carX + 15 >= k[0] and carX + 15 <= k[0] + 32 or k[0] >= carX + 15 and k[0] <= carX + 64 - 15: # check for same x level
                # if carY >= k[1] and carY <= k[1] + 32 or k[1] >= carY and k[1] <= carY + 64: # check for same y level
                
                carX_change = 0
                carY_change = 0
                for n in block_no:
                    n[2] = 0
                    n[3] = 0
                state = ''
    
    if state == 'go':
        j = j + 1
        score(j)
    block_body(block_no)
    car_body(carX, carY)
    if state == '': gameover(j)           
    pygame.display.update()
    clock.tick(30) # FPS ( game speed/smoothness )
    
pygame.quit()
