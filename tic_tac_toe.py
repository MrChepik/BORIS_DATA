#!/usr/bin/env python3
#-*- coding: 'utf-8' -*-

import numpy as np
import random
from time import sleep

#Create an empty board
# def create_board():
	# return(np.array([[0, 0, 0],
					# [0, 0, 0],
					# [0, 0, 0]]))
					
def create_board(): 
	return(np.array([[0, 0, 0], 
					[0, 0, 0], 
					[0, 0, 0]])) 

# #Check empty spaces on board
# def empty_board(board):
	# l = []
	# for i in range(len(board)):
		# for j in range(len(board)):
			# if board[i][j] == 0:
				# l.append((i, j))
	#return(l)

def possibilities(board): 
	l = [] 
	
	for i in range(len(board)): 
		for j in range(len(board)): 
			
			if board[i][j] == 0: 
				l.append((i, j)) 
	return(l) 

# #Select a randome place for a player	
# def random_place(board, player):
	# selection = possibilities(board)
	# current_location = random.choice(selection)
	# board[current_location] = player
	# return(board)
	
def random_place(board, player): 
	selection = possibilities(board) 
	current_loc = random.choice(selection) 
	board[current_loc] = player 
	return(board) 


# #check player marks on horizontal row

# def horizontal_pos(board, player):
	# for x in range(len(board)):
		# win = True
		
		# for y in range(len(board)):
			# if board[x, y] != player:
				# win = False
				# continue
		# if win == True:
			# return(win)
	# return(win)
	
def row_win(board, player): 
	for x in range(len(board)): 
		win = True
		
		for y in range(len(board)): 
			if board[x, y] != player: 
				win = False
				continue
				
		if win == True: 
			return(win) 
	return(win) 


# #check player marks on vertical row

# def vertical_pos(board, player):
	# for x in range(len(board)):
		# win = True
		
		# for y in range(len(board)):
			# if board[y] [x] != player:
				# win = False
				# continue
		# if win == True:
			# return(win)
	# return(win)
	
def col_win(board, player): 
	for x in range(len(board)): 
		win = True
		
		for y in range(len(board)): 
			if board[y][x] != player: 
				win = False
				continue
				
		if win == True: 
			return(win) 
	return(win) 


# #check player marks on diagonal row	
# def diagonal_position(board, player):
	# win = True
	
	# for x in range(len(board)):
		# if board[x, x] != player:
			# win = False
	# return(win)
	
def diag_win(board, player): 
	win = True
	
	for x in range(len(board)): 
		if board[x, x] != player: 
			win = False
	return(win) 

# #check the winner in the tie

# def check_a_winner(board):
	# winner = 0
	
	# for player in [1, 2]:
		# if (horizontal_pos(board, player) or
			# vertical_pos(board, player) or
			# diagonal_position(board, player)):
				# winner = player
				
	# if np.all(board != 0) and winner == 0:
		# winner = -1
	# return(winner)
	
def evaluate(board): 
	winner = 0
	
	for player in [1, 2]: 
		if (row_win(board, player) or
			col_win(board,player) or
			diag_win(board,player)): 
				
			winner = player 
			
	if np.all(board != 0) and winner == 0: 
		winner = -1
	return winner 


#Let`s start the game

# def start_game():
	# board, winner, counter = create_board(), 0, 1
	# print(board)
	# sleep(2)
	
	# while winner == 0:
		# for player in [1, 2]:
			# board = random_place(board, player)
			# print('Board after: ' + str(counter) + 'move')
			# print(board)
			# sleep(2)
			# counter += 1
			# winner = check_a_winner(board)
			# if winner != 0:
				# break
	# return(winner)
		
# print('Winner is' +str(start_game))

def play_game(): 
	board, winner, counter = create_board(), 0, 1
	print(board) 
	sleep(2) 
	
	while winner == 0: 
		for player in [1, 2]: 
			board = random_place(board, player) 
			print("Board after " + str(counter) + " move") 
			print(board) 
			sleep(2) 
			counter += 1
			winner = evaluate(board) 
			if winner != 0: 
				break
	return(winner) 

# Driver Code 
print("Winner is: " + str(play_game())) 
