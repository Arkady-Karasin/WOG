# To get functions running we need:
# set FLASK_APP=MainScores.py
# flask run --port=8777


from selenium import webdriver
import os

########################################
#  Function checking user score by running Chrome
########################################
def test_scores_service(app_url):
    print("Starting Chrome")
    proj_dir = 'C:\\Users\\akarasin\\PycharmProjects'
    chrome_dr = 'chromedriver.exe'
    chrome_dr_loc = ''
    for root, dirs, files in os.walk(proj_dir):
        for name in files:
            if name == chrome_dr:
                chrome_dr_loc = os.path.abspath(os.path.join(root, name))
    if not chrome_dr_loc:
        print("Chrome driver not found")
        exit()
    chrome_driver = webdriver.Chrome(executable_path=chrome_dr_loc)
    chrome_driver.implicitly_wait(10)
    chrome_driver.get('http://192.168.99.100:8777')
    chrome_driver.implicitly_wait(10)
    score = int(chrome_driver.find_element_by_id('score').text)
    print("Score: ", score)
    if score > 0 and score < 1000:
        return True
    else:
        return False


app_url = 'http://192.168.99.100:8777'
if test_scores_service(app_url) == 1:
    print('1')
else:
    print('0')
