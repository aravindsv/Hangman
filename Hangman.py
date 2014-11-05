board = []
board.append("  ___")
board.append("  | |")
board.append("    |")
board.append("    |")
board.append("    |")
board.append("-----")

answerWord = "Jesus"
clueWord = []
guessedLetters = []
for x in range(len(answerWord)):
	clueWord.append("_ ")

def printBoard(board):
	for row in board:
		print "".join(row)

def printClueWord(clue):
	result = ""
	for letter in clue:
		result += letter
	print result

def hangTheMan(board, lives):
	#TODO:Draw the hungMan parts
	pass

def main():
	lives = 6
	while lives > 0 and clueWord.count("_ ") > 0:
		printBoard(board)
		print "The word is " + str(len(answerWord)) + " letters long"
		printClueWord(clueWord)
		userGuess = raw_input("Guess a letter: ")

		#If user doesn't guess any letter
		if not userGuess:
			print "You must guess a letter"

		#If user tries to guess more than a single character
		elif len(userGuess) > 1:
			print "You may only guess one letter at a time!"

		#If user guesses a letter they already guessed
		elif userGuess in guessedLetters:
			print "You already guessed that letter!"

		#If user guesses an incorrect letter
		elif answerWord.lower().find(userGuess.lower()) == -1:
			print "Nope\n"
			hangTheMan(board, lives)
			lives -= 1

		#If user guesses a correct letter
		else:
			print "Yup\n"
			for index, letter in enumerate(answerWord):
				if letter.lower() == userGuess.lower():
					clueWord[index] = str(letter)

		#Add guess to guessedLetters
		guessedLetters.append(userGuess)

	if lives == 0:
		print "Game Over!\nThe word was \"" + answerWord + "\""
	else:
		print "Congratulations! You won!"
			

if __name__== "__main__":
	main()