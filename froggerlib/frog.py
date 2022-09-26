from froggerlib.player_controllable import PlayerControllable
import assets
import pygame


class Frog(PlayerControllable):

    def __init__(self, x=0, y=0, w=0, h=0, dx=0, dy=0, s=0, hg=0, vg=0):
        self._start_x = x
        self._start_y = y
        PlayerControllable.__init__(self, x, y, w, h, dx, dy, s, hg, vg)
        self._is_dead = False
        self._ready_to_reset = False
        self._frame = 0
        self._death_frame = 0
        self._tick_divisor = 0
        return

    def getAlive(self):
        return not self._is_dead

    def getResetReady(self):
        return self._ready_to_reset

    def reset(self):
        self._is_dead = False
        self._ready_to_reset = False
        self._frame = 0
        self._death_frame = 0
        self._tick_divisor = 0
        self.setDesiredX(self._start_x)
        self.setDesiredY(self._start_y)
        self.setX(self._start_x)
        self.setY(self._start_y)
        return

    def kill(self):
        if not self._is_dead:
            self._is_dead = True
            self._death_frame = 0
            self._tick_divisor = 0
        return

    def up(self):
        if self._is_dead or self.getY() <= 64:
            return
        super().up()
        self._tick_divisor = 0
        self._frame = 1

    def left(self):
        if self._is_dead or self.getX() <= 0:
            return
        super().left()
        self._tick_divisor = 0
        self._frame = 3

    def down(self):
        if self._is_dead or self.getY() >= 14*32:
            return
        super().down()
        self._tick_divisor = 0
        self._frame = 5

    def right(self):
        if self._is_dead or self.getX() >= 14*32:
            return
        super().right()
        self._tick_divisor = 0
        self._frame = 7

    def draw(self, surface):
        self._tick_divisor = (self._tick_divisor+1) % 5
        if self._is_dead:
            if self._death_frame < len(assets.death):
                surface.blit(
                    assets.death[self._death_frame], (self.getX(), self.getY()))
                if self._tick_divisor == 0:
                    self._death_frame += 1
            else:
                self._ready_to_reset = True
                surface.blit(assets.death[len(
                    assets.death)-1], (self.getX(), self.getY()))
        else:
            if self._frame % 2 == 1 and self._tick_divisor == 0:
                self._frame -= 1
            surface.blit(
                assets.frog[self._frame], (self.getX(), self.getY()))
        return

    def __str__(self):
        s = "Frog<"+PlayerControllable.__str__(self)+">"
        return s

    def __repr__(self):
        return str(self)


def test():
    f = Frog()
    f.setHorizontalGap(15)
    f.setVerticalGap(15)
    f.setSpeed(2)

    print(f)
    f.up()
    print(f)
    while not f.atDesiredLocation():
        f.move()
        print(f)

    return


if __name__ == "__main__":
    test()
