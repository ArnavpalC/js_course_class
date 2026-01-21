nf = open('new_file.txt', 'x')
nf.close()

import os

print('cheacking if my file exists or not')
if os.path.exists('my_file.txt'):
    os.remove('my_file.txt')

else :
    print('this file does not exist')

my_file = open('my_file.txt', 'w')
my_file.write('Hi! I am Penguin and I am 1 year old')
my_file.close()

os.remove('codingal.txt')
