# second component asking if the user has played before
# v1 base code
# V2 other variations of yes and no

played_before = input('Have you completed this quiz before?').lower()

# if yes skip straight to quiz
if played_before == 'yes' or played_before == 'y':
    print('skip instructions')
# play instructions if user says no
elif played_before == 'no' or played_before == 'n':
    print('play instructions')
# retry if user inputs something incorrect
else:
    print('please type in yes or no')
