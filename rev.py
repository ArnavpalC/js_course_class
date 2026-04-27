n =[2, 4, 6, 8]

r = {}

def calculate(nu):
    
    total = sum(nu)
    av = total / len(nu)

    r['sum']= total
    r['average']= av


calculate(n)

print('numbers: ',n)
print('result: ', r)

n1 =[2, 4, 6, 8]

pr = {}

def calculate(nu):
    p = 1
    for i in nu:
        p *= i

    pr['product']= p



calculate(n1)


print('result: ', pr)
