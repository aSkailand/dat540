hand = ['ROCK', 'PAPER', 'SCISSORS']


def RoPaSc(playerOneInput, playerTwoInput) -> None:
    '''
        Figure outs which player wins based on the two input parameters given.
    '''
    # Tie
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
    '''
        Prints which player that have won and calls the playAgain() function.
    '''
    print('Player ' + str(player) + ' wins!')
    playAgain()

def getPlayerInput(player):
    '''
        Asks the user for input and returns given input.
    '''
    playerInput = input(player + ': Rock, papers or scissors? type q to quit \n  > ').upper()
    # Checks for valid inputs
    if (not checkInput(playerInput)):
        print('* ' + playerInput + ' *' + ' is not a valid input... Try again!')
        # The function calls itself if input is invalid
        getPlayerInput(player)
    return playerInput
    
def checkInput(playerInput):
    '''
        Returns false if playerInput is invalid. Exits the script if player gives "Q" or "q" as input.
    '''
    if playerInput == 'Q':
        quit()
    return playerInput in hand

def playAgain(choise = None):
    '''
        If input parameter is None due to a draw the user(s) is asked if they want to play again.
        If input is given the function will figure out if the user(s) want to play again.
    '''
    # If either of the player wins chosise is None
    if choise is None:
        choise = input('Play again? (y/n) \n  >')
    # Yes, play again
    if choise == 'y':
        playerOneInput = getPlayerInput('Player 1')
        playerTwoInput = getPlayerInput('Player 2')
        RoPaSc(playerOneInput, playerTwoInput)
    # No, exit script
    elif choise == 'n':
        quit()
    else:
        playAgain(input('Invalid input!'))
    
# Main
if __name__ == "__main__":
    # Takes input from players
    playerOneInput = getPlayerInput('Player 1')
    playerTwoInput = getPlayerInput('Player 2')
    # Starts the rock, paper and scissors game
    RoPaSc(playerOneInput, playerTwoInput)