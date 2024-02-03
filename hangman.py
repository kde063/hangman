import pygame as py
from random import choice
from time import sleep

class Main:
    def __init__(self):
        py.init()
        self.size = (900, 600)
        self.screen = py.display.set_mode(self.size)
        self.running = True
        self.BLACK = (0, 0, 0)
        self.chance = 5
        self.WHITE = (255, 255, 255)
        self.gameCheck = False
        self.tempList = ["apple", "candy", "school", "student", "computer"]
        self.myFont = py.font.SysFont("malgungothic", 50)
        self.word = choice(self.tempList)
        self.answer = ""
        self.end = 0
        self.tempAnswer = ""
        self.inputText = ""

    def loop(self):
        for event in py.event.get():
            if event.type == py.QUIT:
                return False
                # 키 이벤트 처리
            if event.type == py.KEYDOWN:
                # 엔터 키를 누르면 입력 완료
                if event.key == py.K_RETURN:
                    print("입력된 문자열:", self.inputText)
                    self.gameManager()
                    if not self.running :
                        return False
                    self.inputText = ""  # 입력 받은 문자열 초기화
                else:
                    # 다른 키를 누르면 입력 받은 문자열에 추가
                    self.inputText = event.unicode

        self.write(self.inputText)
        return True 
      
    def write(self, text):
        # 화면 업데이트
        textSurface = self.myFont.render(text, True, (255, 255, 255))
        self.screen.blit(textSurface, (10, 10))  # 입력된 문자열을 화면에 출력
    
    def writeResult(self, text):
        self.screen.fill(self.BLACK)
        textSurface = self.myFont.render(text, True, (255, 255, 255))
        self.screen.blit(textSurface, (10, 10))  # 입력된 문자열을 화면에 출력
        sleep(2)

    
    def start(self):
        print(self.word)  #temp
        while self.running:
            self.screen.fill(self.BLACK)
            self.running = self.loop()
            self.draw()
            self.blank()
            self.text()
            py.display.flip()
            
        py.quit()
    def draw(self):
        self.head()
        self.lArm(self.chance)
        self.rArm(self.chance)
        self.lLeg(self.chance)
        self.rLeg(self.chance)

    def head(self):
        py.draw.circle(self.screen, self.WHITE, (300, 200), 50, 1)
        py.draw.circle(self.screen, self.WHITE, (280, 190), 3, 3)
        py.draw.circle(self.screen, self.WHITE, (320, 190), 3, 3)
        py.draw.line(self.screen, self.WHITE, (290, 215), (310, 215), 1)
        py.draw.line(self.screen, self.WHITE, (300, 250), (300, 400), 1)
        
    def rArm(self, chance):
        if chance >= 2:
            py.draw.line(self.screen, self.WHITE, (300, 300), (240, 240), 1)

    def lArm(self, chance):
        if chance >= 3:
            py.draw.line(self.screen, self.WHITE, (300, 300), (360, 240), 1)

    def rLeg(self, chance):
        if chance >= 4:
            py.draw.line(self.screen, self.WHITE, (300, 400), (400, 450), 1)

    def lLeg(self, chance):
        if chance >= 5:
            py.draw.line(self.screen, self.WHITE , (300, 400), (200, 450), 1 )

    def blank(self):
        blank = "_" * len(self.word)

        for i, char in enumerate(blank):
            text_surface = self.myFont.render(char, True, (255, 255, 255))

            x = 500 + i * 40
            y = 400

            self.screen.blit(text_surface, (x, y))

    def text(self):
        for i, char in enumerate(self.answer):
            textSurface = self.myFont.render(char, True, (255, 255, 255))

            x = 500 + i * 40
            y = 390

            self.screen.blit(textSurface, (x, y))

    

    def gameManager(self):
        # print("chance: ", self.chance)
        # inp = input()
        self.answer = ""
        self.end = 0

        if self.inputText in self.word:
            if self.inputText not in self.tempAnswer:
                self.tempAnswer+=self.inputText
            else:
                self.chance-=1
        else:
            self.chance-=1
        
        for i in self.word:
            if i in self.tempAnswer:
                self.answer += i
                self.end += 1

            else:
                self.answer += " "

        if self.end == len(self.answer):
            self.gameCheck = True
    
        if self.chance == 0:
            print("실패")
            self.writeResult("실패")
            self.running = False
        
        elif self.gameCheck and self.running:
            print("성공")
            # self.writeResult("성공")
            self.writeResult("성공")
            sleep(2)
            self.running = False

main = Main()
main.start()