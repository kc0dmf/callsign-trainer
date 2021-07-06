# From https://stackoverflow.com/questions/45427411/simple-way-to-display-text-on-screen-in-python
# This shows a blank screen with text in the center.
# Works great on the Mac.

import sys
from random import choice, randrange
from string import ascii_letters

import pygame as pg


def random_letters(n):
    """Pick n random letters."""
    # return ''.join(choice(ascii_letters) for _ in range(n))
    return 'kc0dmf'


def main():
    info = pg.display.Info()
    screen = pg.display.set_mode((info.current_w, info.current_h), pg.FULLSCREEN)
    screen_rect = screen.get_rect()
    font = pg.font.Font(None, 45)
    clock = pg.time.Clock()
    color = (randrange(256), randrange(256), randrange(256))
    txt = font.render(random_letters(randrange(5, 21)), True, color)
    timer = 10
    done = False

    clr = 0
    clrstep = 20

    while not done:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE or event.key == pg.K_q:
                    done = True

        timer -= 1
        # Update the text surface and color every 10 frames.
        if timer <= 0:
            timer = 10
            clr += clrstep
            if clr > (255-clrstep) or clr <= 0:
                clrstep = clrstep * (-1)
            # color = (randrange(256), randrange(256), randrange(256))
            color = (clr, clr, clr)
            txt = font.render(random_letters(randrange(5, 21)), True, color)

        screen.fill((30, 30, 30))
        screen.blit(txt, txt.get_rect(center=screen_rect.center))

        pg.display.flip()
        clock.tick(100)


if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()
    sys.exit()
