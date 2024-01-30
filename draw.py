import pygame

pygame.font.init()
screen = pygame.display.set_mode((720, 720))
my_font = pygame.font.SysFont('Comic Sans MS', 30)


def body_fragment(fragment_pos, color):
    pygame.draw.rect(screen, "yellow", [fragment_pos[0], fragment_pos[1], 40, 40])
    pygame.draw.rect(screen, color, [fragment_pos[0] + 5, fragment_pos[1] + 5, 30, 30])


def bacground():
    screen.fill("grey")
    pygame.draw.rect(screen, "brown", [40, 40, 640, 640])


def gameover():
    text_surface = my_font.render(' Game Over ', False, (255, 255, 255), (0, 0, 0))
    screen.blit(text_surface,
                ((screen.get_width() - text_surface.get_size()[0]) / 2,
                 (screen.get_height() - text_surface.get_size()[1]) / 2))


def food(food_set):
    for point in food_set:
        pygame.draw.rect(screen, "green", [point[0], point[1], 40, 40])


def points(number):
    text_surface = my_font.render(' Points ' + str(number), False, (0, 0, 0), "darkgrey")
    screen.blit(text_surface, (5, 5))
