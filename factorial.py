def su(n):
    if(n<=0):
        return 0
    return n+ su(n-1)

print(su(125))
