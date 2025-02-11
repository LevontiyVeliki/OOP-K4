class Pupil:
    def __init__(self):
        self.knowledge = []
    def take(self, info):
        self.knowledge.append(info)
    def lose(self):
        from random import randrange
        if self.knowledge:
            i = randrange(len(self.knowledge))
            del self.knowledge[i]