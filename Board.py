from colorama import Fore, Back

class Board():
	board = None
	userSymbol = Fore.GREEN + "X" + Fore.RESET
	botSymbol = Fore.RED + "O" + Fore.RESET
	winner = None

	def __init__(self, brd = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]):
		self.board = brd

	def printBoard(self):
		print("\t -------------")
		for row in self.board:
			print("\t", *row, "", sep = " | ")
			print("\t -------------")
			
	def isSafe(self, tile):
		if self.board[(tile//3)][(tile%3)] == self.botSymbol or self.board[(tile//3)][(tile%3)] == self.userSymbol:
			return False
		return True

	def isTie(self):
		for row in range(3):
			for col in range(3):
				if self.board[row][col] in range(1,10):
					return False
		return True

	def checkWinner(self, isUsingMinMax = False):
		winner = None
		if self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2]:
			winner = self.board[0][0]
			if not isUsingMinMax:
				self.board[0][0] = Back.BLUE + self.board[0][0] + Back.RESET
				self.board[1][1] = Back.BLUE + self.board[1][1] + Back.RESET
				self.board[2][2] = Back.BLUE + self.board[2][2] + Back.RESET

		elif self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0]:
			winner = self.board[0][2]
			if not isUsingMinMax:
				self.board[0][2] = Back.BLUE + self.board[0][2] + Back.RESET
				self.board[1][1] = Back.BLUE + self.board[1][1] + Back.RESET
				self.board[2][0] = Back.BLUE + self.board[2][0] + Back.RESET

		elif self.board[0][0] == self.board[0][1] and self.board[0][1] == self.board[0][2]:
			winner = self.board[0][0]
			if not isUsingMinMax:
				self.board[0][0] = Back.BLUE + self.board[0][0] + Back.RESET
				self.board[0][1] = Back.BLUE + self.board[0][1] + Back.RESET
				self.board[0][2] = Back.BLUE + self.board[0][2] + Back.RESET

		elif self.board[1][0] == self.board[1][1] and self.board[1][1] == self.board[1][2]:
			winner = self.board[1][0]
			if not isUsingMinMax:
				self.board[1][0] = Back.BLUE + self.board[1][0] + Back.RESET
				self.board[1][1] = Back.BLUE + self.board[1][1] + Back.RESET
				self.board[1][2] = Back.BLUE + self.board[1][2] + Back.RESET

		elif self.board[2][0] == self.board[2][1] and self.board[2][1] == self.board[2][2]:
			winner = self.board[2][0]
			if not isUsingMinMax:
				self.board[2][0] = Back.BLUE + self.board[2][0] + Back.RESET
				self.board[2][1] = Back.BLUE + self.board[2][1] + Back.RESET
				self.board[2][2] = Back.BLUE + self.board[2][2] + Back.RESET

		elif self.board[0][0] == self.board[1][0] and self.board[1][0] == self.board[2][0]:
			winner = self.board[0][0]
			if not isUsingMinMax:
				self.board[0][0] = Back.BLUE + self.board[0][0] + Back.RESET
				self.board[1][0] = Back.BLUE + self.board[1][0] + Back.RESET
				self.board[2][0] = Back.BLUE + self.board[2][0] + Back.RESET

		elif self.board[0][1] == self.board[1][1] and self.board[1][1] == self.board[2][1]:
			winner = self.board[0][1]
			if not isUsingMinMax:
				self.board[0][1] = Back.BLUE + self.board[0][1] + Back.RESET
				self.board[1][1] = Back.BLUE + self.board[1][1] + Back.RESET
				self.board[2][1] = Back.BLUE + self.board[2][1] + Back.RESET

		elif self.board[0][2] == self.board[1][2] and self.board[1][2] == self.board[2][2]:
			winner = self.board[0][2]
			if not isUsingMinMax:
				self.board[0][2] = Back.BLUE + self.board[0][2] + Back.RESET
				self.board[1][2] = Back.BLUE + self.board[1][2] + Back.RESET
				self.board[2][2] = Back.BLUE + self.board[2][2] + Back.RESET
		if winner == None:
			if self.isTie():
				self.winner = "Tie"
			else:
				self.winner = winner
		else:
			self.winner = winner