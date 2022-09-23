from colorama import Fore
from tictactoe import TicTacToe
from Board import Board
import random

initialBoard = Board()
print("The initial state of board is as follow- ")
initialBoard.printBoard()
print("\t1) Tiles numbered in color white are empty spaces.")
print("\t2) Tiles numbered in color green are filled by user.")
print("\t3) And the Tiles numbered in red are filled by the computer(AI).")

game = TicTacToe(initialBoard)
state = random.randrange(0, 2)
while(True):
    if state:
        game.startUserMove()
        game.startComputerMove()
    else:
        game.startComputerMove()
        game.startUserMove()