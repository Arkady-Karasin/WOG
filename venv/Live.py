import MemoryGame, GuessGame, Score
import os
import Utils
#from MemoryGame import play
#from GuessGame import play

##########################
### GETTING NAME AND DELETING OLD SCORE FILE
##########################
def welcome(name):
    if name =='':
        try:
            name = input("Please, enter your name: ")
        except EOFError as eof:
            welcome('')
        if len(name) < 2:
            welcome('')
    ret = "Hello " + name + " and welcome to the World of Games (WoG). \r\n Here you can find many cool games to play"
    try:
        os.remove(Utils.SCORES_FILE_NAME)
    except FileNotFoundError as nn:
        a = 0
    return ret

#################################
### GET USER GANE SELECTION AND DIFFICULTY
### LOOP INTIL USER WILL WIN
#################################
def load_game():
    game_num = 0
    game_dif = 0
    score = 0
    while score == 0:
        while game_num < 1 or game_num > 2:
            try:
                game_num = int(input("1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.\r\n"
                                     "2. Guess Game - guess a number and see if you chose like the computer\r\n"
                                     "0. To cancel"))
            except ValueError as ee:
                print("Incorrect input. Try again.")
            if game_num == 0:
                exit()
        while  game_dif < 1 or game_dif > 5:
            try:
                game_dif = int(input("Please choose game difficulty from 1 to 5:"))
            except ValueError as ee:
                print("Incorrect input. Try again.")
        if game_num == 1:
            score = MemoryGame.play(game_dif)
        if game_num == 2:
            score = GuessGame.play(game_dif)
        if score > 0:
            score_file = "Scores.txt"
            Score.add_score(score_file, score)
            return


