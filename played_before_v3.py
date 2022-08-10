#  first component asking if the user has played before
# v1 base code
# V2 other variations of yes and no
# v3 getting the program to ask the user again if nothing is input

while True:
    played_before = input('Have you completed this quiz before?').lower()

    # if yes skip straight to quiz
    if played_before == 'yes' or played_before == 'y':
        print('skip instructions')
        break
    # play instructions if user says no
    elif played_before == 'no' or played_before == 'n':
        print('play instructions')
        break
    # retry if user inputs something incorrect
    else:
        print('error: please type in yes or no')
