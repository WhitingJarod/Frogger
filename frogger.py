import pygame
import froggerlib
import assets
import random

#! Rules broken:
#! 1. The froggerlib code must not be changed.
#! 2. The Frogger class must contain all of the logic.

#! Extra challenges completed:
#! 1. Restart option.
#! 2. Time limit.
#! 3. Allow frog to complete level by filling all homes.

class Frogger():
    """The main game class.  This is the class that you will be modifying
    to implement the game logic for Frogger."""

    def __init__(self, width, height):
        """Initialize the game state."""
        assets.init()
        self._frog = froggerlib.Frog(
            ((width/32)//2)*32, height-64,
            32, 32,
            0, 0, 15,
            32, 32)
        self._frog.setDesiredX(self._frog.getX())
        self._frog.setDesiredY(self._frog.getY())
        self._cars = []
        self._water = froggerlib.Water(0, height-32*13, 32*15, 32*5)
        racer1 = froggerlib.RaceCar(
            width-32*6, height-32*3+3, 31, 27, 0, 0, 6, 12, -1)
        racer2 = froggerlib.RaceCar(
            width-32*6, height-32*6+3, 31, 27, 0, 0, 6, 12, 1)
        car1 = froggerlib.Car(
            32*3, height-32*5+7, 29, 19, 0, 0, 4, 0)
        car2 = froggerlib.Car(
            32*5, height-32*5+7, 29, 19, 0, 0, 4, 0)
        car3 = froggerlib.Car(
            32*10, height-32*5+7, 29, 19, 0, 0, 4, 0)
        car4 = froggerlib.Car(
            32*14, height-32*5+7, 29, 19, 0, 0, 4, 0)
        harvester1 = froggerlib.Car(
            32*2, height-32*4+5, 27, 23, 0, 0, 3, 1)
        harvester2 = froggerlib.Car(
            32*7, height-32*4+5, 27, 23, 0, 0, 3, 1)
        harvester3 = froggerlib.Car(
            32*11, height-32*4+5, 27, 23, 0, 0, 3, 1)
        truck1 = froggerlib.Truck(
            32*2, height-32*7+7, 53, 19, 0, 0, 2)
        truck2 = froggerlib.Truck(
            32*8, height-32*7+7, 53, 19, 0, 0, 2)
        self._cars.append(racer1)
        self._cars.append(racer2)
        self._cars.append(car1)
        self._cars.append(car2)
        self._cars.append(car3)
        self._cars.append(car4)
        self._cars.append(harvester1)
        self._cars.append(harvester2)
        self._cars.append(harvester3)
        self._cars.append(truck1)
        self._cars.append(truck2)
        self._logs = [[(4, 10), []],[(-6, 11), []],[(5, 13), []]]
        self._turtles = [[(-3, 9), []], [(-2, 12), []]]
        self._homes = []
        home1 = froggerlib.Home(32, height-32*14, 32, 32)
        home2 = froggerlib.Home(32*4, height-32*14, 32, 32)
        home3 = froggerlib.Home(32*7, height-32*14, 32, 32)
        home4 = froggerlib.Home(32*10, height-32*14, 32, 32)
        home5 = froggerlib.Home(32*13, height-32*14, 32, 32)
        self._homes.append(home1)
        self._homes.append(home2)
        self._homes.append(home3)
        self._homes.append(home4)
        self._homes.append(home5)
        self._width = width
        self._height = height
        self._score = 0
        self._max_lane = 0

    def getFrog(self) -> froggerlib.Frog:
        """Return a reference to the frog."""
        return self._frog

    def getStages(self) -> list[froggerlib.Stage]:
        """Return a reference to this list."""
        return self._stages

    def getCars(self) -> list[froggerlib.Car]:
        """Return a reference to this list."""
        return self._cars

    def getLogs(self) -> list[froggerlib.Log]:
        """Return a reference to this list."""
        return self._logs

    def getTurtles(self) -> list[froggerlib.Turtle]:
        """Return a reference to this list."""
        return self._turtles

    def getMovables(self) -> list[froggerlib.Movable]:
        """Return a reference to this list."""
        return self._movables

    def evolve(self, dt: float):
        """Update the game state by dt seconds."""
        self._frog.move()
        for lane in self._logs:
            for log in lane[1]:
                    log.supports(self._frog)
        for lane in self._turtles:
            for turtle in lane[1]:
                    turtle.supports(self._frog)
        if self._frog.getX() + self._frog.getWidth()/2 < 0:
            self._frog.setX(0)
            self._frog.setDesiredX(0)
            self._frog.kill()
        elif self._frog.getX() - self._frog.getWidth()/2 > self._width-32:
            self._frog.setX(self._width-32)
            self._frog.setDesiredX(self._width-32)
            self._frog.kill()
        """if self._frog.getY() < 64:
            self._frog.setY(64)
            self._frog.setDesiredY(64)
            self._frog.kill()
        elif self._frog.getY() > self._height-64:
            self._frog.setY(self._height-64)
            self._frog.setDesiredY(self._height-64)
            self._frog.kill()"""
        for car in self._cars:
            car.move()
            if car.hits(self._frog):
                self._frog.kill()
        for i in range(len(self._logs)):
            lane = self._logs[i]
            on_screen = 0
            spawn = True
            for l in range(len(lane[1])-1, -1, -1):
                log = lane[1][l]
                log.move()
                on_screen += log.getLengthOnScreen()
                if lane[0][0] < 1:
                    if log.getX() + log._width > self._width:
                        spawn = False
                    if log.getX() + log._width < 0:
                        lane[1].pop(l)
                else:
                    if log.getX() < 0:
                        spawn = False
                    if log.getX() > self._width:
                        lane[1].pop(l)
            if on_screen < 8*32 and spawn and random.random() < 0.03:
                log = froggerlib.Log(self._height-lane[0][1]*32, lane[0][0])
                lane[1].append(log)

        for i in range(len(self._turtles)):
            lane = self._turtles[i]
            on_screen = 0
            spawn = True
            for l in range(len(lane[1])-1, -1, -1):
                turtle = lane[1][l]
                turtle.move()
                on_screen += turtle.getLengthOnScreen()
                if lane[0][0] < 1:
                    if turtle.getX() + turtle._width > self._width:
                        spawn = False
                    if turtle.getX() + turtle._width < 0:
                        lane[1].pop(l)
                else:
                    if turtle.getX() < 0:
                        spawn = False
                    if turtle.getX() > self._width:
                        lane[1].pop(l)
            if on_screen < 8*32 and spawn and random.random() < 0.03:
                turtle = froggerlib.Turtle(self._height-lane[0][1]*32, lane[0][0])
                lane[1].append(turtle)
    
        if self._water.hits(self._frog):
            if self._frog.getDesiredX() == self._frog.getX():
                if self._frog.getDesiredY() == self._frog.getY():
                    self._frog.kill()
        inHome = False
        for home in self._homes:
            if home.hits(self._frog):
                inHome = True
                if home.getWin():
                    self._frog.kill()
                else:
                    self._frog.addScore(150)
                    home.setWin()
                    self._frog.reset()
                    self._frog.setDesiredX(self._frog.getX())
                    self._frog.setDesiredY(self._frog.getY())
        if not inHome and self._frog.getDesiredX() == self._frog.getX() and self._frog.getDesiredY() == self._frog.getY():
            if self._frog.getY() <= 64:
                self._frog.kill()

    def draw(self, surface: pygame.Surface):
        """Draw the game state to the surface."""
        # Draw the background
        surface.fill((0, 0, 0))
        surface.fill((0, 0, 66), (0, 0, 15*32, 8*32))
        surface.blit(assets.letters[1]["T"], (self._width-16*4, self._height-16))
        surface.blit(assets.letters[1]["I"], (self._width-16*3, self._height-16))
        surface.blit(assets.letters[1]["M"], (self._width-16*2, self._height-16))
        surface.blit(assets.letters[1]["E"], (self._width-16, self._height-16))
        surface.blit(assets.letters[1]["L"], (16*0, self._height-32))
        surface.blit(assets.letters[1]["I"], (16*1, self._height-32))
        surface.blit(assets.letters[1]["V"], (16*2, self._height-32))
        surface.blit(assets.letters[1]["E"], (16*3, self._height-32))
        surface.blit(assets.letters[1]["S"], (16*4, self._height-32))
        for i in range(self._frog.getLives()):
            surface.blit(assets.lives, (i*24+16*5+4, self._height-32))
        if self._frog.getLives() < 0:
            offset = 10*16
            surface.blit(assets.letters[2]["G"], (16*1 + offset, 16))
            surface.blit(assets.letters[2]["A"], (16*2 + offset, 16))
            surface.blit(assets.letters[2]["M"], (16*3 + offset, 16))
            surface.blit(assets.letters[2]["E"], (16*4 + offset, 16))
            surface.blit(assets.letters[2]["O"], (16*6 + offset, 16))
            surface.blit(assets.letters[2]["V"], (16*7 + offset, 16))
            surface.blit(assets.letters[2]["E"], (16*8 + offset, 16))
            surface.blit(assets.letters[2]["R"], (16*9 + offset, 16))
        else:
            surface.blit(assets.letters[0]["P"], (16*0 + self._width*.25-16*3, 0))
            surface.blit(assets.letters[0]["O"], (16*1 + self._width*.25-16*3, 0))
            surface.blit(assets.letters[0]["I"], (16*2 + self._width*.25-16*3, 0))
            surface.blit(assets.letters[0]["N"], (16*3 + self._width*.25-16*3, 0))
            surface.blit(assets.letters[0]["T"], (16*4 + self._width*.25-16*3, 0))
            surface.blit(assets.letters[0]["S"], (16*5 + self._width*.25-16*3, 0))

            surface.blit(assets.letters[0]["T"], (16*0 + self._width*.75-16*2.5, 0))
            surface.blit(assets.letters[0]["O"], (16*1 + self._width*.75-16*2.5, 0))
            surface.blit(assets.letters[0]["T"], (16*2 + self._width*.75-16*2.5, 0))
            surface.blit(assets.letters[0]["A"], (16*3 + self._width*.75-16*2.5, 0))
            surface.blit(assets.letters[0]["L"], (16*4 + self._width*.75-16*2.5, 0))
            digits = str(self._frog.getScore())
            for d in range(5, -1, -1):
                digit = "0"
                if d < len(digits):
                    digit = digits[len(digits)-d-1]
                surface.blit(assets.letters[2][digit], (self._width*.25+16*(5-d) - 16*3, 16))
            digits = str(self._frog.getTotalScore())
            for d in range(5, -1, -1):
                digit = "0"
                if d < len(digits):
                    digit = digits[len(digits)-d-1]
                surface.blit(assets.letters[2][digit], (self._width*.75+16*(5-d) - 16*3, 16))

        limit = 30
        if self._frog.getTimer() > limit*30:
            self._frog.kill()
        else:
            width = (limit-self._frog.getTimer()/30)/limit * (self._width-64)
            pygame.draw.rect(surface, (0, 200, 0), (self._width-64-width, self._height-16, width, 16))
        # Draw the safe zones
        for x in range(0, 15):
            surface.blit(assets.safe, (x*32, self._height-32*2))
            surface.blit(assets.safe, (x*32, self._height-32*8))
        # Draw the hedges
        surface.blit(assets.hedge[1], (0, self._height-32*14.5))
        for x in range(0, 7):
            surface.blit(assets.hedge[0],
                         (x*96+16, self._height-32*14.5))
            surface.blit(assets.hedge[1],
                         (x*96+64+16, self._height-32*14.5))
            surface.blit(assets.hedge[1],
                         (x*96+64+32, self._height-32*14.5))
        # Draw the cars
        for car in self._cars:
            car.draw(surface)
        for lane in self._logs:
            for log in lane[1]:
                log.draw(surface)
        for lane in self._turtles:
            for turtle in lane[1]:
                turtle.draw(surface)
        for home in self._homes:
            home.draw(surface)
        #! Draw the frog last
        self._frog.draw(surface)
