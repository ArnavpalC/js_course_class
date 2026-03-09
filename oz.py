def numberOfBits(n):
    o = 0
    z = 0


    while(n):
        if(n&1==1):
            o+=1
        else:
            z+=1


        n >>= 1
    print('\n\n ones=',o,'\n zeros',z)


number = int(input('enter your number: '))
numberOfBits(number)
