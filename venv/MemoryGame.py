import Utils
import array as arr
import time
from random import randint
import os

####################################
### GENERATE LIST OF NUMBERS
####################################
def generate_sequence(difficulty):
    #nums = arr.array("i")
    nums = ''
    list_a = []
    for i in range(difficulty):
        num = str(randint(1, 101))
        nums = nums + ' ' + num
        list_a.append(num)
    print("Numbers: ", nums)
    time.sleep(0.7)
    Utils.screen_cleaner()
    return list_a

###################################
### GET USER GUESSES
###################################
def get_list_from_user(difficulty):
    print("After seeing the numbers enter the numbers you saw, each one separated with Enter.")
    nums = []
    for i in range(difficulty):
        val = input(">")
        nums.append(val)
    return nums

###################################
### COMPARE COMPUTER AND USER LISTS
###################################
def is_list_equal(list_a, list_b):
    list_a.sort()
    list_b.sort()
    if list_a == list_b:
        return True
    return False

####################################
### MAIN MODULE
####################################
def play(difficulty):
    list_gen = generate_sequence(difficulty)
    list_user = get_list_from_user(difficulty)
    if is_list_equal(list_gen, list_user):
        return difficulty
    else:
        return 0 
