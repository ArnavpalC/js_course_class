prime={1,2,3,5,7,9,11,13}
odd={1,3,5,7,9,11,13,15,17}
even={2,4,6,8,10,12,14,16}

print(prime)
print(odd)
print(even)

prime.add(17)
prime.add(3)
print('updated first listof numbers', prime)


print('the prime odd numbers are', prime.intersection(odd))
print('the prime numbers that are not odd', prime.difference(odd))
print('all the numbers are', odd.symmetric_difference(even))
print('the even prime numbers are', prime.intersection(even))
print('the odd and prime numbers are', prime.union(odd))

