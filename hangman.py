import openai

openai.api_key = "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"

messages = []


theme = input("테마를 입력해주세요\n")
user_content = theme + "을 테마로 하는 영단어 10개만 알려줘 그리고 번호와 단어는 빼줘"
messages.append({"role" : "user", "content" : f"{user_content}"})

completion = openai.ChatCompletion.create(model = "gpt-3.5-turbo", messages = messages)

assistant_content = completion.choices[0].message["content"].strip()

messages.append({"role": "assistant", "content": f"{assistant_content}"})

assistant_content = ''.join(assistant_content)
assistant_content = [i.split()[1] for i in ''.join(assistant_content).split('\n')]

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
        self.chance = 7
        self.WHITE = (255, 255, 255)
        self.gameCheck = False
        self.tempList = assistant_content
        self.myFont = py.font.SysFont("malgungothic", 30)
        self.blankFont = py.font.SysFont("malgungothic", 60)
        self.word = choice(self.tempList).lower()
        self.end = 0
        self.answer = ""
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

            if event.type == py.MOUSEBUTTONDOWN:
                print(py.mouse.get_pos())

        self.write(self.inputText)
        return True 
      
    def write(self, text):
        # 화면 업데이트
        textSurface = self.myFont.render(text, True, (255, 255, 255))
        self.screen.blit(textSurface, (10, 10))  # 입력된 문자열을 화면에 출력

    def start(self):
        while self.running:
            self.screen.fill(self.BLACK)
            self.running = self.loop()
            self.draw()
            self.blank()
            self.text()
            py.display.flip()
        
        sleep(2)
        py.quit()
        
    def draw(self):
        self.frame()
        self.head(self.chance)
        self.body(self.chance)
        self.lArm(self.chance)
        self.rArm(self.chance)
        self.lLeg(self.chance)
        self.rLeg(self.chance)
        self.face(self.chance)

    def face(self, chance):
        if chance <= 0:
            py.draw.line(self.screen, self.WHITE, (491, 118), (509, 119), 1)

    def rArm(self, chance):
        if chance <= 1:
            py.draw.line(self.screen, self.WHITE, (500, 190), (567, 236), 1)

    def lArm(self, chance):
        if chance <= 2:
            py.draw.line(self.screen, self.WHITE, (500, 190), (439, 248), 1)

    def rLeg(self, chance):
        if chance <= 3:
            py.draw.line(self.screen, self.WHITE, (500, 295), (565, 348), 1)

    def lLeg(self, chance):
        if chance <= 4:
            py.draw.line(self.screen, self.WHITE , (500, 295), (440, 353), 1 )

    def body(self, chance):
        if chance <= 5:
            py.draw.line(self.screen, self.WHITE, (500, 150), (500, 295), 1)

    def head(self, chance):
        if chance <= 6:
            py.draw.circle(self.screen, self.WHITE, (500, 100), 50, 1)
            py.draw.circle(self.screen, self.WHITE, (480, 90), 3, 3)
            py.draw.circle(self.screen, self.WHITE, (520, 90), 3, 3)

    def frame(self):
        py.draw.line(self.screen, self.WHITE, (500, 47), (500, 9), 1)
        py.draw.line(self.screen, self.WHITE, (370, 9), (500, 9), 1)
        py.draw.line(self.screen, self.WHITE, (370, 9), (370, 349), 1)
        py.draw.line(self.screen, self.WHITE, (460, 350), (300, 350), 1)

    def blank(self):
        blank = "_" * len(self.word)

        for i, char in enumerate(blank):
            text_surface = self.blankFont.render(char, True, (255, 255, 255))

            x = 50 + i * 40
            y = 400

            self.screen.blit(text_surface, (x, y))

    def text(self):
        for i, char in enumerate(self.answer):
            textSurface = self.myFont.render(char, True, (255, 255, 255))

            x = 50 + i * 40
            y = 405

            self.screen.blit(textSurface, (x, y))

    

    def gameManager(self):
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
            self.write("실패")
            self.running = False
        
        elif self.gameCheck and self.running:
            print("성공")
            self.write("성공")
            self.running = False

main = Main()
main.start()