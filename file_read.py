file = open('codingal.txt', 'r')
print(file.read())
file.close()

file = open('codingal.txt', 'r')
print('\n read in parts \n' )
print(file.read(8))
file.close()

file = open('codingal.txt', 'a')
file.write('hi i am a penguin and im 1 year old.')
file.close()
