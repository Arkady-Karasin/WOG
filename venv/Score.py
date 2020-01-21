import Utils

###############################
### ADDING SCORE TO SCORE FILE
###############################
def add_score(score_file, score_add):
    try:
        f = open(score_file, "r")
        score_exist = int(f.read())
        f.close()
    except IOError as e:
        try:
            f = open(score_file,"x")
            f.close()
            score_exist = 0
        except IOError as ee:
            print(utils.ERROR_MESSAGE, ee)
            return
    try:
        f = open(score_file, "w")
        score_new = str(score_exist + score_add)
        f.write(score_new)
        f.close()
        print("Your score is", score_new)
        
    except IOError as eee:
        print(Utils.ERROR_MESSAGE, eee)
        return






