lst = ['Apple', 'orange', 'papaya', 'jackfruit', 'mango', 'guava']

print('the length of the list is', len(lst))
print("the first item in the list is", lst[0])
print('the last item in the list is', lst[-1])

lst.append('jackfruit')
print('new list is', lst)

lst.remove('papaya')
print('an item was not needed and is removed list now is', lst)

lst.sort()
print('the list is sorted', lst)

lst.pop(1)
print('newer list', lst)

lst.reverse()
print('the reversed list', lst)
