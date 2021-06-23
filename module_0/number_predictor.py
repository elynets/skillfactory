"""SkillFactory Module_0: Number Predictor"""

import numpy as np

"""I wanted to make this predictor more flexible and thus
I'd added a start and finish values input for random int generator"""

print("Welcome! Please set start and finish values for int generator.")
start_value = int(input("Enter a start value (default 1):") or 1)
finish_value = int(input("Enter a finish value (default 101):") or 101)

def game_core_v3(number, start_value, finish_value):    
    """We will find the number by consistent
    dividing by 2 the whole scope of possible numbers."""
    count = 1

    """Deviding all scope in two parts"""
    predict = finish_value % 2
    while number != predict:  
        count += 1
        if number > predict:
            """If our number is bigger than the first half - we will use only second half of the scope"""
            start_value = predict
            predict = (start_value + finish_value) // 2
        elif number < predict:
            """If our number is smaller than the first half - we will use only first half of the scope"""
            finish_value = predict
            predict = (start_value + finish_value) // 2

        """Printing out current prediction step, new start and finish scope values, 
        current predicted number"""        
        print(f"Try count: %2d; StartOfScope: %4d; FinishOfScope: %4d Prediction: %4d Number: %4d" 
        % (count, start_value, finish_value, predict, number))

    """Exit from while loop if number is predicted correctly"""
    return(count)


def score_game(game_core):
    global start_value, finish_value
    count_ls = []

    """Fixing random seed to replicate the test"""
    np.random.seed(1)

    random_array = np.random.randint(start_value, finish_value, size=(1000))
    for number in random_array:
        """Added start and finish values as funtion input 
        in order to make the soluion more flexible"""
        count_ls.append(game_core(number, start_value, finish_value))
    
    """Counting an average of steps to calculate the number"""
    score = int(np.mean(count_ls))
    
    print(f"The numbers were calculated within {score} tries")
    return(score)

score_game(game_core_v3)