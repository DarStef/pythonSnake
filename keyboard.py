import pygame


def rotation_handling(rotation, keys):
    if (keys[pygame.K_w] or keys[pygame.K_UP]) and rotation.y != -40 and rotation.x != 0:
        rotation.y = -40
        rotation.x = 0
    if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and rotation.y != 40 and rotation.x != 0:
        rotation.y = 40
        rotation.x = 0
    if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and rotation.x != -40 and rotation.y != 0:
        rotation.x = -40
        rotation.y = 0
    if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and rotation.x != 40 and rotation.y != 0:
        rotation.x = 40
        rotation.y = 0


def restart(keys):
    if keys[pygame.K_r]:
        return 1
