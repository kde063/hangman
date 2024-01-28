from random import choice
from os import system
wordList = ["apple", "candy", "school", "student", "computer"]
setting = 0

def draw(coord ,chance): #chance = 5

    delList = [[9, 5, 8, 5], #허리
               [5, 6, 6, 7], #팔(오)
               [5, 4, 6, 3], #팔(왼)
               [8, 6, 9, 7],#다리(오)
               [8, 4, 9, 3]]#다리(왼)

    if chance == 5:
        pass
    else:
        coord[delList[chance][0]][delList[chance][1]] = 0
        coord[delList[chance][2]][delList[chance][3]] = 0

    for i in coord:
        for j in i:
            if j == 0:
                print(" ", end="")
            else:
                print("1", end="")

        print("\n", end="")
    

while True:
    if len(wordList) and setting == 0:
        system("cls")
        chance = 5
        answer = ""
        word = choice(wordList)
        wordList.remove(word)
        setting = 1
        coord = [[0,0,0,1,1,1,1,1,0,0,0],
                 [0,0,0,1,0,0,0,1,0,0,0],
                 [0,0,0,1,0,0,0,1,0,0,0],
                 [0,0,0,1,1,1,1,1,0,0,0],
                 [0,0,0,0,0,1,0,0,0,0,0],
                 [0,0,0,0,1,1,1,0,0,0,0],
                 [0,0,0,1,0,1,0,1,0,0,0],
                 [0,0,0,0,0,1,0,0,0,0,0],
                 [0,0,0,0,1,0,1,0,0,0,0],
                 [0,0,0,1,0,0,0,1,0,0,0]]

    elif setting == 1:
        end = 0
        inp = input("한글자를 입력하세요\n")

        if inp in word:
            if inp not in answer:
                answer+=inp
        else:
            chance-=1
        
        draw(coord, chance)
        print("남은 기회:", chance)
        
        for i in word:
            if i in answer:
                print(i, end="")
                end+=1
            else:
                print("-",end="")
        print()

        if chance == 0:
            print("실패")
            setting = 2

        if end == len(word):
            print("정답")
            setting = 2

    elif setting == 2:
        ask = int(input("다시하기 Yes:1/No:2\n"))
        if ask == 1:
            setting = 0
            
        elif ask == 2:
            print("종료")
            break

        else:
            print("error")
            setting = 2
    
    elif len(wordList) == 0 and setting == 0:
        print("남은 단어가 없습니다.")
        break

