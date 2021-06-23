import random



def play():
    user =input(f" whats you choice ? 'r' for rock ,'p' for paprt , 's' sessiors\n ")
    computer =random.choice(['r','p','s'])
    print(computer)


    if user == computer:
        return ' it\'s tie'

    if is_win(user,computer):
        return "You Won !!"
    return "You Loose000"

def is_win (player, opponent):
    if (player =='r' and opponent =='s')or(player=='s'and opponent=='p')or(player=='p'and opponent=='r'):
        return True
    else:
        return False


print (play())
