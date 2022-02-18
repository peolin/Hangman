import string
# Checking if the letter is in the word
def check(answer, hiddenword, letter):
    counter = 0
    letter_position = 0
    for answ_l in str(answer):
        if letter == answ_l: # If there is such letter - change * to it
            tempstr = list(hiddenword) # Temporary string = list
            tempstr[letter_position] = letter # Changing * to letter
            hiddenword = "".join(tempstr) # Rewritting string
            counter +=1
        letter_position +=1
    return hiddenword, counter

def check_alphabet(letter, alphabet):
    for l in alphabet:
        if l == letter: alphabet = alphabet.replace(l+' ','')
    return alphabet