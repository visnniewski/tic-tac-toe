import pygame
from scripts import button as bt

class menu(object):
    def __init__(self, size, win, winsize):
        self.size, self.win, self.winsize = size, win, winsize
        self.buttons = [
            bt.button(int(self.winsize / 10), int(self.winsize / 10), int(self.winsize - (self.winsize / 10) * 2), int(self.winsize / 5), "single-player", (10, 10, 10)),
            bt.button(int(self.winsize / 10), int(self.winsize / 10) + int(self.winsize / 5) + int(self.winsize / 14),
                      int(self.winsize - (self.winsize / 10) * 2), int(self.winsize / 5), "multi-player", (10, 10, 10), int(self.winsize / 14)),
            bt.button(int(self.winsize / 10), int(self.winsize / 10) + int(self.winsize / 5) * 2 + int(self.winsize / 14) * 2,
                      int(self.winsize - (self.winsize / 10) * 2), int(self.winsize / 5), "exit", (10, 10, 10), int(self.winsize / 14) * 2)
        ]
        self.ex = 0

    def update(self):
        pygame.display.update()
        for bt in self.buttons:
            if bt.colided("single-player"):
                self.ex = "single-player"
            elif bt.colided("multi-player"):
                self.ex = "multi-player"
            elif bt.colided("exit"):
                self.ex = bt.colided("exit")
            bt.update()

    def draw(self):
        pygame.draw.rect(self.win, (87, 88, 89), (0, 0, self.winsize, self.winsize + int(self.winsize / 6)))
        for bt in self.buttons:
            bt.draw(self.win)

    def clicked(self):
        return self.ex
