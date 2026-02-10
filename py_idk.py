def fu1(n):
    return n*(n+1)/2

def fu2(n):
    sum=0
    for i  in range(1,n+1):
        sum += i
    return sum


def fu3(n):
    sum=0
    for i  in range(1,n+1):
        for j in range(1,i+1):
            sum += 1
    return sum


print(fu1(83238323))
print(fu2(83231))
print(fu3(83231))
