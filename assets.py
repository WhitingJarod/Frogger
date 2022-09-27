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
    global win
    global turts
    global letters
    global lives
    lives = sprites.image_at((75, 429, 16 ,16))
    safe = sprites.image_at((270, 392, 32, 32))
    car = sprites.image_at((4, 238, 29, 19))
    racer_left = sprites.image_at((38, 234, 31, 27))
    racer_right = sprites.image_at((74, 234, 31, 27))
    truck = sprites.image_at((152, 238, 53, 19))
    harvester = sprites.image_at((112, 236, 27, 23))
    win = sprites.image_at((90, 392, 32, 32))
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
    turts = [
        sprites.image_at((38, 308, 30, 26)),
        sprites.image_at((4, 308, 30, 26)),
        sprites.image_at((74, 308, 30, 26)),
        sprites.image_at((115, 308, 30, 26)),
        sprites.image_at((147, 308, 30, 26)),
    ]
    letters = [
        {
            "0": sprites.image_at((3, 499, 16, 16)),
            "1": sprites.image_at((22, 499, 16, 16)),
            "2": sprites.image_at((40, 499, 16, 16)),
            "3": sprites.image_at((58, 499, 16, 16)),
            "4": sprites.image_at((76, 499, 16, 16)),
            "5": sprites.image_at((94, 499, 16, 16)),
            "6": sprites.image_at((112, 499, 16, 16)),
            "7": sprites.image_at((130, 499, 16, 16)),
            "8": sprites.image_at((148, 499, 16, 16)),
            "9": sprites.image_at((166, 499, 16, 16)),
            "A": sprites.image_at((184, 499, 16, 16)),
            "B": sprites.image_at((202, 499, 16, 16)),
            "C": sprites.image_at((220, 499, 16, 16)),
            "D": sprites.image_at((238, 499, 16, 16)),
            "E": sprites.image_at((256, 499, 16, 16)),
            "F": sprites.image_at((274, 499, 16, 16)),
            "G": sprites.image_at((292, 499, 16, 16)),
            "H": sprites.image_at((3, 517, 16, 16)),
            "I": sprites.image_at((22, 517, 16, 16)),
            "J": sprites.image_at((40, 517, 16, 16)),
            "K": sprites.image_at((58, 517, 16, 16)),
            "L": sprites.image_at((76, 517, 16, 16)),
            "M": sprites.image_at((94, 517, 16, 16)),
            "N": sprites.image_at((112, 517, 16, 16)),
            "O": sprites.image_at((130, 517, 16, 16)),
            "P": sprites.image_at((148, 517, 16, 16)),
            "Q": sprites.image_at((166, 517, 16, 16)),
            "R": sprites.image_at((184, 517, 16, 16)),
            "S": sprites.image_at((202, 517, 16, 16)),
            "T": sprites.image_at((220, 517, 16, 16)),
            "U": sprites.image_at((238, 517, 16, 16)),
            "V": sprites.image_at((256, 517, 16, 16)),
            "W": sprites.image_at((274, 517, 16, 16)),
            "X": sprites.image_at((292, 517, 16, 16)),
            "Y": sprites.image_at((3, 535, 16, 16)),
            "Z": sprites.image_at((22, 535, 16, 16)),
            "-": sprites.image_at((40, 535, 16, 16)),
            "(c)": sprites.image_at((58, 535, 16, 16)),
            "[]": sprites.image_at((76, 535, 16, 16)),
        },
        {
            "0": sprites.image_at((3, 555, 16, 16)),
            "1": sprites.image_at((22, 555, 16, 16)),
            "2": sprites.image_at((40, 555, 16, 16)),
            "3": sprites.image_at((58, 555, 16, 16)),
            "4": sprites.image_at((76, 555, 16, 16)),
            "5": sprites.image_at((94, 555, 16, 16)),
            "6": sprites.image_at((112, 555, 16, 16)),
            "7": sprites.image_at((130, 555, 16, 16)),
            "8": sprites.image_at((148, 555, 16, 16)),
            "9": sprites.image_at((166, 555, 16, 16)),
            "A": sprites.image_at((184, 555, 16, 16)),
            "B": sprites.image_at((202, 555, 16, 16)),
            "C": sprites.image_at((220, 555, 16, 16)),
            "D": sprites.image_at((238, 555, 16, 16)),
            "E": sprites.image_at((256, 555, 16, 16)),
            "F": sprites.image_at((274, 555, 16, 16)),
            "G": sprites.image_at((292, 555, 16, 16)),
            "H": sprites.image_at((3, 573, 16, 16)),
            "I": sprites.image_at((22, 573, 16, 16)),
            "J": sprites.image_at((40, 573, 16, 16)),
            "K": sprites.image_at((58, 573, 16, 16)),
            "L": sprites.image_at((76, 573, 16, 16)),
            "M": sprites.image_at((94, 573, 16, 16)),
            "N": sprites.image_at((112, 573, 16, 16)),
            "O": sprites.image_at((130, 573, 16, 16)),
            "P": sprites.image_at((148, 573, 16, 16)),
            "Q": sprites.image_at((166, 573, 16, 16)),
            "R": sprites.image_at((184, 573, 16, 16)),
            "S": sprites.image_at((202, 573, 16, 16)),
            "T": sprites.image_at((220, 573, 16, 16)),
            "U": sprites.image_at((238, 573, 16, 16)),
            "V": sprites.image_at((256, 573, 16, 16)),
            "W": sprites.image_at((274, 573, 16, 16)),
            "X": sprites.image_at((292, 573, 16, 16)),
            "Y": sprites.image_at((3, 591, 16, 16)),
            "Z": sprites.image_at((22, 591, 16, 16)),
            "-": sprites.image_at((40, 591, 16, 16)),
            "(c)": sprites.image_at((58, 591, 16, 16)),
            "[]": sprites.image_at((76, 591, 16, 16)),
        },
        {
            "0": sprites.image_at((3, 611, 16, 16)),
            "1": sprites.image_at((22, 611, 16, 16)),
            "2": sprites.image_at((40, 611, 16, 16)),
            "3": sprites.image_at((58, 611, 16, 16)),
            "4": sprites.image_at((76, 611, 16, 16)),
            "5": sprites.image_at((94, 611, 16, 16)),
            "6": sprites.image_at((112, 611, 16, 16)),
            "7": sprites.image_at((130, 611, 16, 16)),
            "8": sprites.image_at((148, 611, 16, 16)),
            "9": sprites.image_at((166, 611, 16, 16)),
            "A": sprites.image_at((184, 611, 16, 16)),
            "B": sprites.image_at((202, 611, 16, 16)),
            "C": sprites.image_at((220, 611, 16, 16)),
            "D": sprites.image_at((238, 611, 16, 16)),
            "E": sprites.image_at((256, 611, 16, 16)),
            "F": sprites.image_at((274, 611, 16, 16)),
            "G": sprites.image_at((292, 611, 16, 16)),
            "H": sprites.image_at((3, 629, 16, 16)),
            "I": sprites.image_at((22, 629, 16, 16)),
            "J": sprites.image_at((40, 629, 16, 16)),
            "K": sprites.image_at((58, 629, 16, 16)),
            "L": sprites.image_at((76, 629, 16, 16)),
            "M": sprites.image_at((94, 629, 16, 16)),
            "N": sprites.image_at((112, 629, 16, 16)),
            "O": sprites.image_at((130, 629, 16, 16)),
            "P": sprites.image_at((148, 629, 16, 16)),
            "Q": sprites.image_at((166, 629, 16, 16)),
            "R": sprites.image_at((184, 629, 16, 16)),
            "S": sprites.image_at((202, 629, 16, 16)),
            "T": sprites.image_at((220, 629, 16, 16)),
            "U": sprites.image_at((238, 629, 16, 16)),
            "V": sprites.image_at((256, 629, 16, 16)),
            "W": sprites.image_at((274, 629, 16, 16)),
            "X": sprites.image_at((292, 629, 16, 16)),
            "Y": sprites.image_at((3, 647, 16, 16)),
            "Z": sprites.image_at((22, 647, 16, 16)),
            "-": sprites.image_at((40, 647, 16, 16)),
            "(c)": sprites.image_at((58, 647, 16, 16)),
            "[]": sprites.image_at((76, 647, 16, 16)),
        }
    ]
