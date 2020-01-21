###########################
### gENERATING RANDOM NUMBER
###########################
def generate_number(difficulty):
    from random import randint
    return randint(1, difficulty)

#############################
### GET USER BET
#############################
def get_guess_from_user(difficulty):
    guess = 0
    while guess < 1 or guess > difficulty:
        output = "Please enter number between 1 and " + str(difficulty) + ": "
        guess = int(input(output))
    return guess

###############################
### CHECK IF USER GUESS RIGHT
###############################
def compare_results(difficulty, secret_number):
    if secret_number == get_guess_from_user(difficulty):
        return True
    return False

###############################
### MANAGE GAMES
###############################
def play(difficulty):
    secret_number = generate_number(difficulty)
    #print("Generated", secret_number)
    if compare_results(difficulty, secret_number):
        return difficulty
    else:
        return 0
