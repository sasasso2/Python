# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 14:13:44 2019

@author: sasas
"""

board = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
board_check = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']

turn = 0
win = False

print("Lets play Tic-Tac-Toe!")
player1_choose = ""
player2_choose = ""
player1 = input("Enter a name for player 1 and press enter, leave blank to leave as Player 1: ")
player2 = input("Enter a name for player 2 and press enter, leave blank to leave as Player 2: ")

#sets the players name
if (player1 == "" or player2 == ""):
    if (player1 == ""):
        player1 = "Player 1"
    if (player2 == ""):
        player2 = "Player 2"
else:
    pass

#assigns X or O to players

player1_choose = input(player1 + ", choose X or O: ").upper()
if (player1_choose == "X"):
    player2_choose = "O"
else:
    player2_choose = "X"

        
def print_board(board):
    print(board[0], '|', board[1], '|', board[2])
    print(board[3], '|', board[4], '|', board[5])
    print(board[6], '|', board[7], '|', board[8])

#check to see if a position is free    
def position_free(position, x):
    if position in board:
        if position == 'A1':
            board[0] = x
        if position == 'A2':
            board[1] = x
        if position == 'A3':
            board[2] = x
        if position == 'B1':
            board[3] = x
        if position == 'B2':
            board[4] = x
        if position == 'B3':
            board[5] = x
        if position == 'C1':
            board[6] = x
        if position == 'C2':
            board[7] = x
        if position == 'C3':
            board[8] = x
        print_board(board)
        return True
    else:
        print('Position taken. Please enter a new, correct position.')
        return False
            
    
  
    
    
#checks to see if someone won
def check_win(board):
    if board[0] == 'X' and board[3] == 'X' and board[6] == 'X':
        win = 1
        print(player1, 'wins!')
        return False
    elif board[1] == 'X' and board[4] == 'X' and board[7] == 'X':
        win = 1
        print(player1, 'wins!')
        return False
    elif board[2] == 'X' and board[5] == 'X' and board[8] == 'X':
        win = 1
        print(player1, 'wins!')
        return False
    elif board[0] == 'X' and board[1] == 'X' and board[2] == 'X':
        win = 1
        print(player1, 'wins!')
        return False
    elif board[3] == 'X' and board[4] == 'X' and board[5] == 'X':
        win = 1
        print(player1, 'wins!')
        return False
    elif board[6] == 'X' and board[7] == 'X' and board[8] == 'X':
        win = 1
        print(player1, 'wins!')
        return False
    elif board[0] == 'X' and board[4] == 'X' and board[8] == 'X':
        win = 1
        print(player1, 'wins!')
        return False
    elif board[2] == 'X' and board[4] == 'X' and board[6] == 'X':
        win = 1
        print(player1, 'wins!')
        return False
    elif board[0] == 'O' and board[3] == 'O' and board[6] == 'O':
        win = 1
        print(player2, 'wins!')
        return False
    elif board[1] == 'O' and board[4] == 'O' and board[7] == 'O':
        win = 1
        print(player2, 'wins!')
        return False
    elif board[2] == 'O' and board[5] == 'O' and board[8] == 'O':
        win = 1
        print(player2, 'wins!')
        return False
    elif board[0] == 'O' and board[1] == 'O' and board[2] == 'O':
        win = 1
        print(player2, 'wins!')
        return False
    elif board[3] == 'O' and board[4] == 'O' and board[5] == 'O':
        win = 1
        print(player2, 'wins!')
        return False
    elif board[6] == 'O' and board[7] == 'O' and board[8] == 'O':
        win = 1
        print(player2, 'wins!')
        return False
    elif board[0] == 'O' and board[4] == 'O' and board[8] == 'O':
        win = 1
        print(player2, 'wins!')
        return False
    elif board[2] == 'O' and board[4] == 'O' and board[6] == 'O':
        win = 1
        print(player2, 'wins!')
        return False
    #creats a tie
    elif not any(i in board_check for i in board):
        print( 'draw!')
        return False
    else: 
        return True

#checking to see if position is valid and available
game =  True
while game:       
    pos_valid = False
    while not pos_valid:
        position=(input('Choose a position: '))
        pos_valid = position_free(position, player1_choose)
    game = check_win(board)
    if game == False:
        break
    pos_valid = False
    while not pos_valid:
        position=(input('Choose a position: '))
        pos_valid = position_free(position, player2_choose)
    game = check_win(board)

        
