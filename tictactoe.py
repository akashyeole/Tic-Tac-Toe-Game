from cmath import inf
from colorama import Fore
from Board import Board
import copy

class TicTacToe():
    currSetup = None
    userSymbol = Fore.GREEN + "X" + Fore.RESET
    botSymbol = Fore.RED + "O" + Fore.RESET
    scoreTableForMinMax = {userSymbol: -1, botSymbol: 1, "Tie": 0}
    
    def __init__(self, initialBoard):
        self.currSetup = initialBoard

    def startUserMove(self):
        while(True):
            try:
                userSelectedTile = int(input(("\nYOUR MOVE, enter Tile No. to place '" + self.userSymbol + "': ")))-1
            except:
                print("\nEnter only integer that represents empty tile!")
                continue
            if self.currSetup.isSafe(userSelectedTile):
                self.currSetup.board[(userSelectedTile//3)][(userSelectedTile%3)] = self.userSymbol
                print("Board state after your move: ")
                self.currSetup.printBoard()
                break
            else:
                print("Invalid play, please Try Again!")
        
        self.currSetup.checkWinner()
        if self.currSetup.winner != None:
            self.endGame()
        return
        
    def minmax(self, setup, isCompMove):
        setup.checkWinner(isUsingMinMax = True)
        if setup.winner != None:
            return self.scoreTableForMinMax[setup.winner]

        if isCompMove:
            bestPossibility = float(-inf)
            for row in range(3):
                for col in range(3):
                    if setup.isSafe(((row*3)+col%3)):
                        setup.board[row][col] = self.botSymbol
                        possibility = self.minmax(setup, False)
                        bestPossibility = max(possibility, bestPossibility)
                        setup.board[row][col] = ((row*3)+col%3)+1
            return bestPossibility
        else:
            bestPossibility = float(inf)
            for row in range(3):
                for col in range(3):
                    if setup.isSafe(((row*3)+col%3)):
                        setup.board[row][col] = self.userSymbol
                        possibility = self.minmax(setup, True)
                        bestPossibility = min(possibility, bestPossibility)
                        setup.board[row][col] = ((row*3)+col%3)+1
            return bestPossibility

    def startComputerMove(self):
        print("\nWait! '" + self.botSymbol + "' Computer is playing.......")
        bestPossibility = float(-inf)
        tempBoard= None
        for row in range(3):
            for col in range(3):
                if self.currSetup.isSafe(((row*3)+col%3)):
                    self.currSetup.board[row][col] = self.botSymbol
                    possibility = self.minmax(self.currSetup, False) 
                    if possibility > bestPossibility:
                        bestPossibility = possibility
                        tempBoard = copy.deepcopy(self.currSetup)
                    self.currSetup.board[row][col] = ((row*3)+col%3)+1
        self.currSetup = tempBoard
        print("Board state after computer's move: ")
        self.currSetup.printBoard()
        self.currSetup.checkWinner()
        if self.currSetup.winner != None:
            self.endGame()
        return

    def endGame(self):
        print("\n")
        if self.currSetup.winner == self.userSymbol:
            print(Fore.GREEN + "\tYou 'X' won! Game ended." + Fore.RESET)
        elif self.currSetup.winner == self.botSymbol:
            print(Fore.RED + "\tComputer 'O' won! Better Luck Next Time." + Fore.RESET)
        else:
            print(Fore.YELLOW + "\tTie, Nobody won!" + Fore.RESET)
        self.currSetup.printBoard()
        exit()