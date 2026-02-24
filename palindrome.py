num = int(input("entr your number: "))

on = num
rn = 0


while num > 0:
    dig = num % 10
    rn = rn * 10 + dig
    num //=10

if on == rn:
    print(f'{on} this number is a palindrome')

else:
    print(f'{on} is not a palindrome')
