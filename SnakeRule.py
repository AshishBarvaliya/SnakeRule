import pygame
import random

pygame.init()
white = (255,255,255)
black =(0,0,0)
red=(255,0,0)
green=(0,115,0)

clock=pygame.time.Clock()
d_width =800
d_length =600
applethik=25
gameDisplay=pygame.display.set_mode((d_width,d_length))
pygame.display.set_caption('SnakeRule')
icon=pygame.image.load('snakerule_apple.png')
pygame.display.set_icon(icon)

block_size=20
f_time=17
snake_head_img=pygame.image.load('snakehead.png')


largefont = pygame.font.SysFont("comicsansms",73)
sfont = pygame.font.SysFont("comicsansms",25)
mfont = pygame.font.SysFont("comicsansms",40)
def game_intro():
    intro=True
    while intro:
        gameDisplay.fill(white)
        msg_screen("Welcome to SnakeRule",green,-120,"large")
        msg_screen("the objective of the game is to eat red apples",black,-50,size="small")
        msg_screen("the more apples you eat, the longer you get",black,0,size="small")
        msg_screen("if you run into yourself or the edges, you die!",black,50,size="small")
        msg_screen("press C for Start,P to pause or Q for Quit",black,180,size="med")
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_q:
                    pygame.quit()
                    quit()
                elif event.key==pygame.K_c:
                    intro=False
                    gameLoop()

direction="right"
def snake(snakeList,block_size):
    if direction=="right":
        head=pygame.transform.rotate(snake_head_img,270)
    if direction=="left":
        head=pygame.transform.rotate(snake_head_img,90)
    if direction=="up":
        head=snake_head_img
    if direction=="down":
        head=pygame.transform.rotate(snake_head_img,180)
        
    gameDisplay.blit(head, (snakeList[-1][0],snakeList[-1][1]))
        
    for xny in snakeList[:-1]:
        pygame.draw.rect(gameDisplay, green, [xny[0],xny[1],block_size,block_size])
def msg_screen(msg,color,y_distance,size):
    if size=="large":
        
        screen_text = largefont.render(msg, True, color)
        text_rect = screen_text.get_rect(center=(d_width/2, d_length/2 + y_distance))      
    if size=="med":
        
        screen_text = mfont.render(msg, True, color)
        text_rect = screen_text.get_rect(center=(d_width/2, d_length/2 + y_distance))   
    if size=="small":
        
        screen_text = sfont.render(msg, True, color)
        text_rect = screen_text.get_rect(center=(d_width/2, d_length/2 + y_distance))       
    return gameDisplay.blit(screen_text,text_rect)

def pause():
    pause=True
    while pause:
        msg_screen("paused",red,-50,size="large")
        msg_screen("press C for continue or Q for Quit",black,50,size="med")
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_q:
                    pygame.quit()
                    quit()
                elif event.key==pygame.K_c:
                    pause=False    


def score(score):
    text_score=sfont.render("Score="+str(score), True,black)       
    gameDisplay.blit(text_score,[0,0])
    
def randapple():
    appleX = random.randrange(0, d_width-applethik)
    appleY = random.randrange(0, d_length-applethik)
    return appleX,appleY
    
def gameLoop(): 
    global direction
    direction="right"
    exit=False
    gameover=False
    
    lead_x=d_width/2
    lead_y=d_length/2
    
    lead_x_change=0
    lead_y_change=0
    
    snakeList=[]
    snakelength=1
    global count
    count=0
    
    appleX,appleY=randapple()

    while not exit:
        while gameover==True:
            gameDisplay.fill(white)
            msg_screen("score:"+str(count), black,-110,"med")
            msg_screen("Game Over",red,-50,size="large")
            msg_screen("press C for Restart or Q for Quit",black,50,size="med")
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        pygame.quit()
                        quit()
                    elif event.key==pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    direction="left"
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key==pygame.K_RIGHT:
                    direction="right"
                    lead_x_change = block_size
                    lead_y_change = 0

                elif event.key==pygame.K_UP:
                    direction="up"
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key==pygame.K_DOWN:
                    direction="down"
                    lead_y_change = block_size
                    lead_x_change = 0
                elif event.key==pygame.K_p:
                    pause()    

        if lead_x >= d_width or lead_x < 0 or lead_y < 0 or lead_y >= d_length:
            gameover=True

        lead_x += lead_x_change
        lead_y += lead_y_change
        gameDisplay.fill(white)
        
        #pygame.draw.rect(gameDisplay, red, [appleX,appleY,applethik,applethik])
        apple_img=pygame.image.load('snakerule_apple.png')
        gameDisplay.blit(apple_img,(appleX,appleY))
        
        snakeHead=[]
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)
        if len(snakeList) > snakelength:
            del(snakeList[0])
        for eachseg in snakeList[:-1]:
            if eachseg==snakeHead:
                gameover=True
        
        snake(snakeList,block_size)
        
        score(snakelength-1)
        pygame.display.update()
        
        if lead_x > appleX and lead_x < appleX+applethik or lead_x+block_size >appleX and lead_x+block_size <appleX+applethik: 
            if lead_y > appleY and lead_y < appleY+applethik:
                appleX,appleY=randapple()
                snakelength+=1
                count+=1
            elif lead_y+block_size >appleY and lead_y+block_size <appleY+applethik:
                appleX,appleY=randapple()
                snakelength+=1    
                count+=1
        clock.tick(f_time)
    pygame.quit()
    quit()
game_intro()
gameLoop()