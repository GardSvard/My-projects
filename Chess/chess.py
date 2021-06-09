
import pygame
import pygame .freetype
import random
import os
from itertools import product, permutations

combination = []
for roll in product([-1,0,1], repeat = 2):
    if roll != (0,0):
        combination.append(roll)


board = [
    [-2,-3,-4,-5,-6,-4,-3,-2],
    [-1,-1,-1,-1,-1,-1,-1,-1],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [1,1,1,1,1,1,1,1],
    [2,3,4,5,6,4,3,2]
]

white_king_moved = False
black_king_moved = False

def print_board():
    for i in range(len(board)):
        print(board[i])
    print(' ')

pygame.init()

font = pygame.font.SysFont('ClearSans-Bold.ttf', 15)
black = (0,0,0)
white = (255,255,255)
dark_grey = (169,169,169)
board_black = (179,134,108)
board_white = (243,222,198) 
board_edge = (124,87,65)
red = (255,130,130)

height = 520
width = 520
win = pygame.display.set_mode((width,height))
win.fill(white)

turn = 'white'

pygame.display.set_caption("Chess (%s's turn)" % turn)

class piece:
    def init(self,y,x,value):
        possible_moves = []
        self.y = y
        self.x = x
        self.value = value
        if self.value < 0:
            self.color = 'black'
        else:
            self.color = 'white'
        absolute = abs(self.value)
        if absolute == 2:
            for i in self.rook_moves():
                possible_moves.append([i[0],i[1]])
        elif absolute == 4:
            for i in self.bishop_moves():
                possible_moves.append([i[0],i[1]])
        elif absolute == 5:
            for i in self.rook_moves():
                possible_moves.append([i[0],i[1]])
            for i in self.bishop_moves():
                possible_moves.append([i[0],i[1]])
        elif absolute == 1:
            for i in self.pawn_moves():
                possible_moves.append([i[0],i[1]])
        elif absolute == 6:
            for i in self.king_moves():
                possible_moves.append([i[0],i[1]])
        elif absolute == 3:
            for i in self.knight_moves():
                possible_moves.append([i[0],i[1]])
        return possible_moves

    def knight_moves(self):
        knight_list = []
        for i in (2,-2):
            for j in (1,-1):
                if self.y + i > 7 or self.y + i < 0 or self.x + j > 7 or self.x + j < 0:
                    continue
                elif board[self.y+i][self.x+j] == 0:
                    knight_list.append((self.y+i,self.x+j))
                elif (self.value > 0 and board[self.y+i][self.x+j] < 0
                    or self.value < 0 and board[self.y+i][self.x+j] > 0):
                    knight_list.append((self.y+i,self.x+j))
        for i in (1,-1):
            for j in (2,-2):
                if self.y + i > 7 or self.y + i < 0 or self.x + j > 7 or self.x + j < 0:
                    continue
                elif board[self.y+i][self.x+j] == 0:
                    knight_list.append((self.y+i,self.x+j))
                elif (self.value > 0 and board[self.y+i][self.x+j] < 0
                    or self.value < 0 and board[self.y+i][self.x+j] > 0):
                    knight_list.append((self.y+i,self.x+j))
        return knight_list

    def king_moves(self):
        king_list = []
        castle = []
        if white_king_moved == False:
            for k in range(1,4):
                castle.append(board[self.y][self.x+k])
            if castle.count(0) == 2 and castle[-1] == 2:
                king_list.append((self.y,self.x+2))
            castle = []
            for k in range(1,5):
                castle.append(board[self.y][self.x-k])
            if castle.count(0) == 3 and castle[-1] == 2:
                king_list.append((self.y,self.x-2))
        if black_king_moved == False:
            for k in range(1,4):
                castle.append(board[self.y][self.x+k])
            if castle.count(0) == 2 and castle[-1] == -2:
                king_list.append((self.y,self.x+2))
            castle = []
            for k in range(1,5):
                castle.append(board[self.y][self.x-k])
            if castle.count(0) == 3 and castle[-1] == -2:
                king_list.append((self.y,self.x-2))
        for i in combination:
            if (self.y+i[0] > 7 or self.y+i[0] < 0 or 
                self.x+i[1] > 7 or self.x+i[1] < 0):
                continue
            elif board[self.y+i[0]][self.x+i[1]] == 0:
                king_list.append((self.y+i[0],self.x+i[1]))
            elif (self.value > 0 and board[self.y+i[0]][self.x+i[1]] < 0
                or self.value < 0 and board[self.y+i[0]][self.x+i[1]] > 0):
                king_list.append((self.y+i[0],self.x+i[1]))
        return king_list

    def pawn_moves(self):
        pawn_list = []
        if self.color == 'black':
            step_length = -1
            dia = -1
            if self.y == 1:
                step_length = -2
        else:
            step_length = 1
            dia = 1
            if self.y == 6:
                step_length = 2
        for i in range(dia,step_length+dia,dia):
            if self.y-i < 0 or self.y-i > 7:
                print('broke')
                break
            elif board[self.y-i][self.x] == 0:
                pawn_list.append((self.y-i,self.x))
            else:
                break
        if self.color == 'black':
            if self.x+dia > 7 or self.x+dia < 0:
                pass
            elif board[self.y-dia][self.x+dia] > 0:
                pawn_list.append((self.y-dia,self.x+dia))
            if self.x-dia > 7 or self.x-dia < 0:
                pass
            elif board[self.y-dia][self.x-dia] > 0:
                pawn_list.append((self.y-dia,self.x-dia))
        elif self.color == 'white':
            if self.x+dia > 7 or self.x+dia < 0:
                pass
            elif board[self.y-dia][self.x+dia] < 0:
                pawn_list.append((self.y-dia,self.x+dia))
            if self.x-dia > 7 or self.x-dia < 0:
                pass
            elif board[self.y-dia][self.x-dia] < 0:
                pawn_list.append((self.y-dia,self.x-dia))
        return pawn_list

    def rook_moves(self): # Gather all possible rook moves from a given y,x
        rook_list = []
        for i in ((-1,0),(1,0),(0,-1),(0,1)):
            for k in range(1,len(board)):
                if (self.y+(k*i[0]) > 7
                    or self.y+(k*i[0]) < 0
                    or self.x+(k*i[1]) > 7
                    or self.x+(k*i[1]) < 0):                
                    break
                elif board[self.y+(k*i[0])][self.x+(k*i[1])] == 0:
                    rook_list.append((self.y+(k*i[0]),self.x+(k*i[1])))
                        
                elif(self.color == 'black' and board[self.y+(k*i[0])][self.x+(k*i[1])] > 0
                    or self.color == 'white' and board[self.y+(k*i[0])][self.x+(k*i[1])] < 0):
                    rook_list.append((self.y+(k*i[0]),self.x+(k*i[1])))
                    break
                else:
                    break
        return rook_list

    def bishop_moves(self):
        bishop_list = []
        for i in ((-1,-1),(1,1),(1,-1),(-1,1)):
            for k in range(1,len(board)):
                if (self.y+(k*i[0]) > 7
                    or self.y+(k*i[0]) < 0
                    or self.x+(k*i[1]) > 7
                    or self.x+(k*i[1]) < 0):                
                    break
                elif board[self.y+(k*i[0])][self.x+(k*i[1])] == 0:
                    bishop_list.append((self.y+(k*i[0]),self.x+(k*i[1])))
                        
                elif(self.color == 'black' and board[self.y+(k*i[0])][self.x+(k*i[1])] > 0
                    or self.color == 'white' and board[self.y+(k*i[0])][self.x+(k*i[1])] < 0):
                    bishop_list.append((self.y+(k*i[0]),self.x+(k*i[1])))
                    break
                else:
                    break
        return bishop_list


def redraw_board():
    win.fill(board_edge)
    for i in range(len(board)):
        for j in range(len(board[0])):
            if (i+j)%2 == 1:
                pygame.draw.rect(win, board_black, (i*60+20,j*60+20,60,60))
            else:
                pygame.draw.rect(win, board_white, (i*60+20,j*60+20,60,60))

def redraw_pieces():
    for i in range(8):
        for j in range(8):
            if board[i][j] < 0:
                        temp = 7-abs(board[i][j])+6
            elif board[i][j] > 0:
                temp = 7-abs(board[i][j])
            else:
                continue
            image = pygame.image.load(os.getcwd()+r'\sprites\chess_pieces ('+str(temp)+').png')
            win.blit(image, (j*60+20, i*60+20))
    pygame.display.flip()


def where(xy):
    int_xy = []
    for i in range(len(xy)-1,-1,-1):
        if xy[i] <= 500:
            int_xy.append((xy[i]-20) // 60)
    if len(int_xy) == 2:
        return int_xy
    else:
        return

def highlight(temp):
    for i in temp:
        pygame.draw.rect(win, red, (i[1]*60+25,i[0]*60+25,50,50))

redraw_board()
redraw_pieces()

run = True
done = False
moves = []
current_piece = 0

while run:

    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.MOUSEBUTTONDOWN and done == False:
            temp = pygame.mouse.get_pos()
            click = where(temp)            
            if not click:
                continue
            elif moves.count(click) > 0:
                if board[current_piece[0]][current_piece[1]] == 1 and click[0] == 0:
                    board[click[0]][click[1]] = 5
                elif board[current_piece[0]][current_piece[1]] == -1 and click[0] == 7:
                    board[click[0]][click[1]] = -5
                else:
                    board[click[0]][click[1]] = board[current_piece[0]][current_piece[1]]
                board[current_piece[0]][current_piece[1]] = 0
                redraw_board()
                redraw_pieces()
                moves = []
                if turn == 'white':
                    turn = 'black'
                    pygame.display.set_caption("Chess (%s's turn)" % turn)

                elif turn == 'black':
                    turn = 'white'
                    pygame.display.set_caption("Chess (%s's turn)" % turn)


            elif board[click[0]][click[1]] == 0:
                continue
            elif (board[click[0]][click[1]] < 0 and turn == 'black' 
                or board[click[0]][click[1]] > 0 and turn == 'white'):
                moves = piece().init(click[0],click[1],board[click[0]][click[1]])
                if not moves:
                    pass
                else:
                    redraw_board()
                    highlight(moves)
                    redraw_pieces()
            else:
                continue
                    
            current_piece = click
    single_board = []
    for i in range(8):
        for j in range(8):
            single_board.append(board[i][j])
    if single_board.count(6) == 0 and done == False:
        print('game over, black won')
        pygame.display.set_caption('Black has won the game!')
        pygame.draw.rect(win,(0,0,0,100),(width,height,height,width))
        done = True
    elif single_board.count(-6) == 0 and done == False:
        print('game over, white won')
        pygame.display.set_caption('White has won the game!')
        done = True
                
    pygame.display.flip()

pygame.quit()
