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
if time < 3:
  print(GuessList)
misses = 0
guess = input("Guess a letter: ")
lol = input("How many misses do you want for this game?")
letter = "p", "o", "n", "y", "o"
guess = (wordlist[0])
wordlist = list(guess)
index = 0
for l in guess:
  if l == letter:
    print(count)
    count += 1
print(GuessList)
for letter in wordlist:
	if letter == guess:
		GuessList[index] = guess
	index += 1
print(GuessList)
while misses < "lol":
  print("YOU WON THE GAME!")
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