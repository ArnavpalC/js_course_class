file = open('codingal.txt', 'r')
counter = 0

content = file.read()

coli = content.split('\n')

for i  in coli:
    if i :
        counter += 1


print('this is the number of lines in this file')
print(counter)
