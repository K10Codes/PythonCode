
def display_board(board):
    for i,char in enumerate(board):
        if i%3==2 :
            print(char)
            print('---')
        else:
            print(char + '|', end=" ")


def player_choice(i):
    choice = input('Enter player{} choice '.format(i))
    return choice



def playerInput(player,char,board):
    validInput = False
    while not validInput:
        pInput = int(input('Enter player {} input from(1-9)'.format(player)));
        if(pInput<1 or pInput>9):
            print('Incorrect input')
            continue
        
        pInput = pInput-1
        if checkIfValidInput(board,pInput):
            board[pInput] = char
            validInput = True
        else : 
            print('Incorrect input')



def checkIfValidInput(board,i):
    return board[i] == ''

def tictactoe():
    print('Welcome to tic tac toe')
    board = ['1','2','3','4','5','6','7','8','9']
    display_board(board)
    print('Lets begin!')
    
    board = ['','','','','','','','','',]
    player1 = player_choice(1)
    player2 = 'O' if player1=='X' else 'X'
    gameFinished = False
    
    while not gameFinished:
        playerInput(1,player1,board)
        display_board(board)
        playerInput(2,player2,board)
        display_board(board)
        
        gameFinished = True


'''
Call tictactoe() to start playing
'''

tictactoe()





