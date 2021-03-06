import random
import values
import os
import json

def readLog():
    with open("log/log.json", "r") as log_file:
        return json.load(log_file)

def writeLog():
    global turn
    global maxScore
    
    
    log = readLog()
    
    log_json = {"turn" : 0, "maxScore" : 0}
    
    if(turn > log['turn']):
        log_json["turn"] = turn
    else:
        log_json["turn"] = log["turn"]
    if(maxScore > log['maxScore']):
        log_json["maxScore"] = maxScore
    else:
        log_json["maxScore"] = log["maxScore"]
    
    with open("log/log.json", "w") as log_file:
        json.dump(log_json, log_file)


class Image:
    def __init__(self, img, score, locate):
        self.image = img
        self.score = score
        self.locate = locate
def showImg(img, x,y):
    screen.blit(img, (x,y))
def showImgs(imgs):
    for img in imgs:
        showImg(img.image, img.locate[0], img.locate[1])
def loadImage(path, size):
    return pygame.transform.scale(pygame.image.load(path), size)

def getTextByTop(text, fontsize, textColor, bgcolor, x, y):
    font = pygame.font.Font('freesansbold.ttf', fontsize) 
    text = font.render(text, True, textColor, bgcolor)
    textRect = text.get_rect()
    textRect.x = x
    textRect.y = y
    return text, textRect
def getTextByCenter(text, fontsize, textColor, bgcolor, x, y):
    font = pygame.font.Font('freesansbold.ttf', fontsize) 
    text = font.render(text, True, textColor, bgcolor)
    textRect = text.get_rect()
    textRect.center = (x, y)
    return text, textRect
def movePocket():
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_a]: pocket.locate[0] -= values.pocketSpeed*speed
    if pressed[pygame.K_d]: pocket.locate[0] += values.pocketSpeed*speed
    if pressed[pygame.K_RIGHT]: pocket.locate[0] += values.pocketSpeed*speed
    if pressed[pygame.K_LEFT]: pocket.locate[0] -= values.pocketSpeed*speed
    if pressed[pygame.K_w]: pocket.locate[1] -= values.pocketSpeed*speed
    if pressed[pygame.K_s]: pocket.locate[1] += values.pocketSpeed*speed
    if pressed[pygame.K_UP]: pocket.locate[1] -= values.pocketSpeed*speed
    if pressed[pygame.K_DOWN]: pocket.locate[1] += values.pocketSpeed*speed
    
def resetFallObject():
    global turn
    global locate
    global speed
    global fallSpeed
    global objects
    global objectIndex
    
    turn += 1
    
    locate[1] = 0-values.fallingObjectsize[1]
    objectIndex = random.choice(percentages)
    locate = objects[objectIndex].locate
    locate[0] = random.randint(0, values.size[0]-values.fallingObjectsize[0])
    
    fallSpeed = values.fallSpeed * speed
    if(speed < 4):
        speed += values.addingSpeed

#????????? ??? ?????? ??????
os.system("wscript alert.vbs")

import pygame

#??????
pygame.init()

#title
pygame.display.set_caption("?????? ??????")

#?????????
screen= pygame.display.set_mode(values.size)

#?????????
finish = False
isSetUp = True
isGameIn = False
gameStartTrigger = False

#????????? ????????????
backgroundImg = loadImage(r'resources\background.jpg', (values.size[0], values.size[1]))
cakeImg = loadImage(r'resources\cake.png', values.fallingObjectsize)
cookieImg = loadImage(r'resources\cookie.png', values.fallingObjectsize)
shitImg = loadImage(r'resources\shit.png', values.fallingObjectsize)
pocketImg = loadImage(r'resources\pocket.png', values.pocketObjectsize)

#?????? ????????????
bgm1 = pygame.mixer.Sound('resources\music1.wav')
bgm1.set_volume(0.5)
bgm1.play(-1)



#????????? ????????????(????????? ??????, ??????, ??????)
cake = Image(cakeImg, values.cakeScore, [random.randint(0, values.size[0]-values.fallingObjectsize[0]),0]) 
cookie = Image(cookieImg,values.cookieScore, [random.randint(0, values.size[0]-values.fallingObjectsize[0]),0])
shit = Image(shitImg, values.shitScore, [random.randint(0, values.size[0]-values.fallingObjectsize[0]),0])
pocket = Image(pocketImg, None, [values.size[0]/2-values.pocketObjectsize[0]/2,values.size[1] - values.pocketObjectsize[1] - 10])

#?????? ??????
score = 0
maxScore = score
turn = 0
objects = [cake, cookie, shit]
speed = values.speed
fallSpeed = values.fallSpeed

#?????? ??????
scoreText, scoreTextRect = getTextByTop(f'SCORE : {score}', 20, values.textColor,values.bgcolor, values.smallNotice[0], values.smallNotice[1])
maxscoreText, maxscoreTextRect = getTextByTop(f'MAX SCORE : {maxScore}', 20, values.textColor,values.bgcolor, values.smallNotice[0], values.smallNotice[1]+20)
turnText, turnTextRect = getTextByTop(f'TURN : {turn}', 20, values.textColor,values.bgcolor, values.smallNotice[0], values.smallNotice[1]+40)
maxscoreLargeText, maxscoreLargeTextRect = getTextByCenter(f'MAX SCORE : {maxScore}', 50, values.textColor,values.bgcolor, values.bigNotice[0], values.bigNotice[1]-25)
turnLargeText, turnLargeTextRect = getTextByCenter(f'TURN : {turn}', 50, values.textColor,values.bgcolor, values.bigNotice[0], values.bigNotice[1]+25)
restartLargeText, restartLargeTextRect = getTextByCenter(f'PRESS SPACE BAR TO RESTART', 20, values.textColor,values.bgcolor, values.bigNotice[0], values.bigNotice[1]+60)

#?????? ??????
percentages = []

for i in range(values.cakePercentage):
    percentages.append(0)
for i in range(values.cookiePercentage):
    percentages.append(1)
for i in range(values.shitPercentage):
    percentages.append(2)

#object ??????
objectIndex = random.choice(percentages)
locate = objects[objectIndex].locate

#?????? ??????
while not(finish):
    #????????????
    showImg(backgroundImg, 0,0)

    #????????? ??????
    for event in pygame.event.get():
        #????????????
        if event.type == pygame.QUIT:
            writeLog()
            finish = True
        

    #?????? ???
    if(isGameIn):
        #????????? ?????????
        if(isSetUp):
            score = 0
            maxScore = score
            turn = 0
            speed = values.speed
            fallSpeed = values.fallSpeed
            
            objectIndex = random.choice(percentages)
            locate = objects[objectIndex].locate
            
            cake = Image(cakeImg, values.cakeScore, [random.randint(0, values.size[0]-values.fallingObjectsize[0]),0]) 
            cookie = Image(cookieImg,values.cookieScore, [random.randint(0, values.size[0]-values.fallingObjectsize[0]),0])
            shit = Image(shitImg, values.shitScore, [random.randint(0, values.size[0]-values.fallingObjectsize[0]),0])
            pocket = Image(pocketImg, None, [values.size[0]/2-values.pocketObjectsize[0]/2,values.size[1] - values.pocketObjectsize[1] - 10])  
        #????????? ?????? 
        isSetUp = False 
        
        #pocket ????????? ??????
        movePocket()

        
        #?????? ?????? ??????
        if(pocket.locate[0] < 0):  
            pocket.locate[0] = 0
        elif(pocket.locate[0] > values.size[0]-values.pocketObjectsize[0]):
            pocket.locate[0] = values.size[0]-values.pocketObjectsize[0]
        elif(pocket.locate[1] < values.size[1]-values.pocketObjectsize[1] - 100): 
            pocket.locate[1] = values.size[1]-values.pocketObjectsize[1] - 100
        elif(pocket.locate[1] > values.size[1]-values.pocketObjectsize[1]):
            pocket.locate[1] = values.size[1]-values.pocketObjectsize[1]
            
        
        
        #?????? ??????
        if(locate[1]+values.fallingObjectsize[1] > pocket.locate[1] and locate[1]-values.fallingObjectsize[1] < pocket.locate[1] + values.pocketObjectsize[1]):
            #????????????
            if(locate[0]+values.fallingObjectsize[0] > pocket.locate[0]-values.fallingObjectsize[0] /2 and locate[0]+values.fallingObjectsize[0] < pocket.locate[0] + values.pocketObjectsize[0] + values.fallingObjectsize[0]/2):
                score += objects[objectIndex].score
                
                if(maxScore < score):
                    maxScore = score
                resetFallObject()             
            #??????????????? 
            else:
                locate[1] += fallSpeed*speed
                fallSpeed += values.addingFallSpeed * speed
                   
        #????????? ?????? ???????????? ????????? ???
        elif(locate[1] > values.size[1]):
            resetFallObject()
        else:
            locate[1] += fallSpeed*speed
            fallSpeed += values.addingFallSpeed * speed
                

            
        #text??????
        scoreText, scoreTextRect = getTextByTop(f'SCORE : {score}', 20, values.textColor,values.bgcolor, values.smallNotice[0], values.smallNotice[1])
        maxscoreText, maxscoreTextRect = getTextByTop(f'MAX SCORE : {maxScore}', 20, values.textColor,values.bgcolor, values.smallNotice[0], values.smallNotice[1]+20)
        turnText, turnTextRect = getTextByTop(f'TURN : {turn}', 20, values.textColor,values.bgcolor, values.smallNotice[0], values.smallNotice[1]+40)
        screen.blit(scoreText, scoreTextRect) 
        screen.blit(maxscoreText, maxscoreTextRect) 
        screen.blit(turnText, turnTextRect) 
        #????????? ????????????
        showImgs([objects[objectIndex], pocket])
        #????????? 0????????? ???
        if(score < 0):
            isGameIn = False
            gameStartTrigger = False
    #?????? ??????
    else:
        writeLog()
        log = readLog()
        #text??????
        logText, logTextRect = getTextByCenter(f'PC MAX SCORE : {log["maxScore"]}', 50,values.textColor,values.bgcolor, values.bigNotice[0], values.bigNotice[1]-125)
        log2Text, log2TextRect = getTextByCenter(f'PC MAX TURN : {log["turn"]}', 50,values.textColor,values.bgcolor, values.bigNotice[0], values.bigNotice[1]-75)
        maxscoreLargeText, maxscoreLargeTextRect = getTextByCenter(f'MAX SCORE : {maxScore}', 50,values.textColor,values.bgcolor, values.bigNotice[0], values.bigNotice[1]-25)
        turnLargeText, turnLargeTextRect = getTextByCenter(f'TURN : {turn}', 50, values.textColor,values.bgcolor, values.bigNotice[0], values.bigNotice[1]+25)
        screen.blit(log2Text, log2TextRect) 
        screen.blit(logText, logTextRect) 
        screen.blit(maxscoreLargeText, maxscoreLargeTextRect) 
        screen.blit(turnLargeText, turnLargeTextRect) 
        screen.blit(restartLargeText, restartLargeTextRect) 
        #restart
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_SPACE] and not gameStartTrigger:
            isGameIn = True; isSetUp = True; gameStartTrigger = True
        #?????? ??????
        elif pressed[pygame.K_ESCAPE]:
            finish = True
        
        
        
    
        
    pygame.display.flip()