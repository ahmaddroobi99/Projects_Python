import random


def guess (x):
    random_number =random.randint(1,x)
    print(random_number)
    guess =0
    while  guess !=random_number :
        guess =int(input(f'Guess numper betwwen 1 and {x}::'))
        if guess <random_number :
            print("Sory, guess agin .Too low")

        elif guess> random_number:
            print("Sorry ,guess..Too hight")

    print(f"yah,Congratulation. you have guessded the number..{random_number} ")

def computer_guess (x):
    low =1
    high =x
    feedback=''
    while feedback != 'c'  :
        if low!=high :
            guess = random.randint(low, high)

        else :
            guess=low

        feedback = input(f'is {guess} too high (h) ,Too low ,orr correct (c)').lower()
        if feedback == 'h':
            high =guess -1
        elif feedback =="l":
            low =guess+1
    print(f"yah ,the Computer guessed your number ,{guess},correctly")

# guess(50)

computer_guess(500)