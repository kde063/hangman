import pygame as py
from random import choice

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
        self.myFont = py.font.SysFont(None, 50)
        self.word = choice(self.tempList)
        self.answer = ""
        self.end = 0
        self.tempAnswer = ""

    def loop(self):
        for event in py.event.get():
            if event.type == py.QUIT:
                self.running = True
                py.quit()

    def start(self):
        while self.running:
            self.loop()
            self.draw()
            self.blank()
            self.text()
            py.display.flip()
            self.gameManager()
            self.gameOver()
            py.display.flip()

    def draw(self):
        self.screen.fill(self.BLACK)
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
        inp = input()  #temp
        
        if inp in self.word:
            if inp not in self.tempAnswer:
                self.tempAnswer+=inp
        else:
            self.chance-=1
        
        for i in self.word:
            if i in self.tempAnswer:
                self.tempAnswer += i

            else:
                self.tempAnswer += " "

        if self.end == len(self.answer):
            self.gameCheck = True
    
    def gameOver(self):
        if self.chance == 0:
            print("실패")
            self.running = False
        
        elif self.gameCheck and self.running:
            print("성공")
            self.running = False

main = Main()
main.start()