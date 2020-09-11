hand = ['ROCK', 'PAPER', 'SCISSORS']

def RoPaSc(playerOneInput, playerTwoInput):
    if (playerTwoInput == playerOneInput):
        choise = input('Its a tie! Play again? (y/n) \n  >')
        playAgain(choise)
    elif(playerOneInput == 'ROCK'):
        if(playerTwoInput == 'SCISSOR'):
            playerWin(1)
        else:
            playerWin(2)
    elif(playerOneInput == 'PAPER'):
        if(playerTwoInput == 'ROCK'):
            playerWin(1)
        else:
            playerWin(2)
    elif(playerOneInput == 'SCISSORS'):
        if(playerTwoInput == 'ROCK'):
            playerWin(2)
        else:
            playerWin(1)
        
def playerWin(player):
    print('Player ' + str(player) + ' wins!')
    playAgain()

def getPlayerInput(player):
    playerInput = input(player + ': Rock, papers or scissors? type q to quit \n  > ').upper()
    if (not checkInput(playerInput)):
        print('* ' + playerInput + ' *' + ' is not a valid input... Try again!')
        getPlayerInput(player)
    return playerInput
    
def checkInput(playerInput):
    if playerInput == 'Q':
        exit()
    return playerInput in hand

def playAgain(choise = None):
    if choise is None:
        choise = input('Play again? (y/n) \n  >')
    if choise == 'y':
        playerOneInput = getPlayerInput('Player 1')
        playerTwoInput = getPlayerInput('Player 2')
        RoPaSc(playerOneInput, playerTwoInput)
    elif choise == 'n':
        exit()
    else:
        playAgain(input('Invalid input!'))
    

if __name__ == "__main__":
    playerOneInput = getPlayerInput('Player 1')
    playerTwoInput = getPlayerInput('Player 2')
    RoPaSc(playerOneInput, playerTwoInput)