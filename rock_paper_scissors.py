import random

def play():
    # take both the user and computer input
    user = input("What's your choice? 'r' for rock, 'p' for paper 's', for scissors -> ")
    computer = random.choice(['r', 'p', 's'])

    # set some rules i.e r > s, s > p, p > r
    if user == computer:
        return 'It\'s a tie'

    if is_win(user, computer):
        return 'You won!'

    return 'You lost!'

# defined the helper function is_win to see who wins
def is_win(player, opponent):
    # return true if player wins
    # r > s, s > p, p > r
    if (player == 'p' and opponent == 'r') or (player == 's' and opponent == 'p') \
        or (player == 'r' and opponent == 's'):
        return True

print(play())