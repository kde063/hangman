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
        for i in range(1, len(self.word) + 1):
            Text = self.myFont.render("_", (0 + i*10, 0), (255, 255, 255))
            self.screen.blit(Text, (200, 100))

    def text(self):
        myText = self.myFont.render("Hello World ",  True, (0, 0, 255))
        self.screen.blit(myText, (100, 100))

    def gameOver(self):
        if self.chance == 0:
            print("실패")
            self.running = False
        
        elif self.gameCheck and self.running != 0:
            print("성공")

main = Main()
main.start()