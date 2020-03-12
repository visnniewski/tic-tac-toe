import random

class bot(object):
    def __init__(self):
        pass

    def update(self, os, xs):
        x, y = 0, 0
        should_restart = True
        while should_restart:
            x, y = random.randint(0, 2), random.randint(0, 2)
            should_restart = False
            for op in os:
                if op[0] == x and op[1] == y:
                    should_restart = True
            for op in xs:
                if op[0] == x and op[1] == y:
                    should_restart = True
        print(x, y)
        return [True, x, y]
