import pygame
import sys

# Pygame 초기화
pygame.init()

# 화면 크기 설정
width, height = 400, 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Text Printing Example")

# 폰트 설정
font = pygame.font.Font(None, 36)

# 텍스트를 찍을 문자열
text = "e"*3

# 문자열의 각 문자를 차례로 찍기
for i, char in enumerate(text):
    # 문자를 이미지로 렌더링
    text_surface = font.render(char, True, (255, 255, 255))
    
    # 문자의 위치 계산
    x = 50 + i * 40
    y = height // 2 - text_surface.get_height() // 2
    
    # 화면에 문자 표시
    screen.blit(text_surface, (x, y))

# 화면 업데이트
pygame.display.flip()

# 메인 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 화면 업데이트
    pygame.display.flip()

# Pygame 종료
pygame.quit()
sys.exit()
