import pygame

import game
import keyboard
import draw

# pygame setup
pygame.init()

clock = pygame.time.Clock()

running = True
TICK = pygame.USEREVENT + 1

pygame.time.set_timer(TICK, 250)

player_pos = pygame.Vector2(draw.screen.get_width() / 2, draw.screen.get_height() / 2)
rotation = pygame.Vector2(40, 0)

is_game_over = 0
points = 0
food = set()
body = list()
foo = 0

while running:
    for event in pygame.event.get():
        if event.type == TICK:
            food, point = game.colision_check(food, player_pos)
            points += point
            foo, bite = game.colision_check(body, player_pos)
            if game.move(player_pos, rotation, body, is_game_over) == 1 or bite:
                is_game_over = 1
            if point:
                if len(body) > 0:
                    body.extend([game.tail])
                else:
                    frag_pos = player_pos.x - rotation.x, player_pos.y - rotation.y
                    body.insert(0, frag_pos)
            if game.chance(10) and is_game_over == 0:
                food.add(game.food_generator())
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    keyboard.rotation_handling(rotation, keys)

    if keyboard.restart(keys):
        food, player_pos, is_game_over, points \
            = game.restart_handler(food,
                                   pygame.Vector2(draw.screen.get_width() / 2, draw.screen.get_height() / 2),
                                   body)

    draw.bacground()
    draw.food(food)
    draw.body_fragment(player_pos, "blue")
    print(body)
    for fragment in body:
        draw.body_fragment(fragment, "black")
    draw.points(points)

    if is_game_over == 1:
        draw.gameover()

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 12
    clock.tick(12)

pygame.display.quit()
pygame.quit()
