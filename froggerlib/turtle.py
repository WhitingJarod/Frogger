from froggerlib.rideable import Rideable
import assets
import random
import math

class Turtle(Rideable):

    def __init__(self, y, s):
        self._width = random.randint(2, 5)*32
        self._countdown = random.randint(30*3, 30*8)
        self._up = True
        self._sprite = assets.turts[1]
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
        
    def move(self):
        if self._countdown < 0:
            self._countdown += 1
            if self._countdown == -20:
                self._sprite = assets.turts[3]
            elif self._countdown == -1:
                self._sprite = assets.turts[1]
                self._countdown = random.randint(30*3, 30*6)
                self._up = True
        else:
            self._countdown -= 1
            if self._countdown == 20:
                self._sprite = assets.turts[3]
            elif self._countdown == 1:
                self._sprite = assets.turts[4]
                self._countdown = -random.randint(30*2, 30*4)
                self._up = False
            elif self._countdown > 20:
                n = math.floor((self._countdown/10)%4)
                if n == 3:
                    n = 1
                self._sprite = assets.turts[n]
        if not self._up:
            for rider in self.getRiders():
                rider.kill()
        Rideable.move(self)
        return
        
    def draw(self, surface):
        for n in range(self._width//32):
            surface.blit(self._sprite, (self.getX()+n*32+2, self.getY()))

    def __str__(self):
        s = "Turtle<"+Rideable.__str__(self)+">"
        return s

    def __repr__(self):
        return str(self)

def test():
    r = Turtle(5,5,10,10, -15, 10, 4)
    print(r)
    while not r.atDesiredLocation():
        r.move()
        print(r)
    return

if __name__ == "__main__":
    test()
