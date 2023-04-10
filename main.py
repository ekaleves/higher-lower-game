import random
import art
import game_data
from replit import clear




def reject_sample(list, exception):
    """Check if the second item it is not the same as the first item"""
    while True:
        choice = random.choice(list)
        if choice != exception:
            return choice

def compare(a, b, user_choice):
    """Receive two dictionaries and the user's choice, and check which one has the higher amount of followers. Returns the points made, the position where this happened."""
    points = 0
    if user_choice == "a":
        if a['follower_count'] >= b['follower_count']:
            points = 1
            index_wins = 1
        elif a['follower_count'] < b['follower_count']:
            clear()
            index_wins = 2
    elif user_choice == "b":
        if b['follower_count'] >= a['follower_count']:
            points = 1
            index_wins = 3
        elif b['follower_count'] < a['follower_count']:
            clear()
            index_wins = 4
            
    return points, index_wins


def random_option():
    """Choose a random item from the list game_data"""
    option = random.choice(game_data.data)
    return option

def show_options(first, second):
    print(f"Compare A: {first['name']}, {first['description']}, {first['country']}.")
    
    
    print(f"{art.vs}\n\n")
    
    print(f"Compare B: {second['name']}, {second['description']}, {second['country']}.")
    
    

option_a = random_option()
option_b = random_option()

option_b = reject_sample(game_data.data, option_a)


print(f"{art.logo}\n\n\n")


show_options(option_a, option_b)

answer = input("\nWho has more followers? Type 'A' or 'B': ").lower()

score = 0
score_loop, index_wins = compare(option_a, option_b, answer)

score += score_loop
loose = False



while loose == False:
    
    if index_wins == 1:
        clear()
        option_a = option_b
        option_b = random_option()
        option_b = reject_sample(game_data.data, option_a)
        print(f"{art.logo}\n\n\n")
        print(f"You're right! Current score: {score}.\n")
        show_options(option_a, option_b)
        answer = input("\nWho has more followers? Type 'A' or 'B': ").lower()
        score_loop, index_wins = compare(option_a, option_b, answer)
        score += score_loop
    elif index_wins == 2:
        clear()
        print(f"Sorry, that's wrong. Final score: {score}")
        loose = True
    elif index_wins == 3:
        clear()
        option_b = random_option()
        option_b = reject_sample(game_data.data, option_a)
        print(f"{art.logo}\n\n\n")
        print(f"You're right! Current score: {score}.\n")
        show_options(option_a, option_b)
        answer = input("\nWho has more followers? Type 'A' or 'B': ").lower()
        score_loop, index_wins = compare(option_a, option_b, answer)
        score += score_loop
    elif index_wins == 4:
        clear()
        print(f"{art.logo}\n\n\n")
        print(f"Sorry, that's wrong. Final score: {score}")
        loose = True
    
    

