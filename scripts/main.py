import pygame
from scripts import sceneManager

class main(object):
    def __init__(self, size):
        pygame.init()
        pygame.font.init()
        self.size = size
        self.winsize = self.size * 3 + 2
        pygame.display.set_caption("Tic Tac Toe")
        self.win = pygame.display.set_mode((self.winsize, self.winsize + int(self.winsize / 6)))
        self.scene, self.turn = "gameplay", 'x'
        self.sm = sceneManager.scene(self.scene, self.win, size, self.winsize)
        self.sm.update()
        self.mainLoop()

    def mainLoop(self):
        running = True
        clock = pygame.time.Clock()
        while running:
            self.update()
            self.draw()
            for event in pygame.event.get() :
                if event.type == pygame.QUIT :
                    running = False
                if event.type == pygame.MOUSEBUTTONUP :
                    if event.button == pygame.BUTTON_LEFT and self.sm.sc.winner == 0:
                        self.sm.sc.mPressed()
                if event.type == pygame.KEYUP :
                    if event.key == pygame.K_SPACE and self.sm.sc.winner == 'x' or self.sm.sc.winner == 'o' or self.sm.sc.winner == 't' and self.sm.scene != "menu":
                        self.sm.sc.winner, self.sm.sc.ocp = 0, 0
                        self.sm.sc.board = [['', '', ''], ['', '', ''], ['', '', '']]
                        self.sm.sc.xs, self.sm.sc.os = [], []
                    if event.key == pygame.K_ESCAPE and self.sm.scene != "menu":
                        self.sm.changeScene("menu")
            clock.tick(60)
        pygame.quit()

    def draw(self):
        self.sm.sc.draw()

    def update(self):
        self.sm.sc.update()



if __name__ == "__main__":
    main(120)
