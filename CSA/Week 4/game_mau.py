import pygame, sys     # import hai thư viện pygame và sys (system)

# khởi tạo
pygame.init()
clock = pygame.time.Clock()

# tạo ra hai kích thước của cửa sổ game
screen_width = 1280
screen_height = 720

# tạo ra màn hình game dựa vào hai kích thước trên
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong Game')    # tạo ra title cho game

# tạo ra màu sắc cho nhân vật, cho background
bgcolor = pygame.Color('black')
blue = (0, 90, 156)


# xử lý màn hình game
while True:
    for event in pygame.event.get():      # kiểm tra tất cả sự kiện game
        if event.type == pygame.QUIT:     # nếu thấy một sự kiện "nhấp chuột vào nút thoát - nút X đỏ"
            pygame.quit()                 # thoát game
            sys.exit()
            
    pygame.display.flip()       # cập nhật màn hình
    clock.tick(60)              # tỉ lệ khung hình trên giây (FPS)




