import random,sys,hang_man
from playsound import *
# give word at the end if guessed wrong
# change wording around number of guesses
words_long = ['supercalifragilisticexpialidocious','hippopotomonstrosesquipedaliophobia','antidisestablishmentarianism','pneumonoultramicroscopicsilicovolcanoconiosis','foccinaucinihilipilification','chargoggagoggmanchauggauggagoggchaubunagungamaugg','taumatawhakatangihangakoauauotamateaturipukakapikimaungahoronukupokaiwhenuakitanatahu','pseudopseudohypoparathyroidism','pseudohypoparathyroidism','methylenedioxymethamphetamine','electroencephalographically',]
words_hard = ['inhabitant','occupation','constraint','definition','brainstorm','vegetarian','convention','pedestrian','relinquish','brilliance']
words_mid = ['pattern','mixture','trivial','confuse','percent','citizen','perform','illness','session','distort']
words_easy = ['brag','arm','chase','occupy','ego','lay','drag','coffee','denial','moment','pizza']


guessed_letters = ""
not_in_randword_guess = ""
#guess a letter code
def guess_a_letter(guess, randword):
    len_of_guess = len(guess)
    if len_of_guess > 1 or len_of_guess < 1:
        print('not one letter letter')
    else:
        if guess in randword:
            return True
        else:
            return False
#letter display code
def letter_display(randword,guessed_letters,guess):
    for guess in randword:
        if guess in guessed_letters:
            print(" {} ".format(guess), end="")
        else:
            print(" _ ", end="")
    print("\n")
guessed_letters = ""
#checking to see if different letters code
def different_letters(randword):
    return "" .join(set(randword))
#letter guessing code the most important part of the program
def letter_guessing_code(guessed_letters,guesses,randword,total_attemts,not_in_randword_guess,difficulty):
    while guesses > 1 and len(guessed_letters) < len(different_letters(randword)):    
        guess = input('Guess a letter: ')
        if guess in guessed_letters or guess in not_in_randword_guess:
            print("letter has already been guessed")
            print(hang_man.hang_man_guy(guesses,total_attemts))
            letter_display(randword,guessed_letters,guess)
        elif guess in randword and len(guess) == 1: 
            guessed_letters += guess
            print(hang_man.hang_man_guy(guesses,total_attemts))
            letter_display(randword,guessed_letters,guess)

        elif len(guess) != 1:
            print("not one letter")
        elif guess not in randword and guess not in guessed_letters and guess not in not_in_randword_guess:
            print("no that letter is not in the word")
            guesses -= 1
            print(hang_man.hang_man_guy(guesses,total_attemts))
            letter_display(randword,guessed_letters,guess)
            not_in_randword_guess += guess
            guessesstr = str(guesses)
            print("guesses left "+ guessesstr)
            
    guessesstr = str((guesses-1))
    if len(guessed_letters) == len(different_letters(randword)):
        playsound('cheering.wav')
        print("congrates "+ name + " you have beat "+ difficulty + " mode \n You have " + guessesstr +" wrong guessses left")
    elif guesses == 1: #len(guessed_letters) <  len(different_letters(randword)) or len(guessed_letters) > len(different_letters(randword)) and :
        print("You Have lost")
        print("the word was " + randword)
#main part of running the code
def code(guessed_letters, total_guesses,randword,total_attemts,not_in_randword_guess,difficulty):
    guessed_letters = ""  
    guesses = total_guesses
    guess = str((guesses-1))
    langth = len(randword)
    letter_space = "_ " * langth
    length = str(langth)
    print(hang_man.hang_man_guy(guesses,total_attemts))
    print(letter_space +" "+ length + " letters and "+ guess + " wrong guesses")
    letter_guessing_code(guessed_letters,guesses,randword,total_attemts,not_in_randword_guess,difficulty)
#part that repeats asks your name or runs def code 
while True:
    Repeat = 0
    while True:
            
        while True:    
            try:    
                name = str(input("what is your name?:  "))
                break
            except ValueError:
                print("Not A Name")
                continue
        print("Hello "+ name +" Would you like to play a game?")
        print("To continue type 1 to stop type 2 ")   
        while True:
            try:
                Repeat = int(input('Enter Number 1 or 2: '))
                if Repeat == 1 or Repeat == 2:
                    break
                else:
                    print("Not 1 or 2")
            except ValueError:
                print("Not A Valid Number")

        if Repeat == 1:
            break 
        elif Repeat == 2:
            sys.exit()
            
            
    while True:
        if Repeat == 3:
            break
        while True:
            try:
                Difficulty = int(input('Enter Number \n 1 for easy \n 2 for medium \n 3 for hard \n and 4 for long words: '))
                if Difficulty == 1 or 2 or 3 or 4:
                    break
                else:
                    print("Not 1, 2, 3 or 4")
                    continue
            except ValueError:
                print("Not A Valid Number")
                continue

        if Difficulty == 1:
            randword = random.choice(words_easy)
            print("Easy Picked")
            if name == 'red cardinal':
                while True:
                    try:    
                        devcode = str(input("What is the Code:  "))
                        if devcode == 'opensesame':
                            print(randword)
                        else:
                            print('not the code')
                        break
                    except ValueError:
                        continue
            code(guessed_letters,7,randword,7,not_in_randword_guess,'Easy')
        elif Difficulty == 2:
            randword = random.choice(words_mid)
            if name == 'red cardinal':
                while True:
                    try:    
                        devcode = str(input("What is the Code:  "))
                        if devcode == 'opensesame':
                            print(randword)
                        else:
                            print('not the code')
                        break
                    except ValueError:
                        continue
            print("Medium Picked")
            code(guessed_letters,6,randword,6,not_in_randword_guess,'Medium')
        elif Difficulty == 3:
            randword = random.choice(words_hard)
            if name == 'red cardinal':
                while True:
                    try:    
                        devcode = str(input("What is the Code:  "))
                        if devcode == 'opensesame':
                            print(randword)
                        else:
                            print('not the code')
                        break
                    except ValueError:
                        continue
            print("HARD PICKED")
            code(guessed_letters,5,randword,5,not_in_randword_guess,'HARD')
        elif Difficulty == 4:
            randword = random.choice(words_long)
            if name == 'red cardinal':
                while True:
                    try:    
                        devcode = str(input("What is the Code:  "))
                        if devcode == 'opensesame':
                            print(randword)
                        else:
                            print('not the code')
                        break
                    except ValueError:
                        continue
            print("LONG PICKED")
            code(guessed_letters,5,randword,5,not_in_randword_guess,'LONG')
        print(name +" Would You Like To Play Again? Type 1 To Continue or 2 to Stop")
        while True:
            try:
                Repeat = int(input('Enter Number 1 or 2 or type 3 to go back to start: '))
                if Repeat == 1 or Repeat == 2 or Repeat == 3:
                    break
                else:
                    print("Not 1 or 2 or 3")
            except ValueError:
                print("Not A Valid Number")
                continue
        while True:
            if Repeat == 1 or 3:
                break
            elif Repeat == 2:
                sys.exit()
                   

            
        