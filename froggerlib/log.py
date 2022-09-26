from froggerlib.rideable import Rideable
import pygame
import assets
import random

class Log(Rideable):

    def __init__(self, y=0, s=0):
        self._width = random.randint(3, random.randint(3, 10))*32
        x = 0
        if s > 0:
            self._direction = 1
            x = -self._width
        else:
            self._direction = -1
            s = -s
            x = 15*32+self._width
        Rideable.__init__(self, x, y+1, self._width, 30, 0, 0, s)
        self.setDesiredY(y)
        if self._direction < 1:
            self.setDesiredX(-self._width-128)
        else:
            self.setDesiredX(15*32+128)
        return
    
    def getLengthOnScreen(self):
        if self.getX() < 0:
            return self._width+self.getX()
        else:
            return min(self._width, 15*32-self.getX())

    def draw(self, surface: pygame.Surface):
        for n in range(self._width//32):
            if n == 0:
                surface.blit(assets.log[0], (self.getX()+n*32, self.getY()))
            elif n == self._width/32-1:
                surface.blit(assets.log[2], (self.getX()+n*32, self.getY()))
            else:
                surface.blit(assets.log[1], (self.getX()+n*32, self.getY()))


    def __str__(self):
        s = "Log<"+Rideable.__str__(self)+">"
        return s

    def __repr__(self):
        return str(self)

def test():
    r = Log(5,5,10,10, -15, 10, 4)
    print(r)
    while not r.atDesiredLocation():
        r.move()
        print(r)
    return

if __name__ == "__main__":
    test()
