import random
import pygame

pygame.init()

# Spil-variabler og konstanter
WIDTH = 600
HEIGHT = 600
fps = 60
timer = pygame.time.Clock()
rows = 6
cols = 8
correct = [[0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0]]
optionsList = []
spaces = []
used = []
newBoard = True
firstGuess = False
secondGuess = False
firstGuessNum = 0
secondGuessNum = 0
score = 0
bestScore = 0
matches = 0
gameOver = False

# Farver
white = (255, 255, 255)
black = (0, 0, 0,)
grey = (128, 128, 128, 128)
green = (125, 185, 182)
blue = (83, 127, 231)
pink = (221, 83, 83)
purple = (183, 62, 62)

# Lyde
wrongSound = pygame.mixer.Sound("./sounds/fejl.wav")
clickSound = pygame.mixer.Sound("./sounds/klik.wav")
correctSound = pygame.mixer.Sound("./sounds/korrekt.wav")

# Fonts
titleFont = pygame.font.Font("freesansbold.ttf", 56)
smallFont = pygame.font.Font("freesansbold.ttf", 26)
middleFont = pygame.font.Font("freesansbold.ttf", 40)

# Opret spillet
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Julies vendespil!")

def generateBoard():
    global optionsList
    global spaces
    global bestScore
    highscoreFile = open("./highscore.txt", "r")
    bestScore = int(highscoreFile.read())
    highscoreFile.close()
    for item in range(rows * cols // 2):
        optionsList.append(item)

    for item in range(rows * cols):
        piece = optionsList[random.randint(0, len(optionsList) - 1)]
        spaces.append(piece)
        if piece in used:
            used.remove(piece)
            optionsList.remove(piece)
        else: 
            used.append(piece)


def drawBackgrounds():
    topMenu = pygame.draw.rect(screen, purple, [0, 0, WIDTH, 100], 0)
    titleText = titleFont.render("Julies vendespil", True, black)
    screen.blit(titleText, (70, 20))
    boardSpace = pygame.draw.rect(screen, pink, [0, 100, WIDTH, HEIGHT - 200], 0)
    buttomMenu = pygame.draw.rect(screen, purple, [0, HEIGHT - 100, WIDTH, 100], 0)
    restartButton = pygame.draw.rect(screen, pink, [20, HEIGHT - 80, 180, 60], 0, 10)
    restartText = middleFont.render("Restart", True, white)
    screen.blit(restartText, (40, 530))
    scoreText = smallFont.render(f'Current Turns: {score}', True, white)
    screen.blit(scoreText, (350, 520))
    bestText = smallFont.render(f'All-Time Best: {bestScore}', True, white)
    screen.blit(bestText, (350, 560))

    return restartButton

def drawBoard():
    global rows
    global cols
    global correct
    boardList = []
    for i in range(cols):
        for j in range(rows):
            piece = pygame.draw.rect(screen, white, [i * 75 + 12, j * 65 + 112, 50, 50], 0, 4)
            boardList.append(piece)
            '''pieceText = smallFont.render(f'{spaces[i * rows + j]}', True, grey)
            screen.blit(pieceText, (i * 75 + 18, j * 65 + 120))'''

    for r in range(rows):
        for c in range(cols):
            if correct[r][c] == 1:
                pygame.draw.rect(screen, green, [c * 75 + 10, r * 65 + 110, 54, 54], 3, 4)
                image = numberToImage(spaces[c * rows + r])
                image = pygame.transform.scale(image, (40, 40))
                #pieceText = smallFont.render(f'{spaces[c * rows + r]}', True, black)
                screen.blit(image, (c * 75 + 18, r * 65 + 120))


    return boardList


def checkGuesses(first, second):
    global spaces
    global correct
    global score
    global matches
    if spaces[first] == spaces[second]:
        col1 = first // rows
        col2 = second // rows
        row1 = first - (col1 * rows)
        row2 = second - (col2 *rows)
        if correct[row1][col1] == 0 and correct[row2][col2] == 0:
            correct[row1][col1] = 1
            correct[row2][col2] = 1
            score += 1
            matches += 1
            correctSound.set_volume(0.3)
            playSound(correctSound)
    else:
        score += 1
        wrongSound.set_volume(0.3)
        playSound(wrongSound)

        
def playSound(sound):
    play = True
    if play:
        sound.play()
        play = False

def numberToImage(number):
    match number:
        case 0:
            return pygame.image.load("./picture/abrikos.jpg").convert()
        case 1:
            return pygame.image.load("./picture/aeble.jpg").convert()
        case 2:
            return pygame.image.load("./picture/annanas.jpg").convert()
        case 3:
            return pygame.image.load("./picture/appelsin.jpg").convert()
        case 4:
            return pygame.image.load("./picture/banan.jpg").convert()
        case 5:
            return pygame.image.load("./picture/blaabaer.jpg").convert()
        case 6:
            return pygame.image.load("./picture/citron.jpg").convert()
        case 7:
            return pygame.image.load("./picture/granataeble.jpg").convert()
        case 8:
            return pygame.image.load("./picture/hindbaer.jpg").convert()
        case 9:
            return pygame.image.load("./picture/jordbaer.jpg").convert()
        case 10:
            return pygame.image.load("./picture/kakifrugt.jpg").convert()
        case 11:
            return pygame.image.load("./picture/kirsebaer.jpg").convert()
        case 12:
            return pygame.image.load("./picture/kiwi.jpg").convert()
        case 13:
            return pygame.image.load("./picture/lime.jpg").convert()
        case 14:
            return pygame.image.load("./picture/melon.jpg").convert()
        case 15:
            return pygame.image.load("./picture/paerer.jpg").convert()
        case 16:
            return pygame.image.load("./picture/passionsfrugt.jpg").convert()
        case 17:
            return pygame.image.load("./picture/pomelo.jpg").convert()
        case 18:
            return pygame.image.load("./picture/ribs.jpg").convert()
        case 19:
            return pygame.image.load("./picture/rosiner.jpg").convert()
        case 20:
            return pygame.image.load("./picture/solbaer.jpg").convert()
        case 21:
            return pygame.image.load("./picture/stikkelsbaer.jpg").convert()
        case 22:
            return pygame.image.load("./picture/tranebaer.jpg").convert()
        case 23:
            return pygame.image.load("./picture/vindruer.jpg").convert()


running = True
while running:
    timer.tick(fps)
    screen.fill(white)
    if newBoard:
        generateBoard()
        newBoard = False

    restart = drawBackgrounds()
    board = drawBoard()


    if firstGuess and secondGuess:
        checkGuesses(firstGuessNum, secondGuessNum)
        pygame.time.delay(1000)
        firstGuess = False
        secondGuess = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(board)):
                button = board[i]
                if not gameOver:
                    if button.collidepoint(event.pos) and not firstGuess:
                        firstGuess = True
                        firstGuessNum = i
                        clickSound.set_volume(0.3)
                        playSound(clickSound)
                    if button.collidepoint(event.pos) and not secondGuess and firstGuess and i != firstGuessNum:
                        secondGuess = True
                        secondGuessNum = i

            if restart.collidepoint(event.pos):
                optionsList = []
                used = []
                spaces = []
                newBoard = True
                score = 0
                matches = 0
                firstGuess = False
                secondGuess = False
                correct = [[0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0]]
                gameOver = False

    if matches == rows * cols // 2:
        gameOver = True
        winner = pygame.draw.rect(screen, grey, [10, HEIGHT - 300, WIDTH - 20, 80], 0, 5)
        winnerText = titleFont.render(f'You won in {score} moves!', True, white)
        screen.blit(winnerText, (10, HEIGHT - 290))
        if bestScore > score or bestScore == 0:
            bestScore = score
            highscoreFile = open("./highscore.txt", "w")
            highscoreFile.write(str(bestScore))
            highscoreFile.close()

        # Vendespil med tal
    '''if firstGuess:
        pieceText = smallFont.render(f'{spaces[firstGuessNum]}', True, blue)
        location = (firstGuessNum // rows * 75 + 18, (firstGuessNum - (firstGuessNum // rows * rows)) * 65 + 120)
        screen.blit(pieceText, (location))

    if secondGuess:
        pieceText = smallFont.render(f'{spaces[secondGuessNum]}', True, blue)
        location = (secondGuessNum // rows * 75 + 18, (secondGuessNum - (secondGuessNum // rows * rows)) * 65 + 120)
        screen.blit(pieceText, (location))'''


        # Vendespil med billeder
    if firstGuess:
        image = numberToImage(spaces[firstGuessNum])
        image = pygame.transform.scale(image, (40, 40))
        location = (firstGuessNum // rows * 75 + 18, (firstGuessNum - (firstGuessNum // rows * rows)) * 65 + 120)
        screen.blit(image, (location))

    if secondGuess:
        image = numberToImage(spaces[secondGuessNum])
        image = pygame.transform.scale(image, (40, 40))
        location = (secondGuessNum // rows * 75 + 18, (secondGuessNum - (secondGuessNum // rows * rows)) * 65 + 120)
        screen.blit(image, (location))

    pygame.display.flip()
pygame.quit()