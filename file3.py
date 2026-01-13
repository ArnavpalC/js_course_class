fr = open('codingal.txt' , 'r')

print('the file is in read mode')
print(fr.read())

fr.close()


fw = open('codingal.txt', 'w')

print('the file is in write mode')
fw.write('hi i am a penguin from codingal hq here to help you learn')

fw.close()

fw = open('codingal.txt' , 'r')
print(fw.read())

fw.close()

fa = open('codingal.txt' , 'a')

print('this file is in apend mode')
fa.write('hi i am a penguin from codingal hq here to help you learn and will guide you through the coding world')

fa.close()

fa = open('codingal.txt' , 'r')

print(fa.read())

fa.close()
