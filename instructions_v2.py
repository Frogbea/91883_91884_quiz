# ask user for name, print instructions, then ask if user is ready to start
# v1 ask user for name
# v2 print instructions

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
