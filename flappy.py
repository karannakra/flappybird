#for generating random numbers
import random
import pygame
from pygame.locals import*


#global variables
FPS=32
Screen_width=500
Screen_height=511
GameDisplay=pygame.display.set_mode((Screen_width,Screen_height))
GroundY=int(423)
Game_sprites={}
Game_sound={}
Player='document/images/player.png'
Background='document/images/background.png'
Pipe='document/images/pipe.png'

def WelcomeScreen():
    playerX=int(Screen_width/2-55)
    playerY=int((Screen_height -250))
    messageX = int((Screen_width - Game_sprites['message'].get_width()) /2)
    messageY = int(Screen_height-550)
    baseX=0
    while True:
        for event in pygame.event.get():
            if event.type==QUIT or(event.type==KEYDOWN and event.key==pygame.K_ESCAPE):
                pygame.quit()
                quit()
            elif event.type==KEYDOWN and (event.key==K_SPACE or event.key==K_UP):
                    return()
            else:
                GameDisplay.blit(Game_sprites['background'],(0,0))
                GameDisplay.blit(Game_sprites['player'], (playerX, playerY))
                GameDisplay.blit(Game_sprites['base'], (baseX, GroundY))
                GameDisplay.blit(Game_sprites['message'], (messageX, messageY))
                pygame.display.update()
                FPSCLOCK.tick(FPS)
def getRandomPipe():
    pipeHeight=Game_sprites['pipe'][0].get_height()

    offset=int(Screen_height/3)

    y2=offset+random.randrange(0,int(Screen_height-Game_sprites['base'].get_height()-offset))
    pipex=Screen_width+10

    y1=pipeHeight - y2 +offset
    pipe=[
        {'x':pipex,'y':-y1},#uppper pipe
        {'x':pipex,'y':y2} #lower pipe
    ]
    return pipe
def mainGame():
    score=0
    playerX=int(Screen_width/5)
    playerY=int(Screen_height/2)
    basex=0
    newPipe1=getRandomPipe()
    newPipe2=getRandomPipe()
    upperPipes=[
        {
         'x':Screen_width+200,'y':newPipe1[0]['y']},
         {'x':Screen_width+200+(Screen_width/2),'y':newPipe1[1]['y']},
    ]
    lowerPipes=[
        {
         'x': Screen_width + 200, 'y': newPipe2[0]['y']},
        {'x': Screen_width + 200 + (Screen_width / 2), 'y': newPipe2[1]['y']},
    ]
    pipeVelx=-4
    playerVely = -9
    playerMaxvelY = 50
    playerAccY =1   #player getting down speed
    playerFlapaccV = -20  # player rising speed
    playerFlapped = False
    while True:
        for event in pygame.event.get():
            if event.type==QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
                pygame.quit()
                quit()
            if event.type==KEYDOWN and(event.key==K_SPACE or event.key==K_UP):
                if playerY >0:
                    playerVely=-10
                    playerFlapped=True
                    #Game_sound[''].play()
        if playerVely < playerMaxvelY and not playerFlapped:
            playerVely += playerAccY
        if playerFlapped:
            playerFlapped = False

        playerHeight = Game_sprites['player'].get_height()
        playerY = playerY  + min(playerVely, GroundY - playerY - playerHeight)
        for upperPipe,lowerPipe in zip(upperPipes,lowerPipes):
            upperPipe['x']+=pipeVelx
            lowerPipe['x']+=pipeVelx

        if 0<upperPipes[0]['x']<5:
            newpipe=getRandomPipe()
            upperPipes.append(newpipe[0])
            lowerPipes.append(newpipe[1])

        if upperPipes[0]['x']< -Game_sprites['pipe'][0].get_width():
            upperPipes.pop(0)
            lowerPipes.pop(0)

        GameDisplay.blit(Game_sprites['background'],(0,0))
        for upperPipe,lowerPipe in zip(upperPipes,lowerPipes):
            GameDisplay.blit(Game_sprites['pipe'][0],(int(upperPipe['x']),int(upperPipe['y'])))
            GameDisplay.blit(Game_sprites['pipe'][1],(int(lowerPipe['x']),int(lowerPipe['y'])))

        GameDisplay.blit(Game_sprites['base'],(basex,GroundY))

        GameDisplay.blit(Game_sprites['player'],(playerX,playerY))

        pygame.display.update()

        FPSCLOCK.tick(FPS)
if __name__=='__main__':
    #this is the main function from where our game will start
    pygame.init()
    FPSCLOCK=pygame.time.Clock()
    pygame.display.set_caption("Flappy bird by karan nakra")
    Game_sprites['numbers']=(
    pygame.image.load("document/images/0.png").convert_alpha(),
    pygame.image.load("document/images/1.png").convert_alpha(),
    pygame.image.load("document/images/2.png").convert_alpha(),
    pygame.image.load("document/images/3.png").convert_alpha(),
    pygame.image.load("document/images/4.png").convert_alpha(),
    pygame.image.load("document/images/5.png").convert_alpha(),
    pygame.image.load("document/images/6.png").convert_alpha(),
    pygame.image.load("document/images/7.png").convert_alpha(),
    pygame.image.load("document/images/8.png").convert_alpha(),
    pygame.image.load("document/images/9.png").convert_alpha(),
    )
Game_sprites['message']=pygame.image.load("document/images/front.png").convert_alpha()

Game_sprites['base']=pygame.image.load("document/images/base.png").convert_alpha()

Game_sprites['pipe']=(
    pygame.transform.rotate(pygame.image.load(Pipe).convert_alpha(),180),

    pygame.image.load(Pipe).convert_alpha()
)
Game_sprites['background']=pygame.image.load(Background).convert()

Game_sprites['player']=pygame.image.load(Player).convert_alpha()
#game sound
''''
Game_sound['die']=pygame.mixer.sound('/document/audio/')
Game_sound['hit']=pygame.mixer.sound('/document/audio/')
Game_sound['point']=pygame.mixer.sound('/document/audio/')
Game_sound['wing']=pygame.mixer.sound('/document/audio/')
Game_sound['die']=pygame.mixer.sound('/document/audio/')
Game_sound['die']=pygame.mixer.sound('/document/audio/')
'''
while True:
    WelcomeScreen()
    mainGame()
