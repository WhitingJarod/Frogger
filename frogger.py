import pygame
import froggerlib
import froggerlib.assets as assets

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
    
    def draw(self, surface: pygame.Surface):
        """Draw the game state to the surface."""
        # Draw the background
        surface.fill((0, 0, 0))
        surface.fill((0, 0, 66), (0, 0, 15*32, 8*32))
        # Draw the safe zones
        for x in range(0, 15):
            surface.blit(assets.safe_sprite, (x*32, self._height-32*2))
            surface.blit(assets.safe_sprite, (x*32, self._height-32*8))
        # Draw the hedges
        surface.blit(assets.hedge_sprites[1], (0, self._height-32*14.5))
        for x in range(0, 7):
            surface.blit(assets.hedge_sprites[0], (x*96+16, self._height-32*14.5))
            surface.blit(assets.hedge_sprites[1], (x*96+64+16, self._height-32*14.5))
            surface.blit(assets.hedge_sprites[1], (x*96+64+32, self._height-32*14.5))
        # Draw the frog
        self._frog.draw(surface)