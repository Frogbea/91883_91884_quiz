# second component asking if the user has played before
# v1 base code

played_before = input('Have you completed this quiz before?')

if played_before == 'Yes':
    print('skip instructions')
elif played_before == 'No':
    print('play instructions')
