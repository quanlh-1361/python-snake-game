import sys, pygame
from random import *

pygame.init()
font = pygame.font.SysFont("None", 24)
main = pygame.display.set_mode((720, 480))
main.fill((255,255,255))

class Body:
    x=0
    y=0

    def __init__(self, x, y):
        self.x = x
        self.y = y

class Snake:
    bodyList = []
    heading = 0
    x = 0
    y = 0

    def __init__(self, x, y):
        self.heading = pygame.K_RIGHT
        self.x = x
        self.y = y

        self.bodyList.append(Body(x-20, y))
        self.bodyList.append(Body(x-40, y))
        self.bodyList.append(Body(x-60, y))
    
    def draw(self):
        for e in self.bodyList:
            pygame.draw.rect(main, (0, 255, 0), ((e.x - 10, e.y - 10), (20, 20)), 0)
        pygame.draw.rect(main, (10, 128, 0), ((self.x - 10, self.y - 10), (20, 20)), 0)
    
    def setHeading(self, key):
        self.heading = key
    
    def collide(self):
        for bd in self.bodyList:
            if ((self.x, self.y) == (bd.x, bd.y)):
                return True
            return False

    def grow(self):
        tmbBody = self.bodyList[len(self.bodyList) - 1]
        self.bodyList.append(tmbBody)

    def move(self):
        self.bodyList.insert(0, Body(self.x, self.y))
        removeBlock = self.bodyList.pop()

        pygame.draw.rect(main, (255, 255, 255), ((removeBlock.x-10, removeBlock.y-10), (20, 20)), 0)

        if self.heading == pygame.K_RIGHT:
            self.x += 20
        elif self.heading == pygame.K_DOWN:
            self.y += 20
        elif self.heading == pygame.K_UP:
            self.y -= 20
        elif self.heading == pygame.K_LEFT:
            self.x -= 20
        elif self.heading == pygame.K_q:
            sys.exit()
        else:
            return

    def eat(self, food):
        return ((food.x == self.x) and (food.y == self.y))

class Food:
    x = 0
    y = 0

    def __init__(self):
        self.x = randint(1, 34) * 20
        self.y = (randint(1, 22) * 20) + 20
        self.color = (0,0,255)

    def draw(self):
        pygame.draw.rect(main, self.color, ((self.x - 10, self.y - 10), (20, 20)), 0)
    
    def remove(self):
        pygame.draw.rect(main,(255,255,255),((self.x-10,self.y-10), (20,20)),0)
        self.x = randint(1,34) * 20
        self.y = (randint(1, 22) * 20) + 20

class ScoreBoard:
    score = 0

    def __init__(self):
        self.score = 0

    def increase(self):
        self.score += 1

    def display(self):
        pygame.draw.rect(main, (0,0,0), ((0,0), (720, 20)), 0)
        text=font.render("Score "+ str(self.score), True,(255,0,0))
        main.blit(text, (320, 5))

def outOfBound(x, y):
    if (x < 20 or x > 710 or y < 40 or y > 470):
        return True
    return False

def Main():
    scoreboard = ScoreBoard()
    apple = Food()
    snake = Snake(100, 80)

    snake.draw()
    pygame.display.update()

    while True:
        scoreboard.display()

        apple.draw()
        if outOfBound(snake.x, snake.y):
            sys.exit()
        if snake.collide():
            sys.exit()
        if snake.eat(apple):
            scoreboard.increase()
            snake.grow()
            apple.remove()
        
        snake.move()
        snake.draw()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                snake.setHeading(event.key)
            
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
    
        pygame.time.delay(70)


if __name__ == '__main__':
    pygame.display.set_caption('Snake Game')
    pygame.draw.rect(main, (0,0,0), ((0,0), (720, 20)), 0)
    pygame.draw.rect(main, (0,0,0), ((0,20),(720,460)), 16)

    Main()
