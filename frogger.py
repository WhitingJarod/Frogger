import pygame
import froggerlib
import assets


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
        self._stages = []
        self._cars = []
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
        self._logs = []
        self._turtles = []
        self._movables = []
        self._frog_direction = 0
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
        if self._frog.getX() < 0:
            self._frog.setX(0)
            self._frog.setDesiredX(0)
            self._frog.kill()
        elif self._frog.getX() > self._width-32:
            self._frog.setX(self._width-32)
            self._frog.setDesiredX(self._width-32)
            self._frog.kill()
        if self._frog.getY() < 64:
            self._frog.setY(64)
            self._frog.setDesiredY(64)
            self._frog.kill()
        elif self._frog.getY() > self._height-64:
            self._frog.setY(self._height-64)
            self._frog.setDesiredY(self._height-64)
            self._frog.kill()
        for car in self._cars:
            car.move()
            if car.hits(self._frog):
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
        # Draw the frog
        self._frog.draw(surface)
        # Draw the cars
        for car in self._cars:
            car.draw(surface)
