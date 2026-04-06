def power2(n):
    if(n == 0):
        return 0
    if((n & (~(n - 1))) == n):
        return 1
    return 0

n = int(input('enter your number: '))

if(power2(n)):
    print('\n the number is a power of 2')

else:
    print("\n the number isn't a power of 2")
