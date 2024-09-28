import pygame
import sys

# Pygame 초기화
pygame.init()

# 화면 설정
SCREEN_WIDTH = 1200  # 1000 픽셀 선을 보기 위해 충분히 큰 너비 설정
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("1000 픽셀 선 보기")

# 색상 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# 배경 색상 채우기
screen.fill(WHITE)

# 1000 픽셀 길이의 선 그리기
start_pos = (100, SCREEN_HEIGHT // 2)  # 시작 위치 (x, y)
end_pos = (1100, SCREEN_HEIGHT // 2)   # 끝 위치 (x, y) -> 1000 픽셀 길이
pygame.draw.line(screen, RED, start_pos, end_pos, 5)  # 선 두께 5

# 화면 업데이트
pygame.display.flip()

# 이벤트 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Pygame 종료
pygame.quit()
sys.exit()
