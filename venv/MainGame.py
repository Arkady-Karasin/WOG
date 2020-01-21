# To start this app in container we should run:
# docker run -ti venv_web

from Live import load_game, welcome
import MainScores, e2e
from selenium import webdriver
import os
#####################
###  MAIN MODULE
#####################
name = ''
print(welcome(name))
load_game()

########################
### WHEN USER WIN WE WILL OPEN CHROME, BUT FLASK SHOULD BE STARTED BEFORE
########################
e2e.main_function()
