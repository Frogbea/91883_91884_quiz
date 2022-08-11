# ask user for name, print instructions, then ask if user is ready to start
# v1 ask user for name

while True:
    user_name = input('Hi there, what is your name?')
    if user_name == '' or user_name == ' ':
        print('error: please type in your name!')
    else:
        print('Welcome', user_name, 'please read the instructions carefully!')
        break
