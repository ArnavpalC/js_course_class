of = open('co1.txt', 'w')
inf = open('co2.txt', 'r')

l_s_s_f = set()
print('eliminating dupe lines: \n')
for line in inf:
    if line not in l_s_s_f:
        of.write(line)
        l_s_s_f.add(line)



of.close()
inf.close()

of = open('co1.txt', 'r')
print(of.read())
of.close()
