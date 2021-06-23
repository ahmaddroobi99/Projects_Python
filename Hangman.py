import random
from words import words
import string


def get_valid_word(words):
    word =random.choice (words)
    while '-'in word or ' 'in word :
        word =random.choice(words )

    return word

def hangman ():



    word =get_valid_word(words)
    print (word)
    word_letters= set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters =set ()



    while len(word_letters)>0 :

        print("You have used these letters  ::", ' '.join(used_letters))


        word_list = [  letter if letter in used_letters else '-' for letter in word]
        print('current word', ' '.join(word_list))

        user_letter = input("Guess a letter :").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

        elif user_letter in used_letters:
            print("you have alrwady used that character . plz try a gain ")


        else:
            print("invalid character..plz try a gain ")


# user_input =input('Type something')
# print(user_input)

hangman()