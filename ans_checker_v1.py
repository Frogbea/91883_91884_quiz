# checks whether users answer is right or wrong and prevents crashing if not an interger
# v1 making it not crash if something that is not an interger is inputted

import random as r


def random():
    # sets num_1 and num_2 as random numbers
    num_1 = r.randint(10, 99)
    num_2 = r.randint(10, 99)
    # asks the user to answer
    user_answer = int(input('What is {} x {}?'.format(num_1, num_2)))
    print(user_answer)


def ans_checker():
    while True:
        try:
            random()
        except:
            print('Error: please input a number!')


ans_checker()
