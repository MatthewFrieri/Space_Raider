import pygame as pg
import random 
import math
pg.init()

import sprites
ufo, bigUfo, swayingUfo, walkingRight, walkingLeft, idleRight, idleLeft, jetpackStartRight, jetpackStartLeft, damagedRight, damagedLeft, deathRight, deathLeft, fullHeart, emptyHeart, lobbyBackground, lobbyTitle, playButton, playButtonHover, creditsButton, creditsButtonHover, leaderboardsButton, leaderboardsButtonHover, homeButton, homeButtonHover, replayButton, replayButtonHover, deathScreen, highScoreMessage, trophy1, trophy2, trophy3, ribbon, soundOnButton, soundOnButtonHover, soundOffButton, soundOffButtonHover = sprites.get_player_sprites()

screenWidth, screenHeight = 1800, 1000
WIN = pg.display.set_mode((screenWidth, screenHeight))
pg.display.set_caption("Space Raider")

#Images
ground = pg.image.load("Sprites\\Ground.png").convert_alpha()
mountains = pg.image.load("Sprites\\Mountains.png").convert_alpha()
stars = pg.image.load("Sprites\\Stars.png").convert_alpha()
credits = pg.image.load("Sprites\\Credits.png").convert_alpha()

#Sounds
highPitchPress = pg.mixer.Sound("Sounds\\High Pitch Press.wav")
lowPitchPress = pg.mixer.Sound("Sounds\\Low Pitch Press.wav")
enterSound = pg.mixer.Sound("Sounds\\Enter.wav")
enterSound.set_volume(0.5)
wrongSound = pg.mixer.Sound("Sounds\\Wrong.wav")
wrongSound.set_volume(0.2)

jumpSound = pg.mixer.Sound("Sounds\\Jump.wav")
jumpSound.set_volume(0.2)
clickSound = pg.mixer.Sound("Sounds\\Click.wav")
clickSound.set_volume(0.2)

grunt1 = pg.mixer.Sound("Sounds\\Grunt1.wav")
grunt1.set_volume(0.05)
grunt2 = pg.mixer.Sound("Sounds\\Grunt2.wav")
grunt2.set_volume(0.05)
grunt3 = pg.mixer.Sound("Sounds\\Grunt3.wav")
grunt3.set_volume(0.05)
grunt4 = pg.mixer.Sound("Sounds\\Grunt4.wav")
grunt4.set_volume(0.05)

deathScream = pg.mixer.Sound("Sounds\\Death1.wav")
deathScream.set_volume(0.05)
damageGrunts = [grunt1, grunt2, grunt3, grunt4]

pg.mixer.music.load("Sounds\\Music.wav")
pg.mixer.music.set_volume(0.1)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 242, 0)
FPS = 60

font = pg.font.Font("C:\\Windows\\Fonts\\impact.ttf", 100)
fontSize = 100
deathFont = pg.font.Font("C:\\Windows\\Fonts\\impact.ttf", fontSize)

state = "lobby"
volumeOn = True

#Update the window
def draw(state, click, titleBobCounter, titleDirection, titleY, fontSize, deathFont, name, volumeOn):

    if state == "game":
        #Draw the scenery
        WIN.fill(BLACK)
        WIN.blit(stars, (starsX, 0))
        WIN.blit(ground, (groundX, 844))
        WIN.blit(mountains, (mountainsX, 444))
        
        #Draw UFOs
        WIN.blit(ufoSprite, (alien1.x, alien1.y))
        WIN.blit(ufoSprite, (alien2.x, alien2.y))
        WIN.blit(ufoSprite, (alien3.x, alien3.y))
        WIN.blit(ufoSprite, (alien4.x, alien4.y))
        WIN.blit(ufoSprite, (alien5.x, alien5.y))

        WIN.blit(bigUfoSprite, (bigAlien.x, bigAlien.y))
        WIN.blit(swayingUfoSprite, (swayingAlien.x, swayingAlien.y))

        #Draw the user
        WIN.blit(player, (user.x, user.y))

        #Draw the score
        scoreText = font.render(str(score), True, YELLOW)
        WIN.blit(scoreText, (30, 15))

        #Draw the health
        if lives == 3:
            WIN.blit(fullHeart, (1590, 20))
            WIN.blit(fullHeart, (1655, 20))
            WIN.blit(fullHeart, (1720, 20))
        
        if lives == 2:
            WIN.blit(fullHeart, (1590, 20))
            WIN.blit(fullHeart, (1655, 20))
            WIN.blit(emptyHeart, (1720, 20))
            
        if lives == 1:
            WIN.blit(fullHeart, (1590, 20))
            WIN.blit(emptyHeart, (1655, 20))
            WIN.blit(emptyHeart, (1720, 20))

        if lives <= 0:
            WIN.blit(emptyHeart, (1590, 20))
            WIN.blit(emptyHeart, (1655, 20))
            WIN.blit(emptyHeart, (1720, 20))
  
    #In lobby
    elif state == "lobby":

        #Move the title
        if titleDirection == "up":
            titleBobCounter += 0.05

        else:
            titleBobCounter -= 0.05

        if titleBobCounter < -2 or titleBobCounter > 2:
            if titleDirection == "up":
                titleDirection = "down"
            else:
                titleDirection = "up"

        titleY += titleBobCounter
        WIN.blit(lobbyBackground, (0, 0))
        WIN.blit(lobbyTitle, (430, titleY))

        #Play button
        playButtonDistance = math.sqrt((mouseX - 900)**2 + (mouseY - 825)**2)

        if playButtonDistance <= 100:
            WIN.blit(playButtonHover, (800, 725))
            
            #If the button is pressed
            if click == 1:
                state = "game"
                clickSound.play()
                main(state)

        else:
            WIN.blit(playButton, (800, 725))

        #Credits button
        creditsButtonDistance = math.sqrt((mouseX - 1175)**2 + (mouseY - 825)**2)

        if creditsButtonDistance <= 75:
            WIN.blit(creditsButtonHover, (1100, 750))
            
            #If the button is pressed
            if click == 1:
                state = "credits"
                clickSound.play()
        else:
            WIN.blit(creditsButton, (1100, 750))

        #Leaderboards button
        leaderboardsButtonDistance = math.sqrt((mouseX - 625)**2 + (mouseY - 825)**2)
        
        if leaderboardsButtonDistance <= 75:
            WIN.blit(leaderboardsButtonHover, (550, 750))
            
            #If the button is pressed
            if click == 1:
                state = "leaderboards"
                clickSound.play()
        else:
            WIN.blit(leaderboardsButton, (550, 750))
    
    #In credits screen
    elif state == "credits":
        WIN.blit(lobbyBackground, (0, 0))
        WIN.blit(credits, (0, 0))

        #Home button
        homeButtonDistance = math.sqrt((mouseX - 200)**2 + (mouseY - 800)**2)

        if homeButtonDistance <= 125:
            WIN.blit(homeButtonHover, (75, 675))
            
            #If the button is pressed
            if click == 1:
                state = "lobby"
                clickSound.play()
        else:
            WIN.blit(homeButton, (75, 675))

    #In the leaderboards screen
    elif state == "leaderboards":
        WIN.blit(lobbyBackground, (0, 0))

        leaderboardsFont = pg.font.Font("C:\\Windows\\Fonts\\impact.ttf", 70)
        
        leaderboards = open("leaderboard.txt", "r")
        leaderboardsList = leaderboards.readlines()
        leaderboards.close()

        topScores = []

        for person in leaderboardsList:
            splitList = person.split(" ")
            topScores.append((int(splitList[0]), splitList[1]))
            topScores.sort()
            topScores.reverse()

        firstPlace = leaderboardsFont.render(f"{topScores[0][1][:-1]}  -  {topScores[0][0]}", True, WHITE)
        secondPlace = leaderboardsFont.render(f"{topScores[1][1][:-1]}  -  {topScores[1][0]}", True, WHITE)
        thirdPlace = leaderboardsFont.render(f"{topScores[2][1][:-1]}  -  {topScores[2][0]}", True, WHITE)
        fourthPlace = leaderboardsFont.render(f"{topScores[3][1][:-1]}  -  {topScores[3][0]}", True, WHITE)
        fifthPlace = leaderboardsFont.render(f"{topScores[4][1][:-1]}  -  {topScores[4][0]}", True, WHITE)
        
        WIN.blit(trophy1, (250, 50))
        WIN.blit(trophy2, (350, 175))
        WIN.blit(trophy3, (450, 300))
        WIN.blit(ribbon, (550, 425))
        WIN.blit(ribbon, (650, 550))

        WIN.blit(firstPlace, (400, 50))
        WIN.blit(secondPlace, (500, 175))
        WIN.blit(thirdPlace, (600, 300))
        WIN.blit(fourthPlace, (700, 425))
        WIN.blit(fifthPlace, (800, 550))

        #Home button
        homeButtonDistance = math.sqrt((mouseX - 200)**2 + (mouseY - 800)**2)

        if homeButtonDistance <= 125:
            WIN.blit(homeButtonHover, (75, 675))
            
            #If the button is pressed
            if click == 1:
                state = "lobby"
                clickSound.play()
        else:
            WIN.blit(homeButton, (75, 675))

    #In new high score screen
    elif state == "name":
        WIN.blit(deathScreen, (500, 50))

        #Score
        scoreText = deathFont.render(str(score), True, BLACK)
        scoreRect = scoreText.get_rect()
        
        while scoreRect.width < 700 and scoreRect.height < 600:
            fontSize += 1
            deathFont = pg.font.Font("C:\\Windows\\Fonts\\impact.ttf", fontSize)
            scoreText = deathFont.render(str(score), True, BLACK)
            scoreRect = scoreText.get_rect()

        WIN.blit(scoreText, ((900 - scoreRect.width / 2), (340 - scoreRect.height / 2)))
        WIN.blit(highScoreMessage, (650, 600))

        nameText = font.render(name, True, BLACK)
        nameRect = nameText.get_rect()

        WIN.blit(nameText, (900 - nameRect.width / 2, 750))
        underline = pg.Rect(625, 860, 550, 10)
        pg.draw.rect(WIN, BLACK, underline)


    #In death screen
    elif state == "death screen":

        #Screen background
        WIN.blit(deathScreen, (500, 50))

        #Score
        scoreText = deathFont.render(str(score), True, BLACK)
        scoreRect = scoreText.get_rect()
        
        while scoreRect.width < 700 and scoreRect.height < 600:
            fontSize += 1
            deathFont = pg.font.Font("C:\\Windows\\Fonts\\impact.ttf", fontSize)
            scoreText = deathFont.render(str(score), True, BLACK)
            scoreRect = scoreText.get_rect()

        WIN.blit(scoreText, ((900 - scoreRect.width / 2), (340 - scoreRect.height / 2)))

        #Home button
        homeButtonDistance = math.sqrt((mouseX - 725)**2 + (mouseY - 725)**2)

        if homeButtonDistance <= 125:
            WIN.blit(homeButtonHover, (600, 600))
            
            #If the button is pressed
            if click == 1:
                state = "lobby"
                clickSound.play()
        else:
            WIN.blit(homeButton, (600, 600))

        
        #Replay button
        replayButtonDistance = math.sqrt((mouseX - 1075)**2 + (mouseY - 725)**2)
        
        if replayButtonDistance <= 125:
            WIN.blit(replayButtonHover, (950, 600))
            
            #If the button is pressed
            if click == 1:
                state = "game"
                clickSound.play()
                main(state)
        else:
            WIN.blit(replayButton, (950, 600))
    
    volumeButtonDistance = math.sqrt((mouseX - 1725)**2 + (mouseY - 925)**2)

    #Volume ON button
    if volumeOn:
        if volumeButtonDistance <= 50:
            WIN.blit(soundOnButtonHover, (1675, 875))
            
            #If the button is pressed
            if click == 1:
                volumeOn = False
        else:
            WIN.blit(soundOnButton, (1675, 875))
        
    #Volume OFF button
    else:
        if volumeButtonDistance <= 50:
            WIN.blit(soundOffButtonHover, (1675, 875))
            
            #If the button is pressed
            if click == 1:
                volumeOn = True
                clickSound.play()
        else:
            WIN.blit(soundOffButton, (1675, 875))


    pg.display.update()
    return state, titleBobCounter, titleDirection, titleY, fontSize, deathFont, volumeOn

def main(state):
    global user, alien1, alien2, alien3, alien4, alien5, bigAlien, swayingAlien, isJumping, jumpCount, groundX, mountainsX, starsX, player, ufoSprite, bigUfoSprite, swayingUfoSprite, lives, score, sec, mouseX, mouseY, fontSize, deathFont, volumeOn
    
    clock = pg.time.Clock()
    sec = 0

    user = pg.Rect(500, 800, 48, 79)
    alien1 = pg.Rect(1800, random.randint(550, 790), 76, 54)
    alien2 = pg.Rect(1800, random.randint(650, 790), 76, 54)
    alien3 = pg.Rect(1800, random.randint(650, 790), 76, 54)
    alien4 = pg.Rect(1800, random.randint(350, 790), 76, 54)
    alien5 = pg.Rect(1800, random.randint(550, 790), 76, 54)
    bigAlien = pg.Rect(1800, random.randint(500, 766), 120, 85)
    swayingAlien = pg.Rect(1800, random.randint(500, 680), 76, 54)

    titleBobCounter = -1
    titleDirection = "up"
    titleY = 250

    lives = 3
    score = 0
    name = ""

    run = True
    isJumping = False

    jumpCount = 20
    doubleJump = 2
    gravityCount = -20
    velLR = 10
    alien1Vel, alien2Vel, alien3Vel, alien4Vel, alien5Vel = 10, 10, 15, 20, 10
    bigAlienVel = 6
    swayingAlienVel = 10

    leftPressed = False
    rightPressed = False

    groundX = 0
    mountainsX = 0
    starsX = 0

    ufoSprite = ufo[0]
    ufoIndex = 0

    bigUfoSprite = bigUfo[0]
    bigUfoIndex = 0

    swayingUfoSprite = swayingUfo[0]
    swayingUfoIndex = 0
    swayingCounter = 10
    swayingIncrement = 5
    swayingUp = True

    player = idleRight[0]
    walkingRightIndex = 0
    walkingLeftIndex = 0
    idleRightIndex = 0
    idleLeftIndex = 0
    jetpackStartIndex = 0
    damagedIndex = 0
    damageDelay = 0

    reset = False

    #After death
    deathTimer = 0
    slowCounter = 1
    alienSlowCounter = 1
    deathIndex = 0
    finalDamage = False

    alien1Slow = 100/random.randint(100, 160)
    alien2Slow = 100/random.randint(100, 160)
    alien3Slow = 100/random.randint(100, 160)
    alien4Slow = 100/random.randint(100, 160)
    alien5Slow = 100/random.randint(100, 160)
    bigAlienSlow = 100/random.randint(100, 160)
    swayingAlienSlow = 100/random.randint(100, 160)

    previousDirection = "right"

    #Leaderboards
    leaderboards = open("leaderboard.txt", "r")
    leaderboardsList = leaderboards.readlines()
    leaderboards.close()
    worseScores = []

    while run:
        clock.tick(FPS)
        mouseX, mouseY = pg.mouse.get_pos()
        click = 0

        if volumeOn:
            highPitchPress.set_volume(1)
            lowPitchPress.set_volume(1)
            enterSound.set_volume(0.5)
            wrongSound.set_volume(0.2)
            jumpSound.set_volume(0.2)
            clickSound.set_volume(0.2)
            grunt1.set_volume(0.05)
            grunt2.set_volume(0.05)
            grunt3.set_volume(0.05)
            grunt4.set_volume(0.05)
            deathScream.set_volume(0.05)
            pg.mixer.music.set_volume(0.1)

        else:
            highPitchPress.set_volume(0)
            lowPitchPress.set_volume(0)
            enterSound.set_volume(0)
            wrongSound.set_volume(0)
            jumpSound.set_volume(0)
            clickSound.set_volume(0)
            grunt1.set_volume(0)
            grunt2.set_volume(0)
            grunt3.set_volume(0)
            grunt4.set_volume(0)
            deathScream.set_volume(0)
            pg.mixer.music.set_volume(0)

        if state == "lobby":
            sec = 0

        if state == "lobby" or state == "leaderboards" or state == "credits" or state == "death screen":

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False

                #Click
                if event.type == pg.MOUSEBUTTONDOWN:
                    click = event.button
            
        elif state == "name":
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False
                
                #Keyboard
                if event.type == pg.KEYDOWN:
                    letters = [pg.K_a, pg.K_b, pg.K_c, pg.K_d, pg.K_e, pg.K_f, pg.K_g, pg.K_h, pg.K_i, pg.K_j, pg.K_k, pg.K_l, pg.K_m, pg.K_n, pg.K_o, pg.K_p, pg.K_q, pg.K_r, pg.K_s, pg.K_t, pg.K_u, pg.K_v, pg.K_w, pg.K_x, pg.K_y, pg.K_z]
                    if event.key == pg.K_BACKSPACE:
                        name = name[:-1]
                        lowPitchPress.play()
                    
                    elif event.key == pg.K_RETURN:
                        if 3 <= len(name) <= 7:
                            state = "death screen"
                            enterSound.play()

                            leaderboardsList[leaderboardsList.index(worseScores[0])] = f"{score} {name}\n"
                            leaderboards = open("leaderboard.txt", "w")
                            leaderboards.writelines(leaderboardsList)
                            leaderboards.close()

                        else:
                            wrongSound.play()

                    elif len(name) < 7 and event.key in letters:
                        highPitchPress.play()
                        name += event.unicode.upper()

                #Click
                if event.type == pg.MOUSEBUTTONDOWN:
                    click = event.button

        elif state == "game":
            sec += 1/FPS

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False
                
                #Click
                if event.type == pg.MOUSEBUTTONDOWN:
                    click = event.button
                #Jump
                if event.type == pg.KEYDOWN:
                    if (event.key == pg.K_SPACE or event.key == pg.K_w or event.key == pg.K_UP) and reset == False:
                        if doubleJump > 0:
                            doubleJump -= 1
                            jumpSound.play()
                            
                            isJumping = True
                            jumpCount = 20
                            gravityCount = -20


            #Lives left
            if lives > 0:
                
                #Gravity
                if not isJumping:
                    if user.y - gravityCount <= 763:
                        user.y -= gravityCount
                        gravityCount -= 1

                    #Hit the ground
                    else:
                        user.y = 763
                        doubleJump = 2


                #Changes the Y of the user to jump
                if isJumping and jumpCount >= -20:
                    if user.y - jumpCount >= 0:
                        user.y -= jumpCount
                        jumpCount -= 1
                    else:
                        user.y = 0
                        jumpCount -= 2
                    
                    #Animates the jetpack
                    if previousDirection == "right":
                        player = jetpackStartRight[int(jetpackStartIndex)]
                        jetpackStartIndex += 0.25

                        if int(jetpackStartIndex) == len(jetpackStartRight):
                            jetpackStartIndex = len(jetpackStartRight) - 0.25

                    elif previousDirection == "left":
                        player = jetpackStartLeft[int(jetpackStartIndex)]
                        jetpackStartIndex += 0.25

                        if int(jetpackStartIndex) == len(jetpackStartLeft):
                            jetpackStartIndex = len(jetpackStartLeft) - 0.25

                else:
                    isJumping = False
                    jetpackStartIndex = 0


                inputs = pg.key.get_pressed()
                left = inputs[pg.K_a] or inputs[pg.K_LEFT]
                right = inputs[pg.K_d] or inputs[pg.K_RIGHT]

                #Move Left
                if not (isJumping and right and not left):
                    if user.x - 5 >= 0:
                        user.x -= 5
                    else:
                        user.x = 0

                if left and not right:
                    previousDirection = "left"

                    leftPressed = velLR
                    
                    walkingLeftIndex += 1
                    if walkingLeftIndex == len(walkingLeft):
                        walkingLeftIndex = 0

                    if user.x - velLR >= 0:
                        user.x -= velLR
                    else:
                        user.x = 0
                    
                    #Switch Sprite
                    if not isJumping:
                        player = walkingLeft[walkingLeftIndex]
        

                #Glide Left
                else:
                    if leftPressed == 0:
                        leftPressed = False
                    if leftPressed != False:
                        if user.x - leftPressed >= 0:
                            user.x -= leftPressed
                        
                        else:
                            user.x = 0
                        leftPressed -= 1

                
                #Move Right
                if right and not left:
                    previousDirection = "right"

                    rightPressed = velLR

                    walkingRightIndex += 1
                    if walkingRightIndex == len(walkingRight):
                        walkingRightIndex = 0

                    if user.x + user.width + velLR <= screenWidth:
                        user.x += velLR
                    else:
                        user.x = screenWidth - user.width

                    #Switch Sprite
                    if not isJumping:
                        player = walkingRight[walkingRightIndex]         
                    

                #Glide Right
                else:
                    if rightPressed == 0:
                        rightPressed = False
                    if rightPressed != False:
                        if user.x + user.width + rightPressed <= screenWidth:
                            user.x += rightPressed
                        
                        else:
                            user.x = screenWidth - user.width
                        rightPressed -= 1


                #Change alien sprites
                ufoIndex += 0.2
                if ufoIndex >= len(ufo):
                    ufoIndex = 0

                ufoSprite = ufo[int(ufoIndex)]

                bigUfoIndex += 0.1
                if bigUfoIndex >= len(bigUfo):
                    bigUfoIndex = 0

                bigUfoSprite = bigUfo[int(bigUfoIndex)]

                swayingUfoIndex += 0.1
                if swayingUfoIndex >= len(swayingUfo):
                    swayingUfoIndex = 0

                swayingUfoSprite = swayingUfo[int(swayingUfoIndex)]

                #Alien 1 movement
                if sec > 5:
                    alien1.x -= alien1Vel
                    if alien1.x < -80:
                        score += 1
                        alien1Vel = random.randint(7, 15)
                        alien1.x = random.randint(2000, 3500)
                        alien1.y = random.randint(550, 790)

                #Alien 2 movement
                if sec > 10:
                    alien2.x -= alien2Vel
                    if alien2.x < -80:
                        score += 1
                        alien2Vel = random.randint(7, 15)
                        alien2.x = random.randint(2000, 3500)
                        alien2.y = random.randint(650, 790)

                #Alien 3 movement
                if sec > 15:
                    alien3.x -= alien3Vel
                    if alien3.x < -80:
                        score += 1
                        alien3Vel = random.randint(15, 20)
                        alien3.x = random.randint(2000, 4000)
                        alien3.y = random.randint(650, 790)

                #Alien 4 movement
                if sec > 20:
                    alien4.x -= alien4Vel
                    if alien4.x < -80:
                        score += 1
                        alien4Vel = random.randint(20, 25)
                        alien4.x = random.randint(2000, 4000)
                        alien4.y = random.randint(350, 790)

                #Alien 5 movement
                if sec > 30:
                    alien5.x -= alien5Vel
                    if alien5.x < -80:
                        score += 1
                        alien5Vel = random.randint(7, 30)
                        alien5.x = random.randint(2000, 3000)
                        alien5.y = random.randint(500, 790)

                #Big alien movement
                if sec > 45:
                    bigAlien.x -= bigAlienVel 
                    if bigAlien.x < -115:
                        score += 1
                        bigAlienVel = random.randint(6, 10)
                        bigAlien.x = random.randint(5000, 7000)
                        bigAlien.y = random.randint(500, 766)

                #Swaying alien movement
                if sec > 60:
                    swayingAlien.x -= swayingAlienVel

                    if swayingUp:
                        swayingCounter -= swayingIncrement / 10
                        if swayingCounter <= -10:
                            swayingUp = False
                    else:
                        swayingCounter += swayingIncrement / 10
                        if swayingCounter >= 10:
                            swayingUp = True
                        
                    swayingAlien.y -= int(swayingCounter)
                    
                    if swayingAlien.x < -80:
                        score += 1
                        swayingCounter = 10
                        swayingAlienVel = random.randint(6, 15)
                        swayingAlien.x = random.randint(3000, 7000)
                        swayingAlien.y = random.randint(500, 680)
                        swayingIncrement = random.randint(5, 5)


                #Move the ground
                groundX -= 5
                if groundX - 5 < -1800:
                    groundX = 0

                #Move the mountains
                mountainsX -= 3
                if mountainsX - 3 < -1800:
                    mountainsX = 0
                
                #Move the stars
                starsX -= 1
                if starsX - 1 < -1800:
                    starsX = 0

                #Idle Animation
                if not isJumping and ((not left and not right) or (left and right)):
                    
                    if previousDirection == "right":
                        idleRightIndex += 0.2
                        if int(idleRightIndex) == len(idleRight):
                            idleRightIndex = 0
                        player = idleRight[int(idleRightIndex)]

                    elif previousDirection == "left":
                        idleLeftIndex += 0.2
                        if int(idleLeftIndex) == len(idleLeft):
                            idleLeftIndex = 0
                        player = idleLeft[int(idleLeftIndex)]


                #Alien collisions with player
                if damageDelay == 0:
                    if user.colliderect(alien1) or user.colliderect(alien2) or user.colliderect(alien3) or user.colliderect(alien4) or user.colliderect(alien5) or user.colliderect(bigAlien) or user.colliderect(swayingAlien):

                        lives -= 1

                        #Hurt sounds
                        if lives == 0:
                            deathScream.play()
                        else: 
                            random.choice(damageGrunts).play()

                        if previousDirection == "left":

                            player = damagedLeft[int(damagedIndex) % 2]
                            damagedIndex += 0.25

                            if int(damagedIndex) == 15:
                                damagedIndex = 0

                        elif previousDirection == "right":

                            player = damagedRight[int(damagedIndex) % 2]
                            damagedIndex += 0.25

                            if int(damagedIndex) == 15:
                                damagedIndex = 0
                            
                        damageDelay = 60
                else:
                    damageDelay -= 1

                    if previousDirection == "left":

                        player = damagedLeft[int(damagedIndex) % 2]
                        damagedIndex += 0.25

                        if int(damagedIndex) == 15:
                            damagedIndex = 0

                    elif previousDirection == "right":
                        player = damagedRight[int(damagedIndex) % 2]
                        damagedIndex += 0.25
                        if int(damagedIndex) == 15:
                            damagedIndex = 0
                        
    
            #No lives left
            elif lives == 0 and deathIndex != 13:
                
                #Damage animation
                if not finalDamage:
                    if previousDirection == "left":
                        player = damagedLeft[int(damagedIndex) % 2]
                        damagedIndex += 0.25
                        if int(damagedIndex) == 15:
                            finalDamage = True


                    elif previousDirection == "right":
                        player = damagedRight[int(damagedIndex) % 2]
                        damagedIndex += 0.25
                        if int(damagedIndex) == 15:
                            finalDamage = True

                #Explosion animation
                else:
                    if previousDirection == "right":
                        player = deathRight[int(deathIndex)]

                    elif previousDirection == "left":
                        player = deathLeft[int(deathIndex)]
                    deathIndex += 0.2
                    if deathIndex > 13:
                        deathIndex = 13

                #Move the ground
                groundX -= 5 * slowCounter
                if groundX - 5 * slowCounter < -1800:
                    groundX = 0

                #Move the mountains
                mountainsX -= 3 * slowCounter
                if mountainsX - 3 * slowCounter < -1800:
                    mountainsX = 0
                
                #Move the stars
                starsX -= 1 * slowCounter
                if starsX - 1 * slowCounter < -1800:
                    starsX = 0

                #Alien 1 movement
                if sec > 5:
                    alien1.x -= alien1Vel * alienSlowCounter * alien1Slow
                    if alien1.x < -80:
                        score += 1
                        alien1Vel = random.randint(7, 15)
                        alien1.x = random.randint(2000, 3500)
                        alien1.y = random.randint(550, 790)

                #Alien 2 movement
                if sec > 10:
                    alien2.x -= alien2Vel * alienSlowCounter * alien2Slow
                    if alien2.x < -80:
                        score += 1
                        alien2Vel = random.randint(7, 15)
                        alien2.x = random.randint(2000, 3500)
                        alien2.y = random.randint(650, 790)

                #Alien 3 movement
                if sec > 15:
                    alien3.x -= alien3Vel * alienSlowCounter * alien3Slow
                    if alien3.x < -80: 
                        score += 1
                        alien3Vel = random.randint(15, 20)
                        alien3.x = random.randint(2000, 4000)
                        alien3.y = random.randint(650, 790)

                #Alien 4 movement
                if sec > 20:
                    alien4.x -= alien4Vel * alienSlowCounter * alien4Slow
                    if alien4.x < -80:
                        score += 1
                        alien4Vel = random.randint(20, 25)
                        alien4.x = random.randint(2000, 4000)
                        alien4.y = random.randint(350, 790)

                #Alien 5 movement
                if sec > 30:
                    alien5.x -= alien5Vel * alienSlowCounter * alien5Slow
                    if alien5.x < -80:
                        score += 1
                        alien5Vel = random.randint(7, 30)
                        alien5.x = random.randint(2000, 3000)
                        alien5.y = random.randint(500, 790)

                #Big alien movement
                if sec > 45:
                    bigAlien.x -= bigAlienVel * alienSlowCounter * bigAlienSlow
                    if bigAlien.x < -115:
                        score += 1
                        bigAlienVel = random.randint(6, 10)
                        bigAlien.x = random.randint(5000, 7000)
                        bigAlien.y = random.randint(500, 766)

                #Swaying alien movement
                if sec > 60:
                    swayingAlien.x -= swayingAlienVel * alienSlowCounter * swayingAlienSlow
                    if swayingUp:
                        swayingCounter -= swayingIncrement / 10 * alienSlowCounter * swayingAlienSlow
                        if swayingCounter <= -10 * alienSlowCounter * swayingAlienSlow:
                            swayingUp = False
                    else:
                        swayingCounter += swayingIncrement / 10 * alienSlowCounter * swayingAlienSlow
                        if swayingCounter >= 10 * alienSlowCounter * swayingAlienSlow:
                            swayingUp = True
                    swayingAlien.y -= int(swayingCounter)
                    if swayingAlien.x < -80:
                        score += 1
                        swayingCounter = 10
                        swayingAlienVel = random.randint(6, 15)
                        swayingAlien.x = random.randint(3000, 7000)
                        swayingAlien.y = random.randint(500, 680)
                        swayingIncrement = random.randint(5, 5)

                alienSlowCounter -= 0.007
                if alienSlowCounter < 0:
                    alienSlowCounter = 0
                slowCounter -= 0.005
                if slowCounter < 0:
                    slowCounter = 0
                if not reset:
                    gravityCount = 0
                reset = True

                #Gravity
                if not isJumping:
                    if user.y - gravityCount <= 763:
                        user.y -= gravityCount
                        gravityCount -= 1

                    #Hit the ground
                    else:
                        user.y = 763
                        doubleJump = 2

                #Changes the Y of the user to jump
                if isJumping and jumpCount >= -20:
                    if user.y - jumpCount >= 0:
                        user.y -= jumpCount
                        jumpCount -= 1
                    else:
                        user.y = 0
                else:
                    isJumping = False
                
                #Player scroll
                if user.x - 4 * slowCounter >= 0:
                    user.x -= int(4 * slowCounter)
                else:
                    user.x = 0
            
            #Game over
            else:
                deathTimer += 1
                if deathTimer == 100:
                    for index, line in enumerate(leaderboardsList):
                        if score > int(line[:line.index(" ")]): 
                            worseScores.append(line)
                            
                    #New high score
                    if len(worseScores) > 0:               
                        worseScores.sort(key = lambda x: x[:x.index(" ")])
                        
                        #Get the users name
                        state = "name"

                    #No new high score
                    else:
                        state = "death screen"

        #Call draw
        state, titleBobCounter, titleDirection, titleY, fontSize, deathFont, volumeOn = draw(state, click, titleBobCounter, titleDirection, titleY, fontSize, deathFont, name, volumeOn)
    pg.quit()

if __name__ == "__main__":
    pg.mixer.music.play(-1)

    main(state)