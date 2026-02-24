n1 = int(input('enter 1st num: '))
n2 = int(input('enter 2nd num: '))

if n1<n2:
    ns=n1
    nl=n2

else:
    ns=n2
    nl=n1


while(ns):
    nus = ns
    ns = nl % ns
    nl = nus

print('HCF is: ', nl)
