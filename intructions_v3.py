# ask user for name, print instructions, then ask if user is ready to start
# v1 ask user for name
# v2 print instructions
# v3 ask if user is ready to start

while True:
    user_name = input('Hi there, what is your name?')
    if user_name == '' or user_name == ' ':
        print('error: please type in your name!')
    else:
        print('Welcome', user_name, 'please read the instructions carefully!')
        break

print('Hello, this will be a double digit multiplication quiz. ')
print('There will be 10 questions and at the end you will get a score out of ten. ')
print('Please only answer with numbers. Good Luck')

while True:
    user_ready = input('Are you ready to start?').lower()
    if user_ready == 'yes' or user_ready == 'y':
        print('start game')
        break
    elif user_ready == 'no' or user_ready == 'n':
        print('Please type yes when you are ready to start')
    else:
        print('ERROR: please type yes or no')
