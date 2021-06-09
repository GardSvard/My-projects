
import pygame
import math

pygame.init()

font = pygame.font.SysFont('ClearSans-Bold.ttf', 15)
black = (0,0,0)
light_black = (50,50,50)
white = (230,230,230)
dark_white = (180,180,180)
dark_grey = (169,169,169)
board_black = (179,134,108)
board_white = (243,222,198) 
board_edge = (124,87,65)
red = (255,100,100)
dark_red = (255,50,50)
light_blue = (100,100,255)
blue = (50,50,255)
green = (50,255,50)
light_green = (100,255,100)
yellow = (255,255,50)
light_yellow = (255,255,100)
brown = (139,69,19)
light_brown = (210,105,30)

colors = {
    '0' : board_white,
    '1' : red,
    '2' : light_black, #the darker shade first
    '3' : white,
    '4' : dark_red,
    '5' : green,
    '6' : blue,
    '7' : yellow,
    '8' : brown,
}

color = 0
color_num = 0

height = 520
width = 520
width_margin = 30
showLines = False
win = pygame.display.set_mode((width+width_margin,height))
win.fill(white)

pygame.display.set_caption("Map maker")

board_size = 20

board = []
if not board:
    for i in range(board_size):
        board.append([0]*board_size)

def print_board():
    for i in range(board_size):
        print('\t'+str(board[i])+',')

clock = pygame.time.Clock()

blockSize = height/board_size #Set the size of the grid block

def drawGrid():
    linewidth = math.ceil(60/board_size)
    for i in range(1,board_size):
        pygame.draw.line(win,black,(0,i*blockSize),(width,i*blockSize),linewidth)
    for i in range(1,board_size):
        pygame.draw.line(win,black,(i*blockSize,0),(i*blockSize,height),linewidth)
    pygame.draw.line(win,black,(width,0),(width,height),linewidth)

def draw_board():
    y = board_size
    x = board_size
    win.fill(board_white)
    for i in range(y):
        for j in range(x):
            l = board[j][i]
            current = colors[str(l)]
            pygame.draw.rect(win, current, (blockSize*i,blockSize*j,blockSize+1,blockSize+1))
    for i in range(len(colors)):
        pygame.draw.rect(win, colors[str(i)], (width,i*width_margin,width_margin,width_margin))
    pygame.draw.rect(win, color, (width,height-width_margin,width_margin,width_margin))
    if showLines == True:
        drawGrid()
    else:
        pygame.draw.line(win,black,(width,0),(width,height),3)


def where(xy):
    int_xy = []
    if xy[0] <= width:
        int_xy.append((xy[0]) // blockSize)
        int_xy.append((xy[1]) // blockSize)
    else:
        int_xy.append(xy[1]//width_margin)
    return int_xy


run = True
done = False
drawing = False

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print_board()
            run = False
        if event.type == pygame.KEYDOWN and done == False:
        
            if event.key==pygame.K_w: #da up key
                pass        
        
        if event.type == pygame.MOUSEBUTTONDOWN and done == False:
            temp = pygame.mouse.get_pos()
            click = where(temp)
            if len(click) == 1:
                click = click[0]
                if click < len(colors):
                    color = colors[str(click)]
                    color_num = click
                else:
                    color = colors[str(0)]
                    color_num = 0
            else:
                drawing = True

        if event.type == pygame.MOUSEBUTTONUP and done == False:
            drawing = False

    if drawing == True and done == False:
        temp = pygame.mouse.get_pos()
        click = where(temp)
        if len(click) == 1:
            pass
        else:
            board[int(click[1])][int(click[0])] = color_num

    draw_board()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
