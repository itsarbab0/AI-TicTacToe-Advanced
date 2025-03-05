import sys
import pygame
import numpy as np

pygame.init()
###  Defining Colors
White = (255, 255, 255)
Grey = (180, 180, 180)
Red = (255, 0, 0)
Green = (0, 255, 0)
Black = (0, 0, 0)
###  Defining GAme Board

Width = 300
Height = 300
Line_Width = 5
Board_Col = 3
Board_Rows = 3
Sq_Size = Width // Board_Col
Circle_Rad = Sq_Size // 3
Circle_Width = 15
Cross_Width = 25


### Defining Screen
Screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption(" Tic Tac Toe AI")
Screen.fill(Black)

### Creating Borad
Board = np.zeros((Board_Rows, Board_Col))

### Defining Functions
def Boardlines(color = White):
    for i in range(1, Board_Rows):
        pygame.draw.line(Screen, color, (0, Sq_Size * i), (Width, Sq_Size * i), Line_Width) # Horizontal Lines
        pygame.draw.line(Screen, color, (Sq_Size * i, 0), (Sq_Size * i, Height), Line_Width) # Vertical Lines

def draw_Board(color = White):
    for row in range(Board_Rows):
        for col in range(Board_Col):
            if Board[row][col] == 1:
                pygame.draw.circle(Screen, color, (int(col * Sq_Size + Sq_Size // 2), int(row * Sq_Size + Sq_Size // 2)), Circle_Rad, Circle_Width)
            elif Board[row][col] == 2:
                pygame.draw.line(Screen, color, (col * Sq_Size + Sq_Size // 4, row * Sq_Size + Sq_Size // 4), (col * Sq_Size + 3 * Sq_Size // 4, row * Sq_Size + 3 * Sq_Size // 4))
                pygame.draw.line(Screen, color, (col * Sq_Size + Sq_Size // 4, row * Sq_Size + 3 * Sq_Size // 4), (col * Sq_Size + 3 * Sq_Size // 4, row * Sq_Size + Sq_Size // 4))
                
###  Marking Squares
def markSquare(row, col, player):
    Board[row][col] = player

###   Checkingh availability of the position
def pos_Avail(row, col):
    return Board[row][col] == 0

###  Checking if the board is full
def check_Boardfull(checkBoard = Board):
    for row in range(Board_Rows):
        for col in range(Board_Col):
            if checkBoard[row][col] == 0:
                return True
            
    return False 
### Check the Winning Condition
def chech_Win(player, checkBoard = Board):
    for col in range(Board_Col):
        if checkBoard[0][col] == player and checkBoard[1][col] == player and checkBoard[2][col] == player: 
            return True
        
    for row in range(Board_Rows):
        if checkBoard[row][0] == player and checkBoard[row][0] == player and checkBoard[row][0] == player: 
            return True
        
    if checkBoard[0][0] == player and checkBoard[1][1] == player and checkBoard[2][2] == player:
        return True
    if checkBoard[0][2] == player and checkBoard[1][1] == player and checkBoard[2][0] == player:
        return True
    
    return False

###  MiniMax The Main Function for the Game Which is basically the Whole Backbone of the Game
def miniMax(minMaxBoard, depth, maxiMizing):
     