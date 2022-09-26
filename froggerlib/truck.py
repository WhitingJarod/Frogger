from froggerlib.dodgeable import Dodgeable
import random
import assets


class Truck(Dodgeable):

    def __init__(self, x=0, y=0, w=0, h=0, dx=0, dy=0, s=0):
        Dodgeable.__init__(self, x, y, w, h, dx, dy, s)
        self.setDesiredY(self.getY())
        self.setDesiredX(-128)
        return

    def __str__(self):
        s = "Truck<"+Dodgeable.__str__(self)+">"
        return s

    def __repr__(self):
        return str(self)

    def move(self):
        Dodgeable.move(self)
        if self.getX() + self.getWidth() < 0:
            self.setX(15*32)

    def draw(self, surface):
        surface.blit(assets.truck, (self.getX(), self.getY()))


def test():
    r = Truck(5, 5, 10, 10, -15, 10, 4)
    print(r)
    while not r.atDesiredLocation():
        r.move()
        print(r)
    return


if __name__ == "__main__":
    test()
