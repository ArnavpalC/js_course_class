def swap(a ,b):
     a = a^b
     b = b^a
     a = a^b
     print('after swaping first time: a is ',a,' and b is ',b)

def swap2(a , b):
    a = (a & b) + (a | b)

    b = a + (~b) + 1

    a = a + (~b) + 1

    print('after swaping second time: a is ',a,' and b is ',b)

swap(2,1)
swap2(1,2)

        
