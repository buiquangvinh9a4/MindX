import pygame, sys

# khởi tạo
pygame.init()
clock = pygame.time.Clock()

# tạo ra cửu sổ game
screen_width = 1200
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong Game')

# tạo màu sắc colors

bg_color = pygame.Color('black') #RGB
white = pygame.Color('white')

player1 = (0, 90, 156) # RGB

# Rectangles
m = 30
ball = pygame.Rect(screen_width / 2 - m / 2 , screen_height / 2 - m / 2, m, m)
player_right = pygame.Rect(screen_width - 20, screen_height / 2 - 70, 10, 150) 
player_left = pygame.Rect(20, screen_height / 2 - 70, 10, 150) 

rectangle = pygame.Rect(100, 80, 150, 50)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # sự kiện ấn vào dấu x (đỏ), thoát cửa sổ
            pygame.quit()
            sys.exit()
            
    # Draw
    # Sử dụng hàm pygame.draw(surface, color, rect)
    screen.fill(bg_color)
    pygame.draw.ellipse(screen, white, ball)
    pygame.draw.rect(screen, white, player_left)
    pygame.draw.rect(screen, white, player_right)
    pygame.draw.aaline(screen, white, (screen_width / 2, 0), (screen_width / 2, screen_height ))
    pygame.draw.rect(screen, white, rectangle)

    pygame.display.flip()
    clock.tick(60)   # số khung hình trên giây: FPS
