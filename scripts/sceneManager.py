from scripts import gameplay, menu

class scene(object):
    def __init__(self, scene, win, size, winsize):
        self.scene = scene
        self.win, self.size, self.winsize = win, size, winsize
        self.sc = "menu"

    def changeScene(self, newScene):
        self.scene = newScene
        self.update()

    def update(self):
        if self.scene == "menu":
            self.sc = menu.menu(self.size, self.win, self.winsize)
        if self.scene == "multi-player":
            self.sc = gameplay.gameplay(self.size, self.win, self.winsize)
        if self.scene == "single-player":
            self.sc = gameplay.gameplay(self.size, self.win, self.winsize, "single")

