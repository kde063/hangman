# from random import choice
# from os import system
# wordList = ["apple", "candy", "school", "student", "computer"]
# setting = 0

# while True:
#     if len(wordList) and setting == 0:
#         system("cls")
#         chance = 10
#         answer = ""
#         word = choice(wordList)
#         wordList.remove(word)
#         setting = 1

#     elif setting == 1:
#         end = 0
#         inp = input("한글자를 입력하세요\n")

#         if inp in word:
#             if inp not in answer:
#                 answer+=inp
#         else:
#             chance-=1

#         print("남은 기회:", chance)
            
#         for i in word:
#             if i in answer:
#                 print(i, end="")
#                 end+=1
#             else:
#                 print("-",end="")
#         print()

#         if chance == 0:
#             print("실패")
#             setting = 2

#         if end == len(word):
#             print("정답")
#             setting = 2

#     elif setting == 2:
#         ask = int(input("다시하기 Yes:1/No:2\n"))
#         if ask == 1:
#             setting = 0
            
#         elif ask == 2:
#             print("종료")
#             break

#         else:
#             print("error")
#             setting = 2
    
#     elif len(wordList) == 0 and setting == 0:
#         print("남은 단어가 없습니다.")
#         break

# chance = 5
# while chance !=0:   
#     for i in range(0,6-chance):
#         print(i)
#         print("chance", chance)
#         print("----------------")
#     chance-=1

import pygame
import sys

# Pygame 초기화
pygame.init()

# 화면 크기 설정
width, height = 400, 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Text Input Example")

# 폰트 설정
font = pygame.font.Font(None, 36)

# 입력 받은 문자열 초기화
input_text = ""

# 메인 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # 키 이벤트 처리
        elif event.type == pygame.KEYDOWN:
            # 엔터 키를 누르면 입력 완료
            if event.key == pygame.K_RETURN:
                print("입력된 문자열:", input_text)
                input_text = ""  # 입력 받은 문자열 초기화
            else:
                # 다른 키를 누르면 입력 받은 문자열에 추가
                input_text += event.unicode

    # 화면 업데이트
    screen.fill((0, 0, 0))  # 화면을 검은색으로 지우기
    text_surface = font.render(input_text, True, (255, 255, 255))
    screen.blit(text_surface, (10, 10))  # 입력된 문자열을 화면에 출력
    pygame.display.flip()

# Pygame 종료
pygame.quit()
sys.exit()
