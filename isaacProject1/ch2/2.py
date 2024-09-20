import pygame #파이 게임 모듈 임포트

pygame.init() #파이 게임 초기화
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #화면 크기 설정
clock = pygame.time.Clock() 

#변수

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
YELLOW = (255, 255, 0)

while True: #게임 루프
    screen.fill(BLACK) #단색으로 채워 화면 지우기

    #변수 업데이트

    event = pygame.event.poll() #이벤트 처리
    if event.type == pygame.QUIT:
        break

    #화면 그리기

    pygame.display.update() #모든 화면 그리기 업데이트
    clock.tick(30) #30 FPS (초당 프레임 수) 를 위한 딜레이 추가, 딜레이 시간이 아닌 목표로 하는 FPS 값

pygame.quit() 

"""
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
YELLOW = (255, 255, 0)
"""