import pygame

pygame.init()
screen = pygame.display.set_mode((600, 800))
clock = pygame.time.Clock()

girl_image = pygame.image.load('girl.png')
girl = girl_image.get_rect(centerx=300, bottom=800)

while True:
    screen.fill((0, 0, 0))

    event = pygame.event.poll() #이벤트 처리
    if event.type == pygame.QUIT:   #종료 이벤트
        break
    elif event.type == pygame.KEYDOWN:  #키 이벤트
        if event.key == pygame.K_LEFT:
            girl.left -= 5
        elif event.key == pygame.K_RIGHT:
            girl.left += 5

    screen.blit(girl_image, girl)

    pygame.display.update()
    clock.tick(30) #초당 프레임수

pygame.quit() 