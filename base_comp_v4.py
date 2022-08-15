"""
base component for a double digit multiplication quiz
v1: skeleton [DONE]
v2: comp 1 [DONE]
v3: comp 2 [DONE]
v4: comp 3 [DOING]
v5: comp 4 [UNDONE]
v6: comp 5 [UNDONE]
v7: comp 6 [UNDONE]
v8: final check
author = E.G
"""

# imports
import random as r


# *****************functions****************************

# instructions function
def instructions():
    # asks user for name
    while True:
        user_name = input('Hi there, what is your name?')
        # shows error if user inputs bank
        if user_name == '' or user_name == ' ':
            print('error: please type in your name!')
        # continues when user inputs name
        else:
            print('Welcome', user_name, 'please read the instructions carefully!')
            break

    # print instructions
    print('Hello, this will be a double digit multiplication quiz. ')
    print('There will be 10 questions and at the end you will get a score out of ten. ')
    print('Please only answer with numbers. Good Luck')

    # asks if user is ready
    while True:
        user_ready = input('Are you ready to start?').lower()
        # is yes start game
        if user_ready == 'yes' or user_ready == 'y':
            print('start game')
            break
        # if no ask again
        elif user_ready == 'no' or user_ready == 'n':
            print('Please type yes when you are ready to start')
        # if number or something else shows error then try again
        else:
            print('ERROR: please type yes or no')


# answer checker

# any other one I magically come up with

# ******************************************************************************************
# main route


while True:
    played_before = input('Have you completed this quiz before?').lower()

    # if yes skip straight to quiz
    if played_before == 'yes' or played_before == 'y':
        print('Welcome back!')
        break
    # play instructions if user says no
    elif played_before == 'no' or played_before == 'n':
        instructions()
        break
    # retry if user inputs something incorrect
    else:
        print('error: please type in yes or no')

# repeats the question 10 times
for n in range(10):
    # sets num_1 and num_2 as random numbers
    num_1 = r.randint(10, 99)
    num_2 = r.randint(10, 99)
    # asks the user to answer
    user_answer = int(input('What is {} x {}?'.format(num_1, num_2)))


