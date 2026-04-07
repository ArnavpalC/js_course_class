def divide(od, odi):
    sign = (-1 if((od < 0)^
                  (odi < 0))else 1);
    od = abs(od);
    odi = abs(odi)

    qn = 0
    tn = 0

    for i in range(31, -1, -1):

        if (tn + (odi << i) <= od):
            tn += odi << i
            qn |= 1 << i

    if sign ==-1 :
        qn=-qn
    return qn

a = int(input('enter a for a/b: '))
b = int(input('enter b for a/b: '))
print('result of',a,'divided by',b,'is',divide(a, b))
