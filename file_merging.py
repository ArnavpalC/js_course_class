with open('codingal1.txt') as fp:
    data1 = fp.read()

with open('co1.txt') as sp:
    data2 = sp.read()

data1 += '\n'
data1 += data2
print('merging the two files')
with open('mf.txt', 'w') as pp:
    pp.write(data1)

pp.close()

pp = open('mf.txt', 'r')
print(pp.read())
pp.close()
