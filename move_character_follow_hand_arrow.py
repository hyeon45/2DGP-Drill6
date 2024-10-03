from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand_arrow = load_image('hand_arrow.png')

def handle_events():
    pass

running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0

while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    hand_arrow.draw(TUK_WIDTH // 4, TUK_HEIGHT // 4)
    character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    update_canvas()
    frame = (frame + 1) % 8

    handle_events()

close_canvas()
