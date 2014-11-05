board = []
board.append("  ___")
board.append("  | |")
board.append("    |")
board.append("    |")
board.append("    |")
board.append("-----")

answerWord = "Jesus"
clueWord = ""
for x in range(len(answerWord)):
	clueWord += "_ "

def printBoard(board):
	for row in board:
		print " ".join(row)

def main():
	printBoard(board)
	print "The word is " + str(len(answerWord)) + " letters long"
	print clueWord

if __name__== "__main__":
	main()