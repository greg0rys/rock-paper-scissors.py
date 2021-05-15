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
    # declare the accumulators outside of the while loop
    # this way they don't keep resetting to 0 inside the loop
    # these hold the game stats
    userWins = 0
    computerWins = 0
    gamesPlayed = 0
    ties = 0
    while again:
        user = userChoice()
        computer = compChoice()
        if user == computer:
            print('It\'s a tie!')
            userWins = userWins
            computerWins = computerWins
            ties += 1
        elif user == 'rock' and computer == 'paper':
            print('You lose!', computer,'covers',user)
            computerWins = computerWins + 1
            userWins = userWins
        elif user == 'rock' and computer == 'scissors':
            print('You win!', user,'smashes',computer)
            userWins = userWins + 1
            computerWins = computerWins
        elif user == 'paper' and computer == 'rock':
            print('You win', user,'covers',computer)
            userWins = userWins + 1
            computerWins = computerWins
        elif user == 'paper' and computer == 'scissors':
            print('You lost!', computer,'slices',user)
            computerWins = computerWins + 1
            userWins = userWins
        elif user == 'scissors' and computer == 'rock':
            print('You lost!',computer,'smashes',user)
            computerWins = computerWins + 1
            userWins = userWins
        elif user =='scissors' and computer == 'paper':
            print('You won!', user, 'slices', computer)
            userWins = userWins + 1
            computerWins = computerWins
        gamesPlayed += 1
        again = input('Go again? y/n: ')
        again = again.lower()
        # if the user enters anything but y exit the loop
        if again != 'y':
            break
    # print the games stats:
    print('Thanks for playing!')
    print('----GAME STATS----')
    print('you played:',gamesPlayed,'games')
    print('you won:', userWins,'games')
    print('the computer won:',computerWins,'games')
    print('you tied:', ties,'times')
    print('------------------')

main()

