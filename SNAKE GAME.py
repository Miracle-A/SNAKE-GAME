import pygame
import random

# Initialize pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Screen dimensions
WIDTH = 640
HEIGHT = 480
BLOCK_SIZE = 20

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)


class Snake:
    def __init__(self):
        self.body = [(5, 5), (4, 5), (3, 5)]
        self.direction = RIGHT

    def move(self):
        head = self.body[0]
        new_x = head[0] + self.direction[0]
        new_y = head[1] + self.direction[1]
        self.body.insert(0, (new_x, new_y))
        self.body.pop()

    def grow(self):
        head = self.body[0]
        new_x = head[0] + self.direction[0]
        new_y = head[1] + self.direction[1]
        self.body.insert(0, (new_x, new_y))

    def change_direction(self, new_direction):
        if (new_direction[0] + self.direction[0], new_direction[1] + self.direction[1]) != (0, 0):
            self.direction = new_direction

    def draw(self, surface):
        for part in self.body:
            pygame.draw.rect(
                surface, GREEN, (part[0]*BLOCK_SIZE, part[1]*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))


class Food:
    def __init__(self):
        self.position = (random.randint(0, (WIDTH // BLOCK_SIZE) - 1),
                         random.randint(0, (HEIGHT // BLOCK_SIZE) - 1))

    def randomize_position(self):
        self.position = (random.randint(0, (WIDTH // BLOCK_SIZE) - 1),
                         random.randint(0, (HEIGHT // BLOCK_SIZE) - 1))

    def draw(self, surface):
        pygame.draw.rect(
            surface, RED, (self.position[0]*BLOCK_SIZE, self.position[1]*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()
snake = Snake()
food = Food()

running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_direction(UP)
            elif event.key == pygame.K_DOWN:
                snake.change_direction(DOWN)
            elif event.key == pygame.K_LEFT:
                snake.change_direction(LEFT)
            elif event.key == pygame.K_RIGHT:
                snake.change_direction(RIGHT)

    snake.move()

    head = snake.body[0]
    if head == food.position:
        snake.grow()
        food.randomize_position()

    if (head[0] < 0 or head[0] >= WIDTH // BLOCK_SIZE or
        head[1] < 0 or head[1] >= HEIGHT // BLOCK_SIZE or
            head in snake.body[1:]):
        running = False

    snake.draw(screen)
    food.draw(screen)
    pygame.display.flip()
    clock.tick(10)

pygame.quit()