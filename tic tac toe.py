import pygame
import time

pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
height = 600
width = 600
win = pygame.display.set_mode((width, height))
win.fill(white)


def draw_circle(x, y):
    pygame.draw.circle(win, black, (x, y), 75, 3)


def draw_cross(x, y):
    pygame.draw.line(win, (black), (x - 75, y - 75), (x + 75, y + 75), 4)
    pygame.draw.line(win, (black), (x - 75, y + 75), (x + 75, y - 75), 4)


d1 = 0
d2 = 0
d3 = 0
h1 = 0
h2 = 0
h3 = 0
s1 = 0
s2 = 0
turns = 0
turn = "Cross"
run = True
taken = [False] * 9
center_coordinates = [
    [100, 100],
    [100, 300],
    [100, 500],
    [300, 100],
    [300, 300],
    [300, 500],
    [500, 100],
    [500, 300],
    [500, 500],
]
boundaries = [
    [200, 0, 200, 0],
    [200, 0, 400, 200],
    [200, 0, 600, 400],
    [400, 200, 200, 0],
    [400, 200, 400, 200],
    [400, 200, 600, 400],
    [600, 400, 200, 0],
    [600, 400, 400, 200],
    [600, 400, 600, 400],
]


class square:
    def take(self, number):
        global turns
        global turn
        turns += 1
        if turn == "Cross":
            taken[number - 1] = True
            draw_cross(
                center_coordinates[number - 1][0], center_coordinates[number - 1][1]
            )
            return
        if turn == "Circle":
            taken[number - 1] = True
            draw_circle(
                center_coordinates[number - 1][0], center_coordinates[number - 1][1]
            )
            return

    def check(self, number):
        if (
            mouse_pos[0] < boundaries[number - 1][0]
            and mouse_pos[0] > boundaries[number - 1][1]
            and mouse_pos[1] < boundaries[number - 1][2]
            and mouse_pos[1] > boundaries[number - 1][3]
            and not taken[number - 1]
        ):
            s.take(number)
            return True
        return


s = square()
cross_win = False
circle_win = False
draw = False

while run:
    pygame.time.delay(100)

    if cross_win == False and circle_win == False and draw == False:
        pygame.display.set_caption("Tic Tac Toe (%s's Turn)" % turn)
    if (
        d1 == 3
        or d2 == 3
        or d3 == 3
        or h1 == 3
        or h2 == 3
        or h3 == 3
        or s1 == 3
        or s2 == 3
        and circle_win == False
        and cross_win == False
    ):
        pygame.display.set_caption("CIRCLE WON, CONGRATULATIONS!")
        circle_win = True
    if (
        d1 == -3
        or d2 == -3
        or d3 == -3
        or h1 == -3
        or h2 == -3
        or h3 == -3
        or s1 == -3
        or s2 == -3
        and circle_win == False
        and cross_win == False
    ):
        pygame.display.set_caption("CROSS WON, CONGRATULATIONS!")
        circle_win = True
    if turns == 9 and circle_win == False and cross_win == False:
        pygame.display.set_caption("IT'S A DRAW!")
        draw = True
    for event in pygame.event.get():
        mouse_pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            run = False
        if (
            event.type == pygame.MOUSEBUTTONDOWN
            and circle_win == False
            and cross_win == False
        ):
            if s.check(1) == True:
                if turn == "Cross":
                    turn = "Circle"
                    d1 -= 1
                    h1 -= 1
                    s1 -= 1
                    break
                if turn == "Circle":
                    turn = "Cross"
                    d1 += 1
                    h1 += 1
                    s1 += 1
                    break
            if s.check(2) == True:
                if turn == "Cross":
                    turn = "Circle"
                    d1 -= 1
                    h2 -= 1
                    break
                if turn == "Circle":
                    turn = "Cross"
                    d1 += 1
                    h2 += 1
                    break
            if s.check(3) == True:
                if turn == "Cross":
                    turn = "Circle"
                    d1 -= 1
                    h3 -= 1
                    s2 -= 1
                    break
                if turn == "Circle":
                    turn = "Cross"
                    d1 += 1
                    h3 += 1
                    s2 += 1
                    break
            if s.check(4) == True:
                if turn == "Cross":
                    turn = "Circle"
                    d2 -= 1
                    h1 -= 1
                    break
                if turn == "Circle":
                    turn = "Cross"
                    d2 += 1
                    h1 += 1
                    break
            if s.check(5) == True:
                if turn == "Cross":
                    turn = "Circle"
                    d2 -= 1
                    h2 -= 1
                    s1 -= 1
                    s2 -= 1
                    break
                if turn == "Circle":
                    turn = "Cross"
                    d2 += 1
                    h2 += 1
                    s1 += 1
                    s2 += 1
                    break
            if s.check(6) == True:
                if turn == "Cross":
                    turn = "Circle"
                    d2 -= 1
                    h3 -= 1
                    break
                if turn == "Circle":
                    turn = "Cross"
                    d2 += 1
                    h3 += 1
            if s.check(7) == True:
                if turn == "Cross":
                    turn = "Circle"
                    d3 -= 1
                    h1 -= 1
                    s2 -= 1
                    break
                if turn == "Circle":
                    turn = "Cross"
                    d3 += 1
                    h1 += 1
                    s2 += 1
                    break
            if s.check(8) == True:
                if turn == "Cross":
                    turn = "Circle"
                    d3 -= 1
                    h2 -= 1
                    break
                if turn == "Circle":
                    turn = "Cross"
                    d3 += 1
                    h2 += 1
                    break
            if s.check(9) == True:
                if turn == "Cross":
                    turn = "Circle"
                    d3 -= 1
                    h3 -= 1
                    s1 -= 1
                    break
                if turn == "Circle":
                    turn = "Cross"
                    d3 += 1
                    h3 += 1
                    s1 += 1
                    break
    # draw the lines of the board
    pygame.draw.line(win, (black), (0, height / 3), (width, height / 3), 4)
    pygame.draw.line(
        win, (black), (0, height - height / 3), (width, height - height / 3), 4
    )
    pygame.draw.line(win, (black), (width / 3, 0), (width / 3, height), 4)
    pygame.draw.line(
        win, (black), (width - width / 3, 0), (width - width / 3, height), 4
    )

    pygame.display.flip()
pygame.quit()
