"""
base component for a double digit multiplication quiz
v1: skeleton [DONE]
v2: comp 1 [DOING]
v3: comp 2 [UNDONE]
v4: comp 3 [UNDONE]
v5: comp 4 [UNDONE]
v6: comp 5 [UNDONE]
v7: comp 6 [UNDONE]
v8: final check
author = E.G
"""

# imports


# *****************functions****************************

# random generator

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
        print('play instructions')
        break
    # retry if user inputs something incorrect
    else:
        print('error: please type in yes or no')
