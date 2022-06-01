import pygame
import random
import time

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
blockNumWidth = 20
blockNumHeight = 20
blockSize = 40

def drawGreen(x, y, width, height):
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(x, y, width, height))
    pygame.display.flip()

def clearGreen(x, y, width, height):
    time.sleep(.05)
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(x, y, width, height))
    pygame.display.flip()

def mazeMaker(array, screen, blockNumWidth, blockNumHeight, blockSize, x, y):
    drawGreen(x * blockSize + 5, y * blockSize + 5, blockSize - 10, blockSize - 10)
    array[x][y] = True
    sides = [0, 1, 2, 3]
    sidesRandom = []
    for i in range(0, 3):
        side = random.choice(sides)
        sidesRandom.append(side)
        sides.remove(side)
    for i in sidesRandom:
        drawGreen(x * blockSize + 5, y * blockSize + 5, blockSize - 10, blockSize - 10)
        if i == 0:
            if not y == 0:
                if not array[x][y-1] == True:
                    if x == 0:
                        pygame.draw.line(screen, BLACK, (x * blockSize, y * blockSize), ((x+1) * blockSize - 1, y * blockSize), 1)
                    else:
                        pygame.draw.line(screen, BLACK, (x * blockSize + 1, y * blockSize), ((x+1) * blockSize - 1, y * blockSize), 1)
                    clearGreen(x * blockSize + 5, y * blockSize + 5, blockSize - 10, blockSize - 10)
                    mazeMaker(array, screen, blockNumWidth, blockNumHeight, blockSize, x, y-1)
        elif i == 1:
            if not x == blockNumWidth-1:
                if not array[x+1][y] == True:
                    if y == 0:
                        pygame.draw.line(screen, BLACK, ((x+1) * blockSize, y * blockSize), ((x+1) * blockSize, (y + 1) * blockSize - 1), 1)
                    else:
                        pygame.draw.line(screen, BLACK, ((x+1) * blockSize, y * blockSize + 1), ((x+1) * blockSize, (y + 1) * blockSize - 1), 1)
                    clearGreen(x * blockSize + 5, y * blockSize + 5, blockSize - 10, blockSize - 10)
                    mazeMaker(array, screen, blockNumWidth, blockNumHeight, blockSize, x+1, y)
        elif i == 2:
            if not y == blockNumHeight-1:
                if not array[x][y+1] == True:
                    if x == 0:
                        pygame.draw.line(screen, BLACK, (x * blockSize, (y  + 1) * blockSize), ((x + 1) * blockSize - 1, (y + 1) * blockSize), 1)
                    else:
                        pygame.draw.line(screen, BLACK, (x * blockSize + 1, (y  + 1) * blockSize), ((x + 1) * blockSize - 1, (y + 1) * blockSize), 1)
                    clearGreen(x * blockSize + 5, y * blockSize + 5, blockSize - 10, blockSize - 10)
                    mazeMaker(array, screen, blockNumWidth, blockNumHeight, blockSize, x, y+1)
        elif i == 3:
            if not x == 0:
                if not array[x-1][y] == True:
                    if y == 0:
                        pygame.draw.line(screen, BLACK, ((x) * blockSize, y * blockSize), ((x) * blockSize, (y + 1) * blockSize - 1), 1)
                    else:
                        pygame.draw.line(screen, BLACK, ((x) * blockSize, y * blockSize + 1), ((x) * blockSize, (y + 1) * blockSize - 1), 1)
                    clearGreen(x * blockSize + 5, y * blockSize + 5, blockSize - 10, blockSize - 10)
                    mazeMaker(array, screen, blockNumWidth, blockNumHeight, blockSize, x-1, y)
    drawGreen(x * blockSize + 5, y * blockSize + 5, blockSize - 10, blockSize - 10)
    clearGreen(x * blockSize + 5, y * blockSize + 5, blockSize - 10, blockSize - 10)

pygame.init()
size = (blockSize * blockNumWidth, blockSize * blockNumHeight)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

screen.fill(BLACK)

#draw verticle lines
for x in range(0, blockNumWidth-1):
    pygame.draw.line(screen, WHITE, ((x + 1) * blockSize, 0), ((x + 1) * blockSize, blockSize * blockNumHeight), 1)
#draw horizontal lines
for y in range(0, blockNumHeight):
    pygame.draw.line(screen, WHITE, (0, (y + 1) * blockSize), (blockSize * blockNumWidth, (y + 1) * blockSize), 1)

#2-D array for the nodes
visited = [[False]*blockNumHeight for _ in range(blockNumWidth)]

mazeMaker(visited, screen, blockNumWidth, blockNumHeight, blockSize, 5, 3)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    pygame.display.flip()
    clock.tick(60)