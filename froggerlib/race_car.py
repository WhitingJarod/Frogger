from froggerlib.dodgeable import Dodgeable
import assets
import random
import pygame


class RaceCar(Dodgeable):

    def __init__(self, x=0, y=0, w=0, h=0, dx=0, dy=0, mins=0, maxs=0, direction=1):
        Dodgeable.__init__(self, x, y, w, h, dx, dy, mins)
        self.mMinSpeed = mins
        self.mMaxSpeed = maxs
        self.mSpeedCount = 0
        self.mSpeedCountMax = random.randint(10, 30)
        self.mDirection = direction
        if direction < 1:
            self.setDesiredX(-128)
        else:
            self.setDesiredX(15*32 + 128)
        self.setDesiredY(self.getY())
        if direction < 1:
            self._sprite = assets.racer_left
        else:
            self._sprite = assets.racer_right
        return

    def getMinSpeed(self):
        return self.mMinSpeed

    def getMaxSpeed(self):
        return self.mMaxSpeed

    def setMinSpeed(self, mins):
        self.mMinSpeed = mins
        return

    def setMaxSpeed(self, maxs):
        self.mMaxSpeed = maxs
        return

    def move(self):
        if self.mSpeedCount % self.mSpeedCountMax == 0:
            self.setSpeed(random.randint(self.mMinSpeed, self.mMaxSpeed))
        self.mSpeedCount += 1
        Dodgeable.move(self)
        if self.mDirection < 1:
            if self.getX() + self.getWidth() < 0:
                self.setX(15*32)
        else:
            if self.getX() > 15*32:
                self.setX(-self.getWidth())
        return

    def draw(self, surface: pygame.Surface):
        surface.blit(self._sprite, (self.getX(), self.getY()))

    def __str__(self):
        s = "RaceCar<" + \
            Dodgeable.__str__(self)+","+str(self.mMinSpeed) + \
            ","+str(self.mMaxSpeed)+">"
        return s

    def __repr__(self):
        return str(self)


def test():
    r = RaceCar(5, 5, 10, 10, -15, 10, 2, 5)
    print(r)
    while not r.atDesiredLocation():
        r.move()
        print(r)
    return


if __name__ == "__main__":
    test()
