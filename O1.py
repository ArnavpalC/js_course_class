def pn(n):
    iteration = 0
    print('hjuhgashtasvas', n)
    iteration = 1
    print('bnldibegxj aUHP', iteration, '\n')





pn(10)
pn(20)


def ot(n):
    iteration = 0
    for i in range(1,n+1):
        iteration += 1
    print('input size',n,'amount of iterations = ',iteration)


ot(10)
ot(20)
ot(42)

def ons(n):
    iteration=0
    for i in range(0, n):
        for j in range(0,n):
            print('*', end=' ')
            iteration+=1
        print('')
    print('input size',n,'amount of iterations = ',iteration, '\n')

ons(5)
ons(4)
ons(3)

print('O(n^2)')
