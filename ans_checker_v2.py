# checks whether users answer is right or wrong and prevents crashing if not an integer
# v1 making it not crash if something that is not an integer is inputted
# v2 getting the same question to repeat afterwards

import random as r


def random_function():
    # sets num_1 and num_2 as random numbers
    num_1 = r.randint(1, 10)
    num_2 = r.randint(1, 10)
    # asks the user to answer
    return num_1, num_2


def ans_checker():
    ran_num_1, ran_num_2 = random_function()
    while True:
        try:
            user_answer = int(input('What is {} x {}?'.format(ran_num_1, ran_num_2)))
            print(user_answer)
            if user_answer == ran_num_1*ran_num_2:
                print('Correct, Good job! :)')
                break
            else:
                print('Aw, not quite right :( try again!')
        except:
            print('Error: please input a number!')


ans_checker()
