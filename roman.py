def romanToInt(romanInput):
    roman = {'M':1000,'D':500,'c':100,'L':50,'X':10,'V':5,'I':1}

    resultIntiger = 0
    for i in range(0,len(romanInput) -1):
        if roman[romanInput[i]] < roman[romanInput[i+1]]:
            resultIntiger -= roman[romanInput[i]]

        else:
            resultIntiger += roman[romanInput[i]]
    return resultIntiger + roman[romanInput[-1]]

roman = input('input roman numerals: ')

print('intiger equivalent : ',romanToInt(roman))

        
