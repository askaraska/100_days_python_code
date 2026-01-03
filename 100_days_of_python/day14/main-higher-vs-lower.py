import random
#display art
from art import logo, vs
from game_data import data
def format_data(account):
    """takes the account data and returns(format) the account data into printable format"""
    account_name = account["name"]
    account_describe = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_describe}, from {account_country}"


# use if statement to check if user is correct. create separate function

def check_answer(user_guess,a_followers,b_followers): # need docstring if ur function return something
    """take a user guess and take follower account of a and b and returns if they got it right"""
    if a_followers > b_followers: # a has more follower
        return user_guess == "a" #return a (true)
    else:              # b has more follower
        return user_guess == "b" # return b  (false)
        # if user_guess == "a":
        #     return True
        # else:
        #     return False


print(logo)
score = 0
game_should_continue = True
# making account at position B become the next round account at position A if correct (give b to a: b = a).
account_b = random.choice(data)

# make the game repeatable, while loop- which part?- all look like static
while game_should_continue:
    # Generate a random account from game data
    # making account at position B become the next round account at position A if correct (give b to a: b = a).

    account_a = account_b # give b to a, while looping it swap value account_b to account_a
    account_b = random.choice(data) # actual random choice of account_b
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")
    # format the account data into printable format, here create separate variable for each one, and instead giving more code
    #create separate function for this
    # account_name = account_a["name"]
    # account_describe = account_a["description"]
    # account_country = account_a["country"]
    # print(f"{account_name}, a {account_describe}, from {account_country}")

    # ask user for a guess
    guess = input("Who has a more followers? type 'A' or 'B': ").lower()
    #clear screen
    print("\n" * 30)
    # every time clear screen missing logo so reprint of logo
    print(logo)
    # check if user is correct
    #get follower count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # give user feedback on their guess.  at a same time need to score keep # score keeping
    if is_correct:
        score += 1
        print("you are right! current score is: ",score)
    else:
        print("that's wrong! final score is: ",score)
        game_should_continue = False
        #works well  now repeat



