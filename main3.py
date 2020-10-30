import pygame
import time
import random

pygame.init()
pygame.mixer.init()

display_width = 800
display_height = 700

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
maroon = (128, 0, 0)
yellow = (255, 255, 0)
gray = (169, 169, 169)

block_color = (53, 115, 255)

car_width = 65

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Formula 1 Racing')
clock = pygame.time.Clock()

# Background
background = pygame.image.load('road.png')
background = pygame.transform.scale(background, (800, 700)).convert_alpha()

pygame.mixer.music.load("background.wav")
pygame.mixer.music.play(-1)

# car image
carImg = pygame.image.load('car7.png')

# enemy car image
thingImg = pygame.image.load('carimg.png')

# background image welcome screen
bgimg = pygame.image.load('welcome.jpg')
bgimg = pygame.transform.scale(bgimg, (800, 700)).convert_alpha()


def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: " + str(count), True, black)
    gameDisplay.blit(text, (0, 0))


def things(x, y):
    gameDisplay.blit(thingImg, (x, y))


def car(x, y):
    gameDisplay.blit(carImg, (x, y))


def text_objects(text, font):
    textSurface = font.render(text, True, gray)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 80)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2), (495))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()


def crash():
    message_display('You Crashed')
    time.sleep(3)
    game_loop()


def welcome():
    exit_game = False
    while not exit_game:
        gameDisplay.fill((red))
        gameDisplay.blit(bgimg, (0, 0))
        message_display("Press Space to Play")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load('swoosh.wav')
                    pygame.mixer.music.play()
                    game_loop()

        pygame.display.update()
        clock.tick(40)


def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.77)

    x_change = 0

    thing_startx = random.randrange(225, 460)
    thing_starty = -600
    thing_speed = 4
    thing_width = 100
    thing_height = 100
    y1 = 0
    thingCount = 1

    dodged = 0

    gameExit = False
    pygame.mixer.music.load("background.wav")
    pygame.mixer.music.play(-1)
    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -12
                if event.key == pygame.K_RIGHT:
                    x_change = 12

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        gameDisplay.fill(white)
        rel_y = y1 % background.get_rect().height
        gameDisplay.blit(background, (0, rel_y - background.get_rect().height))
        if rel_y < display_height:
            gameDisplay.blit(background, (0, rel_y))
        y1 += 3

        # things(thingx, thingy, thingw, thingh, color)
        things(thing_startx, thing_starty)

        thing_starty += thing_speed
        car(x, y)
        things_dodged(dodged)

        if x <= 225:
            x = 225
        elif x >= 500:
            x = 500

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(255, 460)
            dodged += 1
            thing_speed += 0.3
            # thing_width += (dodged * 1.2)

        if y < thing_starty + thing_height:
            pass

            if x > thing_startx and x < thing_startx + thing_width or x + car_width > thing_startx and x + car_width < thing_startx + thing_width:
                pygame.mixer.music.load('hit.wav')
                pygame.mixer.music.play()
                crash()

        pygame.display.update()
        clock.tick(60)


welcome()
pygame.quit()
quit()
