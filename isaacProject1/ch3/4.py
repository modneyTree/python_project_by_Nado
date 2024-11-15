import pygame

pygame.init()
screen = pygame.display.set_mode((600, 800))
clock = pygame.time.Clock()

girl_image = pygame.image.load('girl.png')
girl = girl_image.get_rect()
girl.left = 300 - girl_image.get_width() // 2
girl.top = 800 - girl_image.get_height()

while True:
    screen.fill((0, 0, 0))

    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break

    screen.blit(girl_image, girl)

    pygame.display.update()
    clock.tick(30) #초당 프레임수

pygame.quit() 
