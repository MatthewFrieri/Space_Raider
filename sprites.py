import pygame as pg
pg.init()

def get_player_sprites():

    ufo = [
    pg.image.load("Sprites\\UFO Sprites\\UFO\\UFO1.png"),
    pg.image.load("Sprites\\UFO Sprites\\UFO\\UFO2.png"),
    pg.image.load("Sprites\\UFO Sprites\\UFO\\UFO3.png"),
    pg.image.load("Sprites\\UFO Sprites\\UFO\\UFO4.png"),
    pg.image.load("Sprites\\UFO Sprites\\UFO\\UFO5.png"),
    pg.image.load("Sprites\\UFO Sprites\\UFO\\UFO6.png")
    ]

    bigUfo = [
    pg.image.load("Sprites\\UFO Sprites\\Big UFO\\bigUFO1.png"),
    pg.image.load("Sprites\\UFO Sprites\\Big UFO\\bigUFO2.png"),
    pg.image.load("Sprites\\UFO Sprites\\Big UFO\\bigUFO3.png"),
    pg.image.load("Sprites\\UFO Sprites\\Big UFO\\bigUFO4.png"),
    pg.image.load("Sprites\\UFO Sprites\\Big UFO\\bigUFO5.png"),
    pg.image.load("Sprites\\UFO Sprites\\Big UFO\\bigUFO6.png")
    ]

    swayingUfo = [
    pg.image.load("Sprites\\UFO Sprites\\Swaying UFO\\swayingUFO1.png"),
    pg.image.load("Sprites\\UFO Sprites\\Swaying UFO\\swayingUFO2.png"),
    pg.image.load("Sprites\\UFO Sprites\\Swaying UFO\\swayingUFO3.png"),
    pg.image.load("Sprites\\UFO Sprites\\Swaying UFO\\swayingUFO4.png"),
    pg.image.load("Sprites\\UFO Sprites\\Swaying UFO\\swayingUFO5.png"),
    pg.image.load("Sprites\\UFO Sprites\\Swaying UFO\\swayingUFO6.png")
    ]

    walkingRight = [
    pg.image.load("Sprites\\Astronaut Sprites\\Walking Right\\walkRight1.png"),
    pg.image.load("Sprites\\Astronaut Sprites\\Walking Right\\walkRight2.png"),
    pg.image.load("Sprites\\Astronaut Sprites\\Walking Right\\walkRight3.png"),
    pg.image.load("Sprites\\Astronaut Sprites\\Walking Right\\walkRight4.png"),
    pg.image.load("Sprites\\Astronaut Sprites\\Walking Right\\walkRight5.png"),
    pg.image.load("Sprites\\Astronaut Sprites\\Walking Right\\walkRight6.png"),
    pg.image.load("Sprites\\Astronaut Sprites\\Walking Right\\walkRight7.png"),
    pg.image.load("Sprites\\Astronaut Sprites\\Walking Right\\walkRight8.png"),
    pg.image.load("Sprites\\Astronaut Sprites\\Walking Right\\walkRight9.png"),
    pg.image.load("Sprites\\Astronaut Sprites\\Walking Right\\walkRight10.png"),
    pg.image.load("Sprites\\Astronaut Sprites\\Walking Right\\walkRight11.png"),
    pg.image.load("Sprites\\Astronaut Sprites\\Walking Right\\walkRight12.png")
    ]
        
    walkingLeft = [
    pg.image.load("Sprites\\Astronaut Sprites\\Walking Left\\walkLeft1.png"),
    pg.image.load("Sprites\\Astronaut Sprites\\Walking Left\\walkLeft2.png"),
    pg.image.load("Sprites\\Astronaut Sprites\\Walking Left\\walkLeft3.png"),
    pg.image.load("Sprites\\Astronaut Sprites\\Walking Left\\walkLeft4.png"),
    pg.image.load("Sprites\\Astronaut Sprites\\Walking Left\\walkLeft5.png"),
    pg.image.load("Sprites\\Astronaut Sprites\\Walking Left\\walkLeft6.png"),
    pg.image.load("Sprites\\Astronaut Sprites\\Walking Left\\walkLeft7.png"),
    pg.image.load("Sprites\\Astronaut Sprites\\Walking Left\\walkLeft8.png"),
    pg.image.load("Sprites\\Astronaut Sprites\\Walking Left\\walkLeft9.png"),
    pg.image.load("Sprites\\Astronaut Sprites\\Walking Left\\walkLeft10.png"),
    pg.image.load("Sprites\\Astronaut Sprites\\Walking Left\\walkLeft11.png"),
    pg.image.load("Sprites\\Astronaut Sprites\\Walking Left\\walkLeft12.png")
    ]

    idleRight = [
    pg.image.load("Sprites\\Astronaut Sprites\\Idle Right\\idleRight1.png"),
    pg.image.load("Sprites\\Astronaut Sprites\\Idle Right\\idleRight2.png"),
    pg.image.load("Sprites\\Astronaut Sprites\\Idle Right\\idleRight3.png"),
    pg.image.load("Sprites\\Astronaut Sprites\\Idle Right\\idleRight4.png"),
    pg.image.load("Sprites\\Astronaut Sprites\\Idle Right\\idleRight5.png"),
    pg.image.load("Sprites\\Astronaut Sprites\\Idle Right\\idleRight6.png"),
    pg.image.load("Sprites\\Astronaut Sprites\\Idle Right\\idleRight7.png"),
    pg.image.load("Sprites\\Astronaut Sprites\\Idle Right\\idleRight8.png"),
    pg.image.load("Sprites\\Astronaut Sprites\\Idle Right\\idleRight9.png")
    ]

    idleLeft = [
    pg.image.load("Sprites\\Astronaut Sprites\\Idle Left\\idleLeft1.png"),
    pg.image.load("Sprites\\Astronaut Sprites\\Idle Left\\idleLeft2.png"),
    pg.image.load("Sprites\\Astronaut Sprites\\Idle Left\\idleLeft3.png"),
    pg.image.load("Sprites\\Astronaut Sprites\\Idle Left\\idleLeft4.png"),
    pg.image.load("Sprites\\Astronaut Sprites\\Idle Left\\idleLeft5.png"),
    pg.image.load("Sprites\\Astronaut Sprites\\Idle Left\\idleLeft6.png"),
    pg.image.load("Sprites\\Astronaut Sprites\\Idle Left\\idleLeft7.png"),
    pg.image.load("Sprites\\Astronaut Sprites\\Idle Left\\idleLeft8.png"),
    pg.image.load("Sprites\\Astronaut Sprites\\Idle Left\\idleLeft9.png")
    ]

    jetpackStartRight = [
    pg.image.load("Sprites\\Astronaut Sprites\\Jetpack Start Right\\jetpackStartRight1.png"),
    pg.image.load("Sprites\\Astronaut Sprites\\Jetpack Start Right\\jetpackStartRight2.png"),
    pg.image.load("Sprites\\Astronaut Sprites\\Jetpack Start Right\\jetpackStartRight3.png"),
    pg.image.load("Sprites\\Astronaut Sprites\\Jetpack Start Right\\jetpackStartRight4.png"),
    pg.image.load("Sprites\\Astronaut Sprites\\Jetpack Start Right\\jetpackStartRight5.png")
    ]

    jetpackStartLeft = [
    pg.image.load("Sprites\\Astronaut Sprites\\Jetpack Start Left\\jetpackStartLeft1.png"),
    pg.image.load("Sprites\\Astronaut Sprites\\Jetpack Start Left\\jetpackStartLeft2.png"),
    pg.image.load("Sprites\\Astronaut Sprites\\Jetpack Start Left\\jetpackStartLeft3.png"),
    pg.image.load("Sprites\\Astronaut Sprites\\Jetpack Start Left\\jetpackStartLeft4.png"),
    pg.image.load("Sprites\\Astronaut Sprites\\Jetpack Start Left\\jetpackStartLeft5.png")
    ]
    
    damagedRight = [
    pg.image.load("Sprites\\Astronaut Sprites\\Damaged Right\\damagedRight1.png"),
    pg.image.load("Sprites\\Astronaut Sprites\\Damaged Right\\damagedRight2.png"),
    pg.image.load("Sprites\\Astronaut Sprites\\Damaged Right\\damagedRight3.png")
    ]

    damagedLeft = [
    pg.image.load("Sprites\\Astronaut Sprites\\Damaged Left\\damagedLeft1.png"),
    pg.image.load("Sprites\\Astronaut Sprites\\Damaged Left\\damagedLeft2.png"),
    pg.image.load("Sprites\\Astronaut Sprites\\Damaged Left\\damagedLeft3.png")
    ]

    deathRight = [
    pg.image.load("Sprites\\Astronaut Sprites\\Death Right\\deathRight1.png"),
    pg.image.load("Sprites\\Astronaut Sprites\\Death Right\\deathRight2.png"),
    pg.image.load("Sprites\\Astronaut Sprites\\Death Right\\deathRight3.png"),
    pg.image.load("Sprites\\Astronaut Sprites\\Death Right\\deathRight4.png"),
    pg.image.load("Sprites\\Astronaut Sprites\\Death Right\\deathRight5.png"),
    pg.image.load("Sprites\\Astronaut Sprites\\Death Right\\deathRight6.png"),
    pg.image.load("Sprites\\Astronaut Sprites\\Death Right\\deathRight7.png"),
    pg.image.load("Sprites\\Astronaut Sprites\\Death Right\\deathRight8.png"),
    pg.image.load("Sprites\\Astronaut Sprites\\Death Right\\deathRight9.png"),
    pg.image.load("Sprites\\Astronaut Sprites\\Death Right\\deathRight10.png"),
    pg.image.load("Sprites\\Astronaut Sprites\\Death Right\\deathRight11.png"),
    pg.image.load("Sprites\\Astronaut Sprites\\Death Right\\deathRight12.png"),
    pg.image.load("Sprites\\Astronaut Sprites\\Death Right\\deathRight13.png"),
    pg.image.load("Sprites\\Astronaut Sprites\\Death Right\\deathRight14.png")
    ]

    deathLeft = [
    pg.image.load("Sprites\\Astronaut Sprites\\Death Left\\deathLeft1.png"),
    pg.image.load("Sprites\\Astronaut Sprites\\Death Left\\deathLeft2.png"),
    pg.image.load("Sprites\\Astronaut Sprites\\Death Left\\deathLeft3.png"),
    pg.image.load("Sprites\\Astronaut Sprites\\Death Left\\deathLeft4.png"),
    pg.image.load("Sprites\\Astronaut Sprites\\Death Left\\deathLeft5.png"),
    pg.image.load("Sprites\\Astronaut Sprites\\Death Left\\deathLeft6.png"),
    pg.image.load("Sprites\\Astronaut Sprites\\Death Left\\deathLeft7.png"),
    pg.image.load("Sprites\\Astronaut Sprites\\Death Left\\deathLeft8.png"),
    pg.image.load("Sprites\\Astronaut Sprites\\Death Left\\deathLeft9.png"),
    pg.image.load("Sprites\\Astronaut Sprites\\Death Left\\deathLeft10.png"),
    pg.image.load("Sprites\\Astronaut Sprites\\Death Left\\deathLeft11.png"),
    pg.image.load("Sprites\\Astronaut Sprites\\Death Left\\deathLeft12.png"),
    pg.image.load("Sprites\\Astronaut Sprites\\Death Left\\deathLeft13.png"),
    pg.image.load("Sprites\\Astronaut Sprites\\Death Left\\deathLeft14.png")
    ]

    fullHeart = pg.image.load("Sprites\\Full Heart.png")
    emptyHeart = pg.image.load("Sprites\\Empty Heart.png")
    
    lobbyBackground = pg.image.load("Sprites\\Lobby Background.png")
    lobbyTitle = pg.image.load("Sprites\\Lobby Title.png")

    playButton = pg.image.load("Sprites\\Play Button.png")
    playButtonHover = pg.image.load("Sprites\\Play Button Hover.png")
    creditsButton = pg.image.load("Sprites\\Credits Button.png")
    creditsButtonHover = pg.image.load("Sprites\\Credits Button Hover.png")
    leaderboardsButton = pg.image.load("Sprites\\Leaderboards Button.png")
    leaderboardsButtonHover = pg.image.load("Sprites\\Leaderboards Button Hover.png")
    homeButton = pg.image.load("Sprites\\Home Button.png")
    homeButtonHover = pg.image.load("Sprites\\Home Button Hover.png")
    replayButton = pg.image.load("Sprites\\Replay Button.png")
    replayButtonHover = pg.image.load("Sprites\\Replay Button Hover.png") 
    soundOnButton = pg.image.load("Sprites\\Sound On Button.png")
    soundOnButtonHover = pg.image.load("Sprites\\Sound On Button Hover.png")
    soundOffButton = pg.image.load("Sprites\\Sound Off Button.png")
    soundOffButtonHover = pg.image.load("Sprites\\Sound Off Button Hover.png")


    deathScreen = pg.image.load("Sprites\\Death Screen.png") 
    highScoreMessage = pg.image.load("Sprites\\High Score Message.png")

    trophy1 = pg.image.load("Sprites\\Trophy 1.png") 
    trophy2 = pg.image.load("Sprites\\Trophy 2.png") 
    trophy3 = pg.image.load("Sprites\\Trophy 3.png") 
    ribbon = pg.image.load("Sprites\\Ribbon.png") 

    return ufo, bigUfo, swayingUfo, walkingRight, walkingLeft, idleRight, idleLeft, jetpackStartRight, jetpackStartLeft, damagedRight, damagedLeft, deathRight, deathLeft, fullHeart, emptyHeart, lobbyBackground, lobbyTitle, playButton, playButtonHover, creditsButton, creditsButtonHover, leaderboardsButton, leaderboardsButtonHover, homeButton, homeButtonHover, replayButton, replayButtonHover, deathScreen, highScoreMessage, trophy1, trophy2, trophy3, ribbon, soundOnButton, soundOnButtonHover, soundOffButton, soundOffButtonHover