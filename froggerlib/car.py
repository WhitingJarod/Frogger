from froggerlib.dodgeable import Dodgeable
import random
import assets


class Car(Dodgeable):

    def __init__(self, x=0, y=0, w=0, h=0, dx=0, dy=0, s=0, t=0):
        Dodgeable.__init__(self, x, y, w, h, dx, dy, s)
        self.setDesiredY(self.getY())
        if t < 1:
            self._sprite = assets.car
            self.setDesiredX(-128)
            self._direction = -1
        else:
            self._sprite = assets.harvester
            self.setDesiredX(15*32 + 128)
            self._direction = 1
        return

    def move(self):
        Dodgeable.move(self)
        if self._direction < 1:
            if self.getX() + self.getWidth() < 0:
                self.setX(15*32)
        else:
            if self.getX() > 15*32:
                self.setX(-self.getWidth())
        return

    def draw(self, surface):
        surface.blit(self._sprite, (self.getX(), self.getY()))

    def __str__(self):
        s = "Car<"+Dodgeable.__str__(self)+">"
        return s

    def __repr__(self):
        return str(self)


def test():
    r = Car(5, 5, 10, 10, -15, 10, 4)
    print(r)
    while not r.atDesiredLocation():
        r.move()
        print(r)
    return


if __name__ == "__main__":
    test()
