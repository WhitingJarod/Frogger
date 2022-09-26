from spritesheet import spritesheet


_initialized = False


def init():
    if _initialized:
        return
    sprites = spritesheet("assets.png")
    global frog
    global death
    global car
    global log
    global safe
    global hedge
    global racer_left
    global racer_right
    global truck
    global harvester
    safe = sprites.image_at((270, 392, 32, 32))
    car = sprites.image_at((4, 238, 29, 19))
    racer_left = sprites.image_at((38, 234, 31, 27))
    racer_right = sprites.image_at((74, 234, 31, 27))
    truck = sprites.image_at((152, 238, 53, 19))
    harvester = sprites.image_at((112, 236, 27, 23))
    frog = [
        sprites.image_at((2, 2, 32, 32)),
        sprites.image_at((38, 2, 32, 32)),
        sprites.image_at((74, 2, 32, 32)),
        sprites.image_at((110, 2, 32, 32)),
        sprites.image_at((146, 2, 32, 32)),
        sprites.image_at((182, 2, 32, 32)),
        sprites.image_at((218, 2, 32, 32)),
        sprites.image_at((254, 2, 32, 32))
    ]
    death = [
        sprites.image_at((2, 160, 32, 32)),
        sprites.image_at((38, 160, 32, 32)),
        sprites.image_at((74, 160, 32, 32)),
        sprites.image_at((110, 160, 32, 32)),
        sprites.image_at((146, 160, 32, 32)),
        sprites.image_at((182, 160, 32, 32)),
        sprites.image_at((218, 160, 32, 32))
    ]
    log = [
        sprites.image_at((2, 268, 32, 32)),
        sprites.image_at((38, 268, 32, 32)),
        sprites.image_at((74, 268, 32, 32))
    ]
    hedge = [
        sprites.image_at((2, 376, 64, 48)),
        sprites.image_at((70, 376, 16, 48)),
    ]
