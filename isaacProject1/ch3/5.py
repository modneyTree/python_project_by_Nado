import pygame

pygame.init()
screen = pygame.display.set_mode((600, 800))
clock = pygame.time.Clock()

girl_image = pygame.image.load('girl.png')  #이미지 불러오기
girl = girl_image.get_rect()            #이미지의 사각형 정보를 가져옴
girl.centerx = 300                #이미지의 x좌표를 화면의 중앙으로 설정
girl.bottom = 800             #이미지의 y좌표를 화면의 맨 아래로 설정

while True:
    screen.fill((0, 0, 0))

    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break

    screen.blit(girl_image, girl)

    pygame.display.update()
    clock.tick(30) #초당 프레임수

pygame.quit() 
