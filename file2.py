firstfile = input('enter the content of the first file: ')
secfile = input('enter the content of the second file: ')

f1 = open(firstfile , 'a+')
f2 = open(secfile , 'r')

f1.write(f2.read())

f1.seek(0)
f2.seek(0)

print('content of the first file after appending \n', f1.read())
print('content of the second file after appending \n', f2.read())

f1.close
f2.close
