def setOrNot(number, n):
    if number & (1 <<(n - 1)):
        print('\n set')

    else:
        print('\n not set')

number = int(input('enter number: '))
n = int(input('enter bit number: '))
setOrNot(number,n)
