import pygame
import froggerlib
import assets
import random


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
        self._logs = [[(4, 10), []],[(-6, 11), []],[(-5, 13), []]]
        self._turtles = [[(-4, 9), []], [(4, 12), []]]
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
        for home in self._homes:
            home.draw(surface)
        #! Draw the frog last
        self._frog.draw(surface)
