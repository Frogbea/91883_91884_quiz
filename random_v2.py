# make a generator that randomly multiplies 2 numbers
# v1 making the generater
# v2 ask the question

import random as r

num_1 = r.randint(10, 99)
num_2 = r.randint(10, 99)

user_answer = int(input('What is {} x {}?'.format(num_1, num_2)))


