from froggerlib.player_controllable import PlayerControllable
import assets
import pygame
import math


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
        self._timer = 0
        self._lives = 4
        self._highest_y = y
        self._total_score = 0
        self._score = 0
        return
    
    def getScore(self):
        return self._score
    
    def addScore(self, score):
        self._score += score
        self._total_score += score
        return

    def getLives(self):
        return self._lives
    
    def getTimer(self):
        return self._timer

    def getAlive(self):
        return not self._is_dead

    def getResetReady(self):
        return self._ready_to_reset

    def reset(self):
        if self._lives < 0:
            return
        self._score = 0
        self._is_dead = False
        self._ready_to_reset = False
        self._frame = 0
        self._death_frame = 0
        self._tick_divisor = 0
        self.setDesiredX(self._start_x)
        self.setDesiredY(self._start_y)
        self.setX(self._start_x)
        self.setY(self._start_y)
        self._timer = 0
        self._highest_y = self._start_y
        return
    
    def getTotalScore(self):
        return self._total_score
    
    def move(self):
        if not self.getRide():
            self.setDesiredX(math.floor(self.getDesiredX()/32+0.5)*32)
            self.setDesiredY(math.floor(self.getDesiredY()/32+0.5)*32)
        super().move()

    def kill(self):
        if not self._is_dead:
            if self.getRide():
                riders = self.getRide().getRiders()
                if self in riders:
                    riders.remove(self)
            self.setRide(None)
            self._is_dead = True
            self._death_frame = 0
            self._tick_divisor = 0
            self._lives -= 1
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
            if self._tick_divisor == 0:
                self._death_frame += 1
            if self._death_frame < len(assets.death):
                surface.blit(
                    assets.death[self._death_frame], (self.getX(), self.getY()))
            elif self._death_frame == 10:
                self._ready_to_reset = True
                self.reset()
            else:
                surface.blit(assets.death[len(
                    assets.death)-1], (self.getX(), self.getY()))
        else:        
            if self.getY() < self._highest_y and self.getDesiredY() == self.getY():
                self._highest_y = self.getY()
                self._score += 10
                self._total_score += 10
            self._timer += 1
            if self._timer % 6 == 0:
                self._score += 1
                self._total_score += 1
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
