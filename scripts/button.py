import pygame

class button(object):
    def __init__(self, x, y, width, height, value, color, rh=0):
        self.x, self.y, self.width, self.height, self.value, self.color, self.rh = x, y, width, height, value, color, rh
        pygame.font.init()
        self.bcol = (50, 50, 50)
        self.font = pygame.font.SysFont('arial', int(height / 2) - 5, True)
        self.text = self.font.render(self.value.capitalize(), True, self.color)

    def update(self):
        if self.colided("self"):
            self.bcol = (30, 30, 30)
        else:
            self.bcol = (50, 50, 50)

    def draw(self, win):
        pygame.draw.rect(win, self.bcol, (self.x, self.y, self.width, self.height))
        win.blit(self.text, (int(self.x * 2.82), int((self.y - self.rh) * 1.4)))

    def colided(self, str):
        mpos = pygame.mouse.get_pos()
        if mpos[0] >= self.x and mpos[1] >= self.y and mpos[0] <= self.x + self.width and mpos[1] <= self.y + self.height:
            if str == self.value:
                return self.value
            elif str == "self":
                return True
        else:
            return False
