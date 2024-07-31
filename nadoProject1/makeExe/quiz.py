import os
import pygame
import random
import sys

############################################################################################################
# 기본 초기화 (반드시 해야 하는 것들)
pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("똥 피하기 게임") # 게임 이름

# FPS
clock = pygame.time.Clock()
############################################################################################################

# 1. 사용자 게임 초기화(배경 화면, 게임 이미지, 좌표, 폰트 등)

# 배경 이미지 불러오기
current_path = os.path.dirname(__file__) # 현재 파일의 위치 반환
if getattr(sys, 'frozen', False):
    current_path = sys._MEIPASS # PyInstaller로 패키징된 경우
image_path = os.path.join(current_path, "images") # images 폴더 위치 반환

background = pygame.image.load(os.path.join(image_path, "wallpaper.jpg"))

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load(os.path.join(image_path, "dog.png"))
character_size = character.get_rect().size # 이미지의 크기를 구해옴
character_width = character_size[0] # 캐릭터의 가로 크기
character_height = character_size[1] # 캐릭터의 세로 크기
character_x_pos = (screen_width / 2) - (character_width / 2) # 화면 가로의 절반 크기에 해당하는 곳에 위치
character_y_pos = screen_height - character_height # 화면 세로 크기 가장 아래에 해당하는 곳에 위치

# 이동할 좌표
to_x = 0
to_y = 0

# 이동 속도
character_speed = 0.6

# 적 enemy 똥캐릭터
enemy = pygame.image.load(os.path.join(image_path, "dung.png"))
enemy_size = enemy.get_rect().size # 이미지의 크기를 구해옴
enemy_width = enemy_size[0] # 캐릭터의 가로 크기
enemy_height = enemy_size[1] # 캐릭터의 세로 크기
enemy_x_pos = random.randint(0, screen_width - enemy_width) # 화면 가로 크기 내에서 랜덤으로 위치
enemy_y_pos = 0 # 화면 세로 크기 가장 위에 해당하는 곳에 위치


# 이벤트 루프
running = True 
while running:
    dt = clock.tick(30) # 게임화면의 초당 프레임 수를 설정

    # 2. 이벤트 처리(키보드, 마우스 등)
    for event in pygame.event.get():   
        if event.type == pygame.QUIT: 
            running = False 
        
        if event.type == pygame.KEYDOWN: # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    # 3. 게임 캐릭터 위치 정의        
    character_x_pos += to_x * dt
    
    # 0.5초마다 똥 떨어트리기
    enemy_y_pos += 10

    # 가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    
    # 똥 경계값 처리
    if enemy_y_pos > screen_height:
        enemy_y_pos = 0
        enemy_x_pos = random.randint(0, screen_width - enemy_width)

    # 충돌 처리를 위한 rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # 4. 충돌 처리
    if character_rect.colliderect(enemy_rect):
        print("충돌했어요")
        running = False

    # 5. 화면에 그리기
    screen.blit(background, (0, 0)) # 배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) # 적 그리기

    pygame.display.update() 

pygame.quit()
