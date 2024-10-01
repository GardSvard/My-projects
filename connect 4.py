
board = [[0]*7,[0]*7,[0]*7,[0]*7,[0]*7,[0]*7,]

import pygame
import time

pygame.init()

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
yellow = (255,255,0)
blue = (0,0,255)
height = 600
width = 700
win = pygame.display.set_mode((width,height))
win.fill(blue)
turn = 'Yellow'
win_yellow = False
win_red = False

def place(col):
    for i in range(len(board)):
        global turn, win_yellow, win_red
        if board[i][col] != 0:
            if turn == 'Yellow':
                board[i-1][col] = 1
                draw_circle(col*100+50,(i-1)*100+50,yellow)
                win_yellow = win_cond(col,i-1,turn)
                turn = 'Red'
                break
            elif turn == 'Red':
                board[i-1][col] = 2
                draw_circle(col*100+50,(i-1)*100+50,red)
                win_red = win_cond(col,i-1,turn)
                turn = 'Yellow'
                break
        elif i == 5:
            if turn == 'Yellow':
                board[i][col] = 1
                draw_circle(col*100+50,i*100+50,yellow)
                win_yellow = win_cond(col,i,turn)
                turn = 'Red'
                break
            elif turn == 'Red':
                board[i][col] = 2
                draw_circle(col*100+50,i*100+50,red)
                win_red = win_cond(col,i,turn)
                turn = 'Yellow'
                break
    return (win_red,win_yellow)

def verify(col):
    global turn
    monk = (False,False)
    if board[0][col] == 0:
        monk = place(col)
    return monk

def win_cond(x,y,color):
    #check the horizontal
    for i in range(4):
        if color == 'Yellow':
            if board[y][i:i+4].count(1) == 4:
                return True
        if color == 'Red':
            if board[y][i:i+4].count(2) == 4:
                return True

    #check the vertical
    vertical_list = []
    for i in range(len(board)):
        vertical_list.append(board[i][x])

    for i in range(3):
        if color == 'Yellow':
            if vertical_list[i:i+4].count(1) == 4:
                return True
        if color == 'Red':
            if vertical_list[i:i+4].count(2) == 4:
                return True

    #check upper left to lower right diagonal
    for i in range(10):
        if x-i == 0 or y-i == 0:
            diagonal_start = (y-i,x-i)
            break
    diagonal_list = []
    if diagonal_start[0]<diagonal_start[1]:
        use = diagonal_start[1]
    else:
        use = diagonal_start[0]

    for i in range(7-use):
        try:
            diagonal_list.append(board[diagonal_start[0]+i][diagonal_start[1]+i])
        except:
            pass

    if len(diagonal_list)>3:
        for i in range(len(diagonal_list)-3):
            if turn == 'Yellow':
                if diagonal_list[i:i+4].count(1) == 4:
                    return True

            elif turn == 'Red':
                if diagonal_list[i:i+4].count(2) == 4:
                    return True

    #check lower left to upper right
    for i in range(10):
        if x-i == 0 or y+i == 5:
            diagonal_start = (y-i,x+i)
            break

    diagonal_list = []
    if diagonal_start[0]+6<diagonal_start[1]:
        use = diagonal_start[1]
    else:
        use = diagonal_start[0]

    for i in range(7):
        try:
            diagonal_list.append(board[diagonal_start[0]+i][diagonal_start[1]-i])
        except:
            pass

    if len(diagonal_list)>3:
        for i in range(len(diagonal_list)-3):
            if turn == 'Yellow':
                if diagonal_list[i:i+4].count(1) == 4:
                    return True

            elif turn == 'Red':
                if diagonal_list[i:i+4].count(2) == 4:
                    return True
    return

def draw_circle(x, y, color):
    pygame.draw.circle(win, color, (x, y), 40)

def where(mouse_x):
    return mouse_x // 100

initial_y = -50
for i in range(len(board)):
    initial_x = 50
    initial_y += 100
    for j in range(len(board[0])):
        draw_circle(initial_x,initial_y,white)
        initial_x += 100

pygame.display.flip()
done = False
run = True

while run:

    pygame.time.delay(100)
    for event in pygame.event.get():
        mouse_pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and done == False:
            win_red,win_yellow = verify(where(mouse_pos[0]))
            if win_red == True:
                done = True
                turn = 'Red'
                print('done, red won')
            if win_yellow == True:
                done = True
                turn = 'Yellow'
                print('done, yellow won')
            if done == False:
                pygame.display.set_caption("Connect 4 (%s's Turn)" % turn)
            else:
                pygame.display.set_caption("%s has won the game!" % turn)
    pygame.display.flip()

pygame.quit()
