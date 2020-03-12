import pygame

class gameplay(object):
    def __init__(self, size, win, winsize):
        self.size, self.win, self.winsize = size, win, winsize
        self.font = pygame.font.SysFont('arial', int(size / 5) - 5, True)
        self.xs, self.os = [], []
        self.board = [
            ['', '', ''],
            ['', '', ''],
            ['', '', '']
        ]
        self.turn = 'x'
        self.winner, self.ocp, self.text = 0, 0, 0

    def draw(self):
        pygame.draw.rect(self.win, (87, 88, 89), (0, 0, self.winsize, self.winsize + int(self.winsize / 6)))
        # draw board lines
        for x in range(2):
            self.drawBoardLines(x)
        self.drawCNC(self.xs, self.os)
        self.win.blit(self.text, (5, self.winsize + int(self.winsize * 0.05)))

    def update(self):
        self.xs.sort()
        self.sowin()
        self.mpos = pygame.mouse.get_pos()
        if self.winner == 0:
            self.text = self.font.render(f"it's {self.turn.upper()}'s turn", True, (10, 10, 10))
        elif self.winner == 't':
            self.text = self.font.render(f"Tie. Press space to play again", True, (10, 10, 10))
        else :
            self.text = self.font.render(f"{self.winner.upper()} won the game. Press space to play again", True, (10, 10, 10))
        if self.ocp == 9:
            self.winner = 't'
        pygame.display.update()

    # check where mouse clicked and place x or o
    def mPressed(self) :
        for x in range(3) :
            for y in range(3) :
                if self.mpos[0] <= self.size + self.size * x - 1 and self.mpos[1] <= self.size + self.size * y - 1 and self.mpos[0] >= self.size * x and self.mpos[1] >= self.size * y :
                    if self.ocp != 9 and self.board[y][x] == '' :
                        if self.turn == "x" :
                            self.turn = "o"
                            self.board[y][x] = 'x'
                            self.xs.append([x, y])
                            self.ocp += 1
                        elif self.turn == "o" :
                            self.turn = "x"
                            self.board[y][x] = 'o'
                            self.os.append([x, y])
                            self.ocp += 1
    #draw all x and o
    def drawCNC(self, xs, os):
        for x in xs:
            pygame.draw.line(self.win, (10, 10, 10), (x[0] * self.size + 5, x[1] * self.size + 5), (x[0] * self.size + self.size - 5, x[1] * self.size + self.size - 5), int(self.winsize * 0.015))
            pygame.draw.line(self.win, (10, 10, 10), (x[0] * self.size + self.size - 5, x[1] * self.size + 5), (x[0] * self.size + 5, x[1] * self.size + self.size - 5), int(self.winsize * 0.015))
        for o in os:
            pygame.draw.circle(self.win, (10, 10, 10), (o[0] * self.size + int(self.size / 2), o[1] * self.size + int(self.size / 2)), int(self.size / 2) - 5, int(self.winsize * 0.009))
    #draw board lines
    def drawBoardLines(self, x):
        pygame.draw.line(self.win, (10, 10, 10), (self.size + self.size * x, 0), (self.size + self.size * x, self.winsize), int(self.winsize * 0.007))
        pygame.draw.line(self.win, (10, 10, 10), (0, self.size + self.size * x), (self.winsize, self.size + self.size * x), int(self.winsize * 0.007))
        pygame.draw.line(self.win, (10, 10, 10), (0, self.winsize), (self.winsize, self.winsize), int(self.winsize * 0.007))
    #check if someone won
    def sowin(self):
        i = 0
        j = 0
        f = 'x'
        while j <= 2:
            while i <= 2:
                if self.board[i][0] == self.board[i][1] == self.board[i][2] == f:
                    self.winner = f
                if self.board[0][i] == self.board[1][i] == self.board[2][i] == f:
                    self.winner = f
                i += 1
            i = 0
            if self.board[0][0] == self.board[1][1] == self.board[2][2] == f:
                self.winner = f
            if self.board[0][2] == self.board[1][1] == self.board[2][0] == f:
                self.winner = f
            f = 'o'
            j += 1