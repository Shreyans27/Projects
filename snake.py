import random
import pygame
pygame.init()

# record = open('record.txt','a+')
# handle = open('record.txt','r')
# name = input("Enter Name : ")

snakeL = []
length = 1
snakeX = 400
snakeY = 300
snakeX_change = 0
snakeY_change = 0
size = width, height = 800, 600

foodx = round(random.randint(0, width - 20) / 10.0) * 10.0
foody = round(random.randint(0, height - 20) / 10.0) * 10.0 

screen = pygame.display.set_mode(size)
#pygame.display.set_caption('Snake')
#icon = pygame.image.load('snake.png')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()

# RGB VALUES
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)

# SNAKE BODY
def pos(snakeL):
    for i in snakeL:
        pygame.draw.rect(screen,black,[i[0],i[1],20,20])  
        
def score(length):
    myfont_1 = pygame.font.SysFont(None, 50)
    label_1 = myfont_1.render("Score: "+str(length-1), 1, black)
    screen.blit(label_1, (10, 10))
    
def gameover(length):
    myfont_1 = pygame.font.SysFont(None, 50)
    myfont_2 = pygame.font.SysFont(None, 100)
    label_1 = myfont_1.render("Score: "+str(length), 1, black)
    label_2 = myfont_2.render("GAMEOVER", 1, black)
    screen.blit(label_2, (200, 200))
    screen.blit(label_1, (340, 275))
    
leave = False
while not leave:
    
    screen.fill(yellow)
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            leave = True
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                snakeY_change = -10
                snakeX_change = 0
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                snakeY_change = 10
                snakeX_change = 0
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                snakeX_change = -10
                snakeY_change = 0
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                snakeX_change = 10
                snakeY_change = 0
        
    if snakeX >= width or snakeX < 0 or snakeY >= height or snakeY < 0:
            gameover(length-1)
            snakeX_change = 0
            snakeY_change = 0
            
    pygame.draw.rect(screen,red,[foodx,foody,10,10])        
    snakeX += snakeX_change
    snakeY += snakeY_change
    
    snake_Head = []
    snake_Head.append(snakeX)
    snake_Head.append(snakeY)
    snakeL.append(snake_Head)
    if len(snakeL) > length:
        del snakeL[0]
    pos(snakeL)
    score(length)
    pygame.display.update()
    clock.tick(30)
    
    if snakeX == foodx and snakeY == foody or snakeX+10 == foodx and snakeY+10 == foody:
        foodx = round(random.randint(0, width - 20) / 10.0) * 10.0
        foody = round(random.randint(0, height - 20) / 10.0) * 10.0
        length += 1
    
pygame.quit()

score1 = str(length - 1)
high_score = int(score1) 

# for line in handle:
#     if line.startswith('Player Score : '):
#         a = line.split(':')
#         if int(a[1]) > high_score:
#             high_score = int(a[1])

print('\nYour Score =',score1) 
# print('High Score =',high_score) 

# record.write('\n\n')
# record.write('Player Name : ')
# record.write(name)
# record.write('\n')
# record.write('Player Score : ')
# record.write(score1)
# record.close()
# handle.close()
