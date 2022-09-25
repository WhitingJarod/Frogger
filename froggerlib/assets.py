from spritesheet import spritesheet


_initialized = False
def init():
    if _initialized:
        return
    sprites = spritesheet("froggerlib/assets.png")
    global frog_sprites
    global death_sprites
    global car_sprites
    global log_sprites
    global safe_sprite
    global hedge_sprites
    safe_sprite = sprites.image_at((270, 392, 32, 32))
    frog_sprites = [
        sprites.image_at((2, 2, 32, 32)),
        sprites.image_at((38, 2, 32, 32)),
        sprites.image_at((74, 2, 32, 32)),
        sprites.image_at((110, 2, 32, 32)),
        sprites.image_at((146, 2, 32, 32)),
        sprites.image_at((182, 2, 32, 32)),
        sprites.image_at((218, 2, 32, 32)),
        sprites.image_at((254, 2, 32, 32))
    ]
    death_sprites = [
        sprites.image_at((2, 160, 32, 32)),
        sprites.image_at((38, 160, 32, 32)),
        sprites.image_at((74, 160, 32, 32)),
        sprites.image_at((110, 160, 32, 32)),
        sprites.image_at((146, 160, 32, 32)),
        sprites.image_at((182, 160, 32, 32)),
        sprites.image_at((218, 160, 32, 32))
    ]
    car_sprites = [
        sprites.image_at((2, 232, 32, 32)),
        sprites.image_at((38, 232, 32, 32)),
        sprites.image_at((74, 232, 32, 32)),
        sprites.image_at((110, 232, 32, 32)),
        sprites.image_at((146, 232, 64, 32)),
    ]
    log_sprites = [
        sprites.image_at((2, 268, 32, 32)),
        sprites.image_at((38, 268, 32, 32)),
        sprites.image_at((74, 268, 32, 32))
    ]
    hedge_sprites = [
        sprites.image_at((2, 376, 64, 48)),
        sprites.image_at((70, 376, 16, 48)),
    ]