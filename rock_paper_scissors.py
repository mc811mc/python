from random import randint

computer = ['rock', 'paper', 'scissors']

com_num = randint(0,2)

com_sel = computer[com_num]

player = input('Rock, paper, scissors GO! ')
player = player.lower()

if 'rock' or 'paper' or 'scissors' not in player:
    print("That is not how you play rock, paper, scissors!")

if player == 'rock' or 'paper' or 'scissors':    
    #win
    if player == 'rock' and com_sel == 'scissors':
        print('You win! ', player.title(), ' beats ', com_sel, '!', sep ='')
    if player == "paper" and com_sel == "rock":
        print('You win! ', player.title(), ' beats ', com_sel, '!', sep ='')
    if player == 'scissors' and com_sel == 'paper':
        print('You win! ', player.title(), ' beats ', com_sel, '!', sep ='')

    #draw
    if player == com_sel:
        print('It\'s a draw!')
        
    #lose
    if player == 'rock' and com_sel == 'paper':
        print('You lose.', com_sel.title(), "beats", player, '!', sep = '')
    if player == 'paper' and com_sel == 'scissors':
        print('You lose.', com_sel.title(), "beats", player, '!', sep = '')
    if player == 'scissors' and com_sel == 'rock':
        print('You lose.', com_sel.title(), "beats", player, '!', sep = '')