import pygame, sys

pygame.init()
clock = pygame.time.Clock()

screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Rectangle')

bgcolor = (210, 210, 210)
white = pygame.Color('white')
red = pygame.Color('red')

rectangle = pygame.Rect(screen_width / 2, screen_height / 2, 500, 200)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.draw.rect(screen, white, rectangle)
    
    pygame.display.flip()
    clock.tick(60)
            