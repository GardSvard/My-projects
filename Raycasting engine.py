
import pygame
import math


def darken(color,shader = 30):
    done = []
    for i in range(3):
        if color[i] < shader:
            done.append(0)
        else:
            done.append(color[i]-shader)
    return done

black = (0,0,0)
light_black = (50,50,50)
white = (255,255,255)
dark_white = (220,220,220)
dark_grey = (169,169,169)
board_black = (179,134,108)
board_white = (243,222,198)
board_edge = (124,87,65)
red = (178,34,34)
dark_red = (255,50,50)
light_blue = (50,50,200)
blue = (0,0,200)
green = (0,200,0)
light_green = (100,255,100)
yellow = (200,200,0)
light_yellow = (255,255,50)
sky_blue = (105,180,255)
floor = (200,100,70)
brown = (139,69,19)
light_brown = (210,105,30)
purple = (80,5,94)
light_purple = (201,71,245)

colors = {
    '0' : (darken(board_white),board_white),
    '1' : (red,dark_red),
    '2' : (black,light_black), #the darker shade first
    '3' : (dark_white,white),
    '4' : (red,dark_red),
    '5' : (green,light_green),
    '6' : (blue,light_blue),
    '7' : (yellow,light_yellow),
    '8' : (brown,light_brown),
    '9' : (purple,light_purple)
}

board = [   
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [2, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [2, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [2, 0, 4, 0, 0, 3, 3, 0, 3, 3, 0, 0, 4, 0, 2],
    [2, 0, 0, 0, 3, 0, 0, 0, 0, 0, 3, 0, 0, 0, 2],
    [2, 0, 0, 0, 3, 0, 0, 0, 0, 0, 3, 0, 0, 0, 2],
    [2, 0, 0, 0, 3, 0, 0, 1, 0, 0, 3, 0, 0, 0, 2],
    [2, 0, 5, 0, 3, 0, 0, 0, 0, 0, 3, 0, 0, 0, 2],
    [2, 0, 0, 0, 0, 3, 3, 3, 3, 3, 0, 0,10, 0, 2],
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [2, 0, 8, 0, 0, 0, 0, 6, 0, 0, 0, 0, 9, 0, 2],
    [2, 0, 0, 0,10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
]

tex1 = [
    [2, 3, 2, 3],
    [3, 2, 3, 2],
    [2, 3, 2, 3],
    [3, 2, 3, 2]
]

tex6 = [
    [3, 3, 3, 3],
    [3, 2, 2, 3],
    [3, 2, 2, 3],
    [3, 3, 3, 3]
]

tex3 = [
    [3, 3, 2, 3, 3, 3, 3, 3, 3, 3],
    [3, 2, 2, 2, 2, 2, 3, 3, 3, 3],
    [3, 3, 2, 3, 3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 2, 3, 2, 3, 3, 3],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
    [3, 3, 3, 2, 3, 3, 3, 2, 3, 3],
    [3, 3, 3, 3, 2, 2, 2, 3, 3, 3],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
]

tex4 = [
    [7, 7, 7, 7, 7, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
    [7, 7, 7, 7, 7, 6, 6, 6, 6, 3, 3, 6, 3, 3, 6],
    [7, 7, 7, 7, 6, 6, 6, 6, 3, 3, 3, 3, 3, 3, 3],
    [7, 7, 7, 7, 6, 6, 6, 4, 3, 3, 3, 3, 3, 3, 3],
    [7, 7, 6, 6, 6, 6, 4, 4, 4, 6, 6, 6, 6, 6, 6],
    [6, 6, 3, 3, 6, 4, 4, 7, 4, 4, 6, 6, 6, 6, 6],
    [3, 3, 3, 3, 3, 6, 4, 4, 4, 6, 6, 6, 6, 6, 6],
    [3, 3, 3, 3, 3, 6, 6, 5, 6, 6, 6, 3, 3, 3, 6],
    [6, 6, 6, 6, 6, 6, 6, 5, 5, 6, 3, 3, 3, 3, 3],
    [6, 6, 6, 6, 6, 6, 5, 5, 6, 6, 3, 3, 3, 3, 3],
    [6, 6, 6, 6, 6, 6, 6, 5, 6, 6, 6, 6, 6, 6, 6],
    [6, 6, 6, 6, 6, 6, 6, 5, 6, 6, 6, 6, 6, 6, 6],
    [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
    [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
    [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
]

tex5 = [
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 3, 2, 3, 3, 3, 3, 3, 3, 2, 2, 3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 2, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 2, 2, 3, 3, 3, 3, 3],
    [3, 3, 2, 2, 2, 3, 3, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 2, 2, 3, 3, 3, 3, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3],
    [3, 3, 2, 3, 3, 3, 2, 3, 3, 3, 3, 2, 2, 3, 3, 3, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 3, 3, 3, 2, 2, 3, 3, 3, 3],
    [3, 2, 3, 3, 3, 2, 3, 3, 3, 2, 3, 3, 3, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 2, 2, 2, 2, 3, 3, 3, 2, 3, 3, 3, 2, 3, 3, 3, 3],
    [3, 2, 3, 3, 3, 2, 3, 3, 3, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 3, 3, 3, 3, 3, 3, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 2, 3, 3, 3, 3],
    [3, 2, 3, 3, 3, 2, 3, 3, 2, 2, 3, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 2, 2, 3, 3, 3, 3, 2, 2, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3],
    [3, 2, 3, 3, 3, 2, 3, 3, 3, 2, 3, 3, 3, 2, 2, 2, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 3, 3, 3, 3, 3, 2, 2, 3, 3, 3, 2, 2, 3, 3, 3, 3, 3],
    [3, 3, 2, 3, 3, 3, 3, 3, 3, 2, 2, 3, 3, 3, 2, 3, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 3, 3, 3, 3, 3, 3, 2, 2, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3],
    [3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 2, 2, 2, 3, 2, 3, 3, 3, 3, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 3, 3, 2, 3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 2, 2, 3, 2, 2, 2, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 2, 3, 2, 2, 3, 2, 3, 3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 2, 3, 3, 2, 2, 2, 2, 2, 3, 2, 3, 3, 3, 3, 3, 2, 3, 3, 3, 2, 3, 3, 2, 3, 2, 3, 2, 3, 2, 2, 3, 2, 3, 3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 2, 3, 2, 3, 3, 2, 2, 2, 2, 3, 3, 3, 3, 3, 2, 3, 3, 3, 2, 3, 3, 2, 3, 2, 3, 2, 2, 2, 2, 3, 2, 3, 3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 2, 2, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 2, 3, 3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 2, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 2, 2, 3, 3, 2, 3, 3, 3, 3, 3, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 2, 3, 2, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 2, 2, 3, 2, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 2, 3, 3, 2, 3, 2, 3, 2, 3, 2, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 3, 3, 3, 3, 2, 3, 3, 3, 2, 3, 3, 3, 2, 3, 2, 3, 2, 2, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
]

tex2 = [
    [4, 4, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 4, 4, 0],
    [4, 4, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 4, 4, 0],
    [4, 4, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 4, 4, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4],
    [4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4],
    [4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [4, 4, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 4, 4, 0],
    [4, 4, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 4, 4, 0],
    [4, 4, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 4, 4, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4],
    [4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4],
    [4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [4, 4, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 4, 4, 0],
    [4, 4, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 4, 4, 0],
    [4, 4, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 4, 4, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4],
    [4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4],
    [4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [4, 4, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 4, 4, 0],
    [4, 4, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 4, 4, 0],
    [4, 4, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 4, 4, 0],
]

tex7 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 0, 7, 7, 7, 0, 0, 0, 0, 0, 0, 5, 5, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 0, 7, 7, 7, 0, 7, 7, 7, 7, 7, 0, 0, 0, 5, 5, 5, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 7, 7, 7, 0, 0, 7, 7, 7, 0, 0, 5, 0, 0, 5, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 4, 4, 4, 4, 7, 7, 7, 7, 7, 0, 0, 0, 5, 0, 0, 0, 5, 5, 0],
    [0, 0, 0, 0, 0, 0, 4, 4, 4, 0, 0, 0, 0, 4, 4, 4, 7, 7, 0, 0, 5, 0, 0, 0, 0, 5, 0],
    [0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 0, 0, 0, 5, 0, 0, 0, 0, 0, 5],
    [0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 0, 0, 5, 0, 0, 0, 0, 0, 5],
    [0, 0, 0, 0, 0, 0, 4, 0, 0, 4, 0, 0, 0, 4, 0, 0, 0, 4, 0, 0, 5, 0, 0, 0, 0, 0, 5],
    [0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 5, 0, 0, 0, 0, 0, 5],
    [0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 5, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 4, 0, 0, 0, 4, 4, 0, 0, 0, 4, 0, 0, 4, 0, 5, 5, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 4, 4, 4, 0, 0, 4, 0, 0, 5, 5, 5, 5, 5, 5, 5, 5],
    [0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 5, 5, 5, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 4, 4, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 0, 4, 4, 4, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 5, 5, 5, 5, 5, 5, 0, 0, 0, 0, 0, 0, 5, 5, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 0, 0, 0, 0, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 5, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]


tex8 = [
    [9, 3, 9, 3],
    [3, 9, 3, 9],
    [9, 3, 9, 3],
    [3, 9, 3, 9]
]

tex9 = [
    [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 7, 7, 7, 7],
    [6, 6, 6, 3, 6, 3, 6, 6, 6, 6, 6, 6, 0, 0, 0, 0, 0, 0, 0, 7, 0, 2, 2, 2, 2, 2, 2],
    [6, 3, 6, 6, 6, 6, 6, 3, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 7, 2, 2, 7, 7, 2],
    [6, 6, 3, 3, 3, 3, 3, 6, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 7, 7],
    [6, 6, 6, 6, 6, 6, 6, 6, 0, 0, 6, 0, 6, 3, 3, 0, 0, 3, 3, 0, 7, 0, 0, 7, 7, 7, 2],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 3, 3, 3, 3, 3, 3, 7, 0, 0, 0, 0, 2, 2, 7],
    [6, 0, 0, 0, 6, 0, 0, 0, 6, 0, 0, 0, 0, 0, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 7],
    [6, 0, 6, 0, 6, 0, 6, 0, 6, 0, 0, 0, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0],
    [0, 0, 6, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 2, 7, 2, 7, 2, 0, 0, 0, 0, 7, 0, 0, 7, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 0, 0, 0, 2, 7, 2, 7, 2, 2, 0, 0, 0, 0, 0, 7, 0, 0],
    [0, 0, 0, 4, 4, 0, 0, 4, 1, 4, 0, 0, 0, 2, 7, 2, 7, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 4, 1, 4, 0, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 4, 7, 7, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 4, 0, 0, 0, 7, 7, 7, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 4, 4, 7, 7, 7, 4, 4, 8, 0, 0, 0, 8, 0, 0, 0, 0, 4, 4, 0, 0, 0, 0, 4, 4],
    [0, 0, 4, 4, 0, 4, 5, 4, 0, 0, 4, 8, 0, 8, 0, 0, 8, 0, 0, 4, 4, 4, 4, 0, 4, 4, 4],
    [0, 0, 0, 4, 0, 0, 5, 1, 8, 0, 8, 8, 8, 8, 8, 8, 0, 0, 0, 0, 4, 4, 4, 0, 4, 1, 4],
    [0, 0, 0, 0, 0, 0, 5, 4, 4, 8, 8, 2, 2, 2, 8, 0, 0, 8, 0, 0, 4, 4, 4, 4, 0, 4, 4],
    [0, 0, 0, 0, 0, 0, 5, 0, 8, 0, 0, 2, 2, 2, 0, 8, 8, 0, 0, 0, 0, 4, 4, 0, 4, 4, 0],
    [3, 0, 0, 5, 5, 0, 5, 0, 5, 0, 0, 0, 2, 0, 0, 0, 0, 8, 0, 0, 0, 0, 4, 0, 4, 0, 0],
    [0, 3, 0, 3, 5, 5, 5, 5, 5, 0, 0, 6, 6, 6, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 6, 0],
    [3, 0, 0, 0, 3, 5, 5, 5, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 3, 0, 3, 0, 0, 5, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 0],
    [0, 0, 0, 0, 5, 5, 5, 5, 5, 5, 2, 2, 5, 2, 2, 5, 5, 5, 5, 5, 0, 6, 0, 0, 0, 0, 6],
    [0, 0, 5, 8, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 0, 0, 0, 0, 0, 0],
    [0, 5, 8, 8, 8, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 0, 0, 0, 0],
    [5, 8, 8, 8, 8, 8, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 0],
]

text = {
    '2' : tex1,
    '3' : tex2,
    '4' : tex3,
    '5' : tex4,
    '6' : tex5,
    '7' : tex6,
    '8' : tex7,
    '9' : tex8,
    '10': tex9,
}

pygame.init()

font = pygame.font.SysFont('ClearSans-Bold.ttf', 15)

height = 600
width = 520
game_width = 800
show_board = False

win = pygame.display.set_mode((width*show_board+game_width,height))
superShotgun = pygame.image.load('super shotgun animations.png')

pygame.display.set_caption("Raycasting engine")

og_board = board

board_size = len(board)

player_dir = 90.5
player_speed = [0,0]
move_speed = 30/board_size
turn_speed = 3
looking = 0

clock = pygame.time.Clock()

fish_eye = False
fov = 70
resolution = 200 #should be less than game_width
per_degree = fov/resolution #how many degrees per repetition of the for loop below

blockSize = height/board_size #Set the size of the grid block
for i in range(len(board)):
    try:
        a = board[i].index(1)
        playerx = a*blockSize+blockSize/2
        playery = i*blockSize+blockSize/2
    except:
        pass



def draw_board():
    if show_board == True:
        y = board_size
        x = board_size
        for i in range(y):
            for j in range(x):
                l = board[j][i]
                l = colors[str(l)]
                l = l[1]
                pygame.draw.rect(win, l, (blockSize*i,blockSize*j,blockSize,blockSize))

        drawGrid()

    pygame.draw.rect(win,sky_blue,((width*show_board,0),(width*show_board+game_width,height/2)))
    pygame.draw.rect(win,floor,((width*show_board,height/2),(width*show_board+game_width,height)))

    start = player_dir-fov/2 #start position for the raycasting relative to the looking direction
    xwall = width*show_board+game_width
    distances = []

    for h in range(resolution):

        start += per_degree
        degree = fix_dir(start)
        points = cast_ray(flipy((playerx,playery)),degree)
        #points is a tuple of lists with tuples, and the first list is vertical points, other is horizontal
        h1 = hypotenus((playerx/blockSize,playery/blockSize),flipyboard(points[0]))
        #hypotenus for last vertical point
        h2 = hypotenus((playerx/blockSize,playery/blockSize),flipyboard(points[1]))
        #same for last horizontal point
        vertical = False
        horizontal = False
        if h1 < h2: #checks which point to use, horizontal point or vertical
            distanceto = h1
            vertical = True
            point = points[0]
            tex = text[str(points[0][2])]
            x = point[1]-math.floor(point[1])
            shade = 1

        else:
            distanceto = h2
            horizontal = True
            point = points[1]
            tex = text[str(points[1][2])]
            x = point[0]-math.floor(point[0])
            shade = 0

        if show_board:
            a = flipyboardtocoord(point)
            if vertical == True:
                pygame.draw.line(win,red,(playerx,playery),a,1)
            else:
                pygame.draw.line(win,dark_red,(playerx,playery),a,1)

        texlen = len(tex)
        distances.append((h,distanceto))

        if fish_eye == True:
            k = distanceto
        else:
            k = distanceto*math.cos(math.radians(abs(player_dir-degree)))
        k /= 1.5
        wall_height = 400/k
        y = (height-wall_height)/2
        per_res = game_width/resolution
        xwall -= per_res
        colorlen = wall_height/texlen


        if horizontal:
            if start > 180:
                ax = texlen-int(math.floor(x*texlen))-1
            else:
                ax = int(math.floor(x*texlen))

        else:
            if start > 270 or start < 90:
                ax = texlen-int(math.floor(x*texlen))-1
            else:
                ax = int(math.floor(x*texlen))

        for i in range(texlen):
            color = colors[str(tex[i][ax])][shade]
            pygame.draw.rect(win,color,(xwall,y + colorlen*i,per_res+1,colorlen+1))   

    if show_board:
        x,y = chode((playerx,playery),player_dir)
        pygame.draw.line(win,black,(playerx,playery),(x,playery-(y-playery)),3)
        pygame.draw.circle(win,black,(playerx,playery),8)
        pygame.draw.circle(win,white,(playerx,playery),7)
    pygame.display.flip()

def drawGrid():
    linewidth = 3
    for i in range(1,board_size):
        pygame.draw.line(win,black,(0,i*blockSize),(width*show_board,i*blockSize),linewidth)
    for i in range(1,board_size+1):
        pygame.draw.line(win,black,(i*blockSize,0),(i*blockSize,height),linewidth)

def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()

def chode(pos, direction):
    length = 25
    x,y = trig(direction,length)
    x*blockSize
    y*blockSize
    return x+pos[0],pos[1]+y

def hypotenus(coords1,coords2):
    if coords1[0] < coords2[0]:
        a = coords2[0]-coords1[0]
    else:
        a = coords1[0]-coords2[0]
    if coords1[1] < coords2[1]:
        b = coords2[1]-coords1[1]
    else:
        b = coords1[1]-coords2[1]
    c = math.sqrt(a**2+b**2)
    return c

def trig(direction,length=50):
    y = math.sin(math.radians(direction))
    y *= length
    x = math.cos(math.radians(direction))
    x *= length
    return x,y

def cast_ray(pos,direction):
    depth = board_size
    x2,y2 = chode(pos,direction)
    x2 /= blockSize
    y2 /= blockSize
    tx1,ty1 = pos[0]/blockSize,pos[1]/blockSize
    pointshor = []
    pointsver = []
    x1,y1 = tx1,ty1
    if y2 < y1 and x2 > x1:
        bottom_right = -1
    else:
        bottom_right = 1
   
    if y2 > y1 and x2 < x1:
        top_left = -1
    else:
        top_left = 1

    if y2 < y1 and x2 < x1:
        bottom_left = -1
    else:
        bottom_left = 1

    try:
        m = (y1-y2)/(x1-x2)
    except:
        m = (y1-y2)/(x1+0.01-x2)

    if m == 0:
        m += 0.01
   
    first_step = False

    for i in range(depth): #vertical line finder
        if first_step == False:
            if top_left == -1 or bottom_left == -1:
                y1 += (x1-math.floor(x1))*m*top_left*bottom_left
                x1 += (x1-math.floor(x1))*top_left*bottom_left
            else:
                y1 += (math.ceil(x1)-x1)*m*top_left*bottom_left
                x1 += (math.ceil(x1)-x1)*top_left*bottom_left
            pointsver.append([x1,y1])
            first_step = True
        else:
            x1 += 1*top_left*bottom_left
            y1 += m*top_left*bottom_left
            pointsver.append([x1,y1])

        x,y = pointsver[-1]

        y = board_size-math.floor(y)-1

        if valid(x,y,True) == False:
            break

        if direction > 90 and direction < 270:
            if board[y][int(x)-1] > 1:
                pointsver[-1].append(board[y][int(x)-1])
                break

        else:
            if board[y][int(x)] > 1:
                pointsver[-1].append(board[y][int(x)])
                break

    first_step = False

    x1,y1 = tx1,ty1
    for i in range(depth): #horizontal line finder
        if first_step == False:
            if bottom_right == -1 or bottom_left == -1:
                x1 += (y1-math.floor(y1))*1/m*bottom_right*bottom_left
                y1 += (y1-math.floor(y1))*bottom_right*bottom_left
            else:
                x1 += (math.ceil(y1)-y1)*1/m*bottom_right*bottom_left
                y1 += (math.ceil(y1)-y1)*bottom_right*bottom_left
            pointshor.append([x1,y1])
            first_step = True
        else:
            y1 += 1*bottom_right*bottom_left
            x1 += (1/m)*bottom_right*bottom_left
            pointshor.append([x1,y1])

        x,y = pointshor[-1]
    
        y = (int(board_size)-y)
        x = math.floor(x)

        if not valid(x,y,True):
            break

        if direction > 180:
            if board[int(y)][x] > 1:
                pointshor[-1].append(board[int(y)][x])
                break

        else:
            if board[int(y)-1][x] > 1:
                pointshor[-1].append(board[int(y)-1][x])
                break

    return pointsver[-1],pointshor[-1]
#returns all intersecting points with line of sight and 'ver', vertical lines, and 'hor', horizontal lines


def fix_dir(direction):
    if direction < 0:
        direction += 360
    elif direction > 360:
        direction -= 360
    return direction

def valid(x,y,board_use = False): #make this true if you want to use the data for the board and not the screen
    if board_use == True:
        a = -1
    else:
        a = 0
    if x < 0 or x > board_size+a or y < 0 or y > board_size+a:
        return False
    else:
        return True

def flipy(coords, h = height):
    return (coords[0], h - coords[1])

def flipyboardtocoord(coords, h = board_size):
    return (coords[0]*blockSize, (h - coords[1])*blockSize)

def flipyboard(coords, h = board_size):
    return (coords[0], h - coords[1])


run = True
done = False
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN and done == False:
       
            if event.key==pygame.K_w: #da up key
                player_speed[1] += move_speed
            if event.key==pygame.K_a: #da up key
                player_speed[0] -= move_speed
            if event.key==pygame.K_s: #da up key
                player_speed[1] -= move_speed
            if event.key==pygame.K_d: #da up key
                player_speed[0] += move_speed
            if event.key==pygame.K_LEFT:
                looking += turn_speed
            if event.key==pygame.K_RIGHT:
                looking -= turn_speed


        if event.type == pygame.KEYUP and done == False:
            if event.key==pygame.K_w: #da up key
                player_speed[1] -= move_speed
            if event.key==pygame.K_a: #da up key
                player_speed[0] += move_speed
            if event.key==pygame.K_s: #da up key
                player_speed[1] += move_speed
            if event.key==pygame.K_d: #da up key
                player_speed[0] -= move_speed
            if event.key==pygame.K_LEFT:
                looking -= turn_speed
            if event.key==pygame.K_RIGHT:
                looking += turn_speed

       
        if event.type == pygame.MOUSEBUTTONDOWN and done == False:
            pass

    if player_speed[0] != 0 and player_speed[1] != 0:
        if player_speed[0] == player_speed[1]:
            offset = -45
        else:
            offset = 45
        direction = fix_dir(player_dir+offset)

        if player_speed[1] < 0:
            back = -1
        else:
            back = 1

        x1,y1 = trig(direction,move_speed)
        y1 *= back
        x1 *= back
        x2,y2 = 0,0

    else:
        if player_speed[1] != 0:
            x1,y1 = trig(player_dir,player_speed[1])
        else:
            x1,y1 = 0,0

        if player_speed[0] != 0:
            x2,y2 = trig(fix_dir(player_dir-90),player_speed[0])
        else:
            x2,y2 = 0,0


    changed_speed = [x1+x2,-(y1+y2)]

    if board[int(playery//(blockSize))][int(((playerx -(changed_speed[0]<0)*move_speed*4 + (changed_speed[0]>0)*move_speed*4))//(blockSize))] < 2:
        playerx += changed_speed[0]
    if board[int((playery + (changed_speed[1]>0)*move_speed*4 - (changed_speed[1]<0)*move_speed*4)//(blockSize))][int(playerx//(blockSize))] < 2:
        playery += changed_speed[1]

    player_dir += looking
    player_dir = fix_dir(player_dir)

    draw_board()
    print(clock.tick(60))

pygame.quit()
