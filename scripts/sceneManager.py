from scripts import gameplay

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
            pass
        elif self.scene == "gameplay":
            self.sc = gameplay.gameplay(self.size, self.win, self.winsize)

