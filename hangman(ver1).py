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