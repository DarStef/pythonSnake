import random

import pygame

tail = pygame.Vector2(0, 0)


def move(player_pos, rotation, body, game_mode):
    if 640 >= player_pos.x >= 40 and 640 >= player_pos.y >= 40 and game_mode == 0:
        snake(player_pos, body)
        player_pos += rotation
    else:
        return 1


def food_generator():
    x = random.randint(1, 16)
    y = random.randint(1, 16)
    point: tuple[int, int] = x * 40, y * 40
    return point


def chance(percent):
    res = random.randint(1, 100)
    if res > percent:
        return 0
    else:
        return 1


def colision_check(obj_set, head_pos):
    hit = 0
    for point in obj_set:
        if point[0] == head_pos.x and point[1] == head_pos.y:
            obj_set.remove(point)
            hit = 1
            break
    return obj_set, hit


def restart_handler(food, start_pos, body):
    food.clear()
    body.clear()
    player_pos = start_pos
    is_game_over = 0
    points = 0
    return food, player_pos, is_game_over, points


def snake(head, body):
    if len(body) > 0:
        b_head = head.x, head.y
        body.insert(0, b_head)
        tail = body.pop()


