import random
choices = ['rock','paper','scissors']
# let the computer choose
def compChoice():
    cChoice = random.randint(1,3)
    if cChoice == 1:
        cChoice = 'rock'
    elif cChoice == 2:
        cChoice = 'paper'
    else:
        cChoice = 'scissors'
    return cChoice

# get the users choice
def userChoice():
    userC = 1
    while userC:
        try:
            userC = input('Please enter your choice! rock,paper,or scissors: ')
            userC = userC.lower()
            if userC not in choices:
                raise ValueError
        except ValueError:
            print('I did not understand your entry')
            print('Please choose', choices)
        else:
            break
        userC = userC.lower()
    return userC


def main():
    again = 'y'
    while again:
        user = userChoice()
        computer = compChoice()
        if user == computer:
            print('It\'s a tie!')
        elif user == 'rock' and computer == 'paper':
            print('You lose!', computer,'covers',user)
        elif user == 'rock' and computer == 'scissors':
            print('You win!', user,'smashes',computer)
        elif user == 'paper' and computer == 'rock':
            print('You win', user,'covers',computer)
        elif user == 'paper' and computer == 'scissors':
            print('You lost!', computer,'slices',user)
        elif user == 'scissors' and computer == 'rock':
            print('You lost!',computer,'smashes',user)
        elif user =='scissors' and computer == 'paper':
            print('You won!', user, 'slices', computer)
        again = input('Go again? y/n')
        again = again.lower()
        if again == 'n':
            break

main()

