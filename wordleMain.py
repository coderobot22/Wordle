import random
wordFound = False
validWord = False
noGuesses = 0
maxGuesses = 6
wordArray = []
randomNum = random.randint(0,1379)
resWords = []


f = open("wordList.txt")
lines = f.readlines()
word = lines[randomNum].strip()
print(word)



for i in range(5):
     wordArray.append(word[i])

while wordFound==False and noGuesses!=maxGuesses:
        
       guess = input("Enter Guess: ")

       

       if(guess==word):
                noGuesses+=1
                for i in range(5):
                       print("🟩")
                print("Congratulations! You took " + str(noGuesses) + " guesses to get the word!")
       else:
                print("no")
                noGuesses+=1
                #convert word to array
                #use count and index array features
                for i in range(5):
                       char = guess[i]
                       #print(char)
                       numberInWord = word.count(guess[i])
                       numberInGuess = guess.count(guess[i])
                       #print(numberInWord,numberInGuess)
                       numberSpare = numberInGuess-numberInWord
                       if(numberInWord == 1 and numberInGuess == 2 or numberInGuess == 3):
                              resWords.append(char)
                       #3 conditions
                       #green if in right position
                       #yellow if in word but not in position
                       #grey if not in word
                       if(guess[i] == wordArray[i]):
                              #green
                              print("🟩")
                       elif(guess[i] != wordArray[i] and word.count(guess[i]) > 0 and resWords.count(guess[i]) == 0 ):
                              print("🟨")
                       else:
                               print("⬛️")
                print("That was guess number " + str(noGuesses))
print("Unlucky, the word was " + word)                
                              
