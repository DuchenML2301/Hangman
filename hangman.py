import turtle
import time

wordlist= "ponyo"
GuessList = []
wordlist = list("ponyo")
count = 0
GuessList = list("_____")
wordlist = list(wordlist)
GuessList = []
print(GuessList)
GuessList[0] = "p"
print(GuessList)
GuessList[1] = "o"
print(GuessList)
GuessList[2] = "n"
print(GuessList)
GuessList[3] = "y"
print(GuessList)
GuessList[4] = "o"
print(GuessList)
for l in guess:
  if l == letter:
    print(count)
    count += 1
print(GuessList)
  
hangmanList = [''' 
 
     +---+
     0   |
         |
         |
         === ''', ''' 
 
     +---+
     0   |
         |
         |
         === ''', '''
      +---+
      0   |
      |   |
          |
          === ''', '''
      +---+
      0   |
      |   |
       \  |
          === ''', '''
      +---+ 
      0   |
      |   |
     / \  |
           === ''', '''
      +---+ 
      0   |
      |\  |
     / \  |
         === ''', '''
      +---+
      0   |
     /|\  |
     / \  |
         === ''' ]
misses = 0
guess = input("Guess a letter: ")
guess = (wordlist[0])
wordlist = list(guess)
index = 0
for letter in wordlist:
	if letter == guess:
		GuessList[index] = guess
	index += 1
print(GuessList)
while misses < 7:
	if guess in wordlist:
		#looop through secret word and change my guesss list at the correct lndexs
		print("letter is in the word")
else:
  misses += 1
  print("letter is NOT in the word")
  print(hangmanList[misses])
  print(GuessList)
print("GAME OVER")
for p in wordlist:
	GuessList.append("_")
	print(GuessList)
print("GAME OVER")