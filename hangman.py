import string
from art import tprint
from words import words_easy, words_normal, words_hard, words_extreme
from checkup import check, check_alphabet
from gallows import gallows_type
import random
from simple_term_menu import TerminalMenu

tprint("HANGMAN","rnd-medium")

# Terminal menu to choose mode (word)
options = ['Easy', 'Normal', 'Hard', 'Extreme']
menu = TerminalMenu(options, title = "Choose a game mode:")
menu_entry_index = menu.show()
print("You have selected "+options[menu_entry_index]+" mode!")


# Start EASY
if menu_entry_index == 0:
    while True:
        alphabet = "a b c d e f g h i j k l m n o p q r s t u x y z"
        answer = random.choice(words_easy)
        lives = 7
        hiddenword = ''
        for l in answer:
            if (ord(l) == 32 or ord(l) == 45): hiddenword += l
            else: hiddenword += '*'
        print("Word is", hiddenword, "and you have",lives,"lives!")

        # 1st try
        tprint("START","rnd-small")
        print("Word:",hiddenword,'\n'+"Lives:",lives,'\n'+"Tries:")
        gallows_type(lives)
            #print("a b c d e f g h i j k l m n o p q r s t u x y z") ALPHABET

        for alphabet_letter in string.ascii_lowercase:
            print(alphabet_letter, end =" ")

        letter = str(input('\n'+"Please, choose a letter: "))
        if (ord(letter)==32 or len(letter)>1):
            letter = str(input('\n'+"Please, enter only one letter: "))


        # Checking if the letter is in the word
        hiddenword = check(answer,hiddenword,letter)[0]
        counter = check(answer,hiddenword,letter)[1]
        # If there is no such letter- -1 life
        if counter == 0:
            lives -=1
        else: counter = 0

        alphabet = check_alphabet(letter, alphabet) # Remove used letter

        # Next
        while  (hiddenword != answer and lives>0):        
            # Results to next try
            print("Word:",hiddenword,'\n'+"Lives:",lives)
            gallows_type(lives) # Print a gallow to lives left
            print(alphabet)

            letter = str(input('\n'+"Please, choose a letter: "))
            if (ord(letter)==32 or len(letter)>1):
                letter = str(input('\n'+"Please, enter only one letter: "))

            print('\n')
            # Checking if the letter is in the word
            hiddenword = check(answer,hiddenword,letter)[0]
            counter = check(answer,hiddenword,letter)[1]

            # If there is no such letter- -1 life
            if counter == 0:
                lives -=1
            else: counter = 0
            alphabet = check_alphabet(letter, alphabet) # Remove used letters

        if lives == 0:
            gallows_type(lives)
            print("Sorry, you have lost.")
        elif hiddenword==answer:
            print("The answer is",answer+'!')
            print("Congratulations, you have won!")

        # Restart
        res = input("Want to play again? y/n ")
        if res == 'y':
            continue
        else:
            print("Goodbye!")
            break

# Start NORMAL
elif menu_entry_index == 1:
    while True:
        alphabet = "a b c d e f g h i j k l m n o p q r s t u x y z"
        answer = random.choice(words_normal)
        lives = 7
        hiddenword = ''
        for l in answer:
            if (ord(l) == 32 or ord(l) == 45): hiddenword += l
            else: hiddenword += '*'
        print("Word is", hiddenword, "and you have",lives,"lives!")

        # 1st try
        tprint("START","rnd-small")
        print("Word:",hiddenword,'\n'+"Lives:",lives)
        gallows_type(lives)
            #print("a b c d e f g h i j k l m n o p q r s t u x y z") ALPHABET

        for alphabet_letter in string.ascii_lowercase:
            print(alphabet_letter, end =" ")

        letter = str(input('\n'+"Please, choose a letter: "))
        if (ord(letter)==32 or len(letter)>1):
            letter = str(input('\n'+"Please, enter only one letter: "))

        # Checking if the letter is in the word
        hiddenword = check(answer,hiddenword,letter)[0]
        counter = check(answer,hiddenword,letter)[1]

        # If there is no such letter- -1 life
        if counter == 0:
            lives -=1
        else: counter = 0

        alphabet = check_alphabet(letter, alphabet) # Remove used letter

        # Later
        while (hiddenword != answer and lives>0):        
            # Results to next try
            print("Word:",hiddenword,'\n'+"Lives:",lives,'\n'+"Tries:")
            gallows_type(lives) # Print a gallow to left
            print(alphabet)
            
            letter = str(input('\n'+"Please, choose a letter: "))
            if (ord(letter)==32 or len(letter)>1):
                letter = str(input('\n'+"Please, enter only one letter: "))

            # Checking if the letter is in the word
            hiddenword = check(answer,hiddenword,letter)[0]
            counter = check(answer,hiddenword,letter)[1]

            # If there is no such letter- -1 life
            if counter == 0:
                lives -=1
            else: counter = 0
            alphabet = check_alphabet(letter, alphabet) # Remove used letters

        if  lives == 0:
            gallows_type(lives)
            print("Sorry, you have lost.")
        elif hiddenword==answer:
            print("The answer is",answer+'!')
            print("Congratulations, you have won!")

        res = input("Want to play again? y/n ")
        if res == 'y':
            continue
        else:
            print("Goodbye!")
            break

# Start HARD
elif menu_entry_index == 2:
    while True:
        alphabet = "a b c d e f g h i j k l m n o p q r s t u x y z"
        answer = random.choice(words_hard)
        lives = 7
        hiddenword = ''
        for l in answer:
            if (ord(l) == 32 or ord(l) == 45): hiddenword += l
            else: hiddenword += '*'
        print("Word is", hiddenword, "and you have",lives,"lives!")

        # 1st try
        tprint("START","rnd-small")
        print("Word:",hiddenword,'\n'+"Lives:",lives,'\n'+"Tries:")
        gallows_type(lives)
            #print("a b c d e f g h i j k l m n o p q r s t u x y z") ALPHABET

        for alphabet_letter in string.ascii_lowercase:
            print(alphabet_letter, end =" ")

        letter = str(input('\n'+"Please, choose a letter: "))
        if (ord(letter)==32 or len(letter)>1):
            letter = str(input('\n'+"Please, enter only one letter: "))

        # Checking if the letter is in the word
        hiddenword = check(answer,hiddenword,letter)[0]
        counter = check(answer,hiddenword,letter)[1]

        # If there is no such letter- -1 life
        if counter == 0:
            lives -=1
        else: counter = 0

        alphabet = check_alphabet(letter, alphabet) # Remove used letter

        # Later
        while (hiddenword != answer and lives>0):        
            # Results to next try
            print("Word:",hiddenword,'\n',"Lives:",lives,'\n',"Tries:")
            gallows_type(lives) # Print a gallow to left
            print(alphabet)
            
            letter = str(input('\n'+"Please, choose a letter: "))
            if (ord(letter)==32 or len(letter)>1):
                letter = str(input('\n'+"Please, enter only one letter: "))

            # Checking if the letter is in the word
            hiddenword = check(answer,hiddenword,letter)[0]
            counter = check(answer,hiddenword,letter)[1]

            # If there is no such letter- -1 life
            if counter == 0:
                lives -=1
            else: counter = 0
            alphabet = check_alphabet(letter, alphabet) # Remove used letters
        
        if lives == 0:
            gallows_type(lives)
            print("Sorry, you have lost.")
        elif hiddenword==answer:
            print("The answer is",answer+'!')
            print("Congratulations, you have won!")

        res = input("Want to play again? y/n ")
        if res == 'y':
            continue
        else:
            print("Goodbye!")
            break

# Start EXTREME
elif menu_entry_index == 3:
    while True:
        alphabet = "a b c d e f g h i j k l m n o p q r s t u x y z"
        answer = random.choice(words_hard)
        lives = 7
        hiddenword = ''
        for l in answer:
            if (ord(l) == 32 or ord(l) == 45): hiddenword += l
            else: hiddenword += '*'
        print("Word is", hiddenword, "and you have",lives,"lives!")

        # 1st try
        tprint("START","rnd-small")
        print("Word:",hiddenword,'\n'+"Lives:",lives,'\n'+"Tries:")
        gallows_type(lives)
            #print("a b c d e f g h i j k l m n o p q r s t u x y z") ALPHABET

        for alphabet_letter in string.ascii_lowercase:
            print(alphabet_letter, end =" ")

        letter = str(input('\n'+"Please, choose a letter: "))
        if (len(letter)>1 or ord(letter)==32):
            letter = str(input('\n'+"Please, enter only one letter: "))

        # Checking if the letter is in the word
        hiddenword = check(answer,hiddenword,letter)[0]
        counter = check(answer,hiddenword,letter)[1]

        # If there is no such letter- -1 life
        if counter == 0:
            lives -=1
        else: counter = 0

        alphabet = check_alphabet(letter, alphabet) # Remove used letter

        # Later
        while (hiddenword != answer and lives>0):        
            # Results to next try
            print("Word:",hiddenword,'\n'+"Lives:",lives,'\n'+"Tries:")
            gallows_type(lives) # Print a gallow to left
            print(alphabet)
            
            letter = str(input('\n'+"Please, choose a letter: "))
            if (ord(letter)==32 or len(letter)>1):
                letter = str(input('\n'+"Please, enter only one letter: "))
            else:
                print()
            # Checking if the letter is in the word
            hiddenword = check(answer,hiddenword,letter)[0]
            counter = check(answer,hiddenword,letter)[1]

            # If there is no such letter- -1 life
            if counter == 0:
                lives -=1
            else: counter = 0
            alphabet = check_alphabet(letter, alphabet) # Remove used letters

        if  lives == 0:
            gallows_type(lives)
            print("Sorry, you have lost.")
        elif hiddenword==answer:
            print("The answer is",answer+'!')
            print("Congratulations, you have won!")

        res = input("Want to play again? y/n ")
        if res == 'y':
            continue
        else:
            print("Goodbye!")
            break
else: 
    print("Congratulations, you've broke the game!")