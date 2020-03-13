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
        self.scene, self.turn = "menu", 'x'
        self.sm = sceneManager.scene(self.scene, self.win, size, self.winsize)
        self.sm.update()
        self.mainLoop()

    def mainLoop(self):
        running = True
        clock = pygame.time.Clock()
        while running:
            self.update()
            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONUP:
                    if self.sm.scene == "multi-player" or self.sm.scene == "single-player":
                        if event.button == pygame.BUTTON_LEFT and self.sm.sc.winner == 0:
                            self.sm.sc.mPressed()
                    else:
                        if event.button == pygame.BUTTON_LEFT:
                            if self.sm.sc.clicked() == "multi-player":
                                self.sm.changeScene("multi-player")
                            elif self.sm.sc.clicked() == "single-player":
                                self.sm.changeScene("single-player")
                            elif self.sm.sc.clicked() == "exit":
                                running = False

                if event.type == pygame.KEYUP:
                    if self.sm.scene == "multi-player" or self.sm.scene == "single-player":
                        if event.key == pygame.K_SPACE and self.sm.sc.winner == 'x' or self.sm.sc.winner == 'o' or self.sm.sc.winner == 't':
                            self.sm.sc.winner, self.sm.sc.ocp, self.sm.sc.turn = 0, 0, 'x'
                            self.sm.sc.board = [['', '', ''], ['', '', ''], ['', '', '']]
                            self.sm.sc.xs, self.sm.sc.os = [], []
                        if event.key == pygame.K_ESCAPE:
                            self.sm.changeScene("menu")
            clock.tick(60)
        pygame.quit()

    def draw(self):
        self.sm.sc.draw()

    def update(self):
        self.sm.sc.update()



if __name__ == "__main__":
    main(120)
