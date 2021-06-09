
import pygame
import pygame.freetype
import random

board = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
]
have_merged = [
    [False,False,False,False],
    [False,False,False,False],
    [False,False,False,False],
    [False,False,False,False]
]

def print_board():
    for i in range(len(board)):
        print(board[i])
    print(' ')

pygame.init()
pygame.font.init()

GAME_FONT = pygame.freetype.SysFont("Arial", 24)
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
yellow = (220,220,0)
blue = (0,0,255)
light_grey = (190,190,190)
dark_grey = (169,169,169)
#the colors of the valued tiles
tile2 = (234,221,212)
tile4 = (232,218,192)
tile8 = (232,169,118)
tile16 = (234,143,90)
tile32 = (235,116,86)
tile64 = (235,83,46)

height = 630
width = 630
win = pygame.display.set_mode((width,height))
win.fill(dark_grey)

def draw_square(y,x,value=0):
    if value == 0:
        color = light_grey
    elif value == 2:
        color = tile2
    elif value == 4:
        color = tile4
    elif value == 8:
        color = tile8
    elif value == 16:
        color = tile16
    elif value == 32:
        color = tile32
    elif value == 64:
        color = tile64
    elif value > 2050:
        color = black
    else:
        color = yellow
    if value == 0:
        text = ' '
    else:
        text = value
    if value < 5:
        text_color = black
    else:
        text_color = white
    pygame.draw.rect(win, color, (x*150+30,y*150+30,125,125))
    font = pygame.font.SysFont('ClearSans-Regular.ttf', 85)
    text_box = font.render(str(text), True, text_color)
    textRect = text_box.get_rect()
    textRect.center = (x*150+92.5, y*150+92.5)
    win.blit(text_box, textRect)

def redraw_board():
    for i in range(4):
        for j in range(4):
            #print(board[i][j])
            draw_square(i,j,board[i][j])

def new_tile():
    empty_spaces = []
    newnumber = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                empty_spaces.append((i,j))
    if len(empty_spaces) == 0:
        return False
    two_or_four = random.randint(1,10)
    if two_or_four == 10:
        newnumber = 4
    else:
        newnumber = 2
    new = random.randint(0,len(empty_spaces)-1)
    board[empty_spaces[new][0]][empty_spaces[new][1]] = newnumber
    return True

def find_empty(y,x,direction):
    empty_spaces = []
    if direction == 'right':
        for i in range(x+1,4):
            if board[y][i] == 0:
                empty_spaces.append(i)
        if len(empty_spaces) != 0:
            return empty_spaces[-1]
        else:
            return
    elif direction == 'left':
        for i in range(x-1,-1,-1):
            if board[y][i] == 0:
                empty_spaces.append(i)
        if len(empty_spaces) != 0:
            return empty_spaces[-1]
        else:
            return 'empty'
    elif direction == 'down':
        for i in range(y+1,4):
            if board[i][x] == 0:
                empty_spaces.append(i)
        if len(empty_spaces) != 0:
            return empty_spaces[-1]
        else:
            return
    elif direction == 'up':
        for i in range(y-1,-1,-1):
            if board[i][x] == 0:
                empty_spaces.append(i)
        if len(empty_spaces) != 0:
            return empty_spaces[-1]
        else:
            return 'empty'


for i in range(4):
    for j in range(4):
        draw_square(i,j)

for i in range(18):
    break
    if new_tile() == False:
        break
print_board()

something_happened = True
run = True
done = False
new_tile()

clock = pygame.time.Clock()

while run:

    clock.tick(60)
    if something_happened == True:
        if new_tile() == False:
            done = True
        print_board()
    something_happened = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN and done == False:
            for i in range(4):
                for j in range(4):
                    have_merged[i][j] = False
            if event.key==pygame.K_UP: #da up key
                for i in range(4):
                    count =  []
                    for j in range(4):
                        count.append(board[j][i])
                    if count.count(0) == 4:
                        continue
                    for j in range(4):
                        if board[j][i] != 0:
                            the_thing = False
                            last_zero = find_empty(j,i,'up')
                            try:
                                if last_zero == 'empty':
                                    if (board[j-1][i] == board[j][i] and have_merged[j-1][i] == False
                                        and j-1 > -1):
                                        board[j-1][i] += board[j][i]
                                        have_merged[j-1][i] = True
                                        board[j][i] = 0
                                        something_happened = True
                                        the_thing = True
                                else:
                                    if (board[last_zero-1][i] == board[j][i] and have_merged[last_zero-1][i] == False
                                        and last_zero-1 > -1):
                                        board[last_zero-1][i] += board[j][i]
                                        have_merged[last_zero-1][i] = True
                                        board[j][i] = 0
                                        something_happened = True
                                        the_thing = True
                            except:
                                pass
                            finally:
                                if last_zero == 'empty' or the_thing == True:
                                    pass
                                else:
                                    board[last_zero][i] = board[j][i]
                                    board[j][i] = 0
                                    something_happened = True

            elif event.key==pygame.K_LEFT: #da left arrow key
                for i in range(4):
                    if board[i].count(0) == 4:
                        continue
                    for j in range(4):
                        if board[i][j] != 0:
                            the_thing = False
                            last_zero = find_empty(i,j,'left')
                            try:
                                if last_zero == 'empty':
                                    if (board[i][j-1] == board[i][j] and have_merged[i][j-1] == False
                                        and j-1 > -1):
                                        board[i][j-1] += board[i][j]
                                        have_merged[i][j-1] = True
                                        board[i][j] = 0
                                        something_happened = True
                                        the_thing = True
                                else:
                                    if (board[i][last_zero-1] == board[i][j] and have_merged[i][last_zero-1] == False
                                        and last_zero-1 > -1):
                                        board[i][last_zero-1] += board[i][j]
                                        have_merged[i][last_zero-1] = True
                                        board[i][j] = 0
                                        something_happened = True
                                        the_thing = True
                            except:
                                pass
                            finally:
                                if last_zero == 'empty' or the_thing == True:
                                    pass
                                else:
                                    board[i][last_zero] = board[i][j]
                                    board[i][j] = 0
                                    something_happened = True

            elif event.key==pygame.K_DOWN: #da down key
                for i in range(4):
                    count =  []
                    for j in range(4):
                        count.append(board[j][i])
                    if count.count(0) == 4:
                        continue
                    for j in range(3,-1,-1):
                        if board[j][i] != 0:
                            the_thing = False
                            last_zero = find_empty(j,i,'down')
                            try:
                                if not last_zero:
                                    if board[j+1][i] == board[j][i] and have_merged[j+1][i] == False:
                                        board[j+1][i] += board[j][i]
                                        have_merged[j+1][i] = True
                                        board[j][i] = 0
                                        something_happened = True
                                        the_thing = True
                                else:
                                    if board[last_zero+1][i] == board[j][i] and have_merged[last_zero+1][i] == False:
                                        board[last_zero+1][i] += board[j][i]
                                        have_merged[last_zero+1][i] = True
                                        board[j][i] = 0
                                        something_happened = True
                                        the_thing = True
                            except:
                                pass
                            finally:
                                if not last_zero:
                                    pass
                                elif the_thing == False:
                                    board[last_zero][i] = board[j][i]
                                    board[j][i] = 0
                                    something_happened = True

            elif event.key==pygame.K_RIGHT: # da right key
                for i in range(4):
                    if board[i].count(0) == 4:
                        continue
                    for j in range(3,-1,-1):
                        if board[i][j] != 0:
                            the_thing = False
                            last_zero = find_empty(i,j,'right')
                            try:
                                if not last_zero:
                                    if board[i][j+1] == board[i][j] and have_merged[i][j+1] == False:
                                        board[i][j+1] += board[i][j]
                                        have_merged[i][j+1] = True
                                        board[i][j] = 0
                                        something_happened = True
                                        the_thing = True
                                else:
                                    if board[i][last_zero+1] == board[i][j] and have_merged[i][last_zero+1] == False:
                                        board[i][last_zero+1] += board[i][j]
                                        have_merged[i][last_zero+1] = True
                                        board[i][j] = 0
                                        something_happened = True
                                        the_thing = True
                            except:
                                pass
                            finally:
                                if not last_zero:
                                    pass
                                elif len(str(last_zero)) != 0 and the_thing == False:
                                    board[i][last_zero] = board[i][j]
                                    board[i][j] = 0
                                    something_happened = True

    redraw_board()

    pygame.display.flip()

pygame.quit()
