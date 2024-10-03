from pico2d import *
import random

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand_arrow = load_image('hand_arrow.png')

def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False

def draw_hand_arrow():
    hand_arrow.draw(arrow_x, arrow_y)

def character_line(t):
    global x, y, arrow_x, arrow_y

    move_character_x = (1 - t) * x + t * arrow_x
    move_character_y = (1 - t) * y + t * arrow_y
    return move_character_x, move_character_y

def character_move_to_arrow():
    global x, y, arrow_x, arrow_y, frame

    for i in range(0, 100+1):
        t = i / 100
        move_character_x, move_character_y = character_line(t)

        clear_canvas()
        TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
        draw_hand_arrow()
        character.clip_draw(frame * 100, 100 * 1, 100, 100, move_character_x, move_character_y)
        update_canvas()
        handle_events()
        frame = (frame + 1) % 8
        delay(0.05)

running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
arrow_x = random.randint(0, TUK_WIDTH)
arrow_y = random.randint(0, TUK_HEIGHT)
frame = 0
dir = 0

while running:
    character_move_to_arrow()

    x, y = arrow_x, arrow_y
    arrow_x = random.randint(0, TUK_WIDTH)
    arrow_y = random.randint(0, TUK_HEIGHT)

close_canvas()