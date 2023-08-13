import random

def get_choices():
    player_choice = input("Enter your choice: ")
    RPS = ['rock','paper','scissors']
    computer_choice = random.choice(RPS)
    choices = {'player':player_choice, 'computer':computer_choice}
    return choices

def check_win(player, computer):
    print(f'You chose {player}. Computer chose {computer}.')
    if player == computer:
        return 'Its a tie!'
    elif player == 'rock':
        if computer == 'paper':
            return 'Paper covers rock! You lose!'
        else:
            return 'Rock smashes scissors! You win!'
    elif player == 'paper':
        if computer == 'scissors':
            return 'Scissors cut paper! You lose!'
        else:
            return 'Paper covers rock! You win!'
    elif player == 'scissors':
        if computer == 'rock':
            return 'Rock smashes scissors! You lose!'
        else:
            return 'Scissors cut paper! You win!'

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)
