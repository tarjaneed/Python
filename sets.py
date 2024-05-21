'''
- Unordered collection of unique elements i.e. does not maintain the order or sequence - we do not know the order in elements are stored
- Duplicates are not allowed
- Mutable but cannot change its value with assignment
'''

set1 = set() # Empty Set
print(set1)

set2 = {1, 2, 3, 1}
print(set2) # {1, 2, 3} - No Duplicates

set2.add('Hello') # Add an item
print(set2) # {1, 2, 3, 'Hello'}

set2.remove(3) # Remove an item
print(set2) # {1, 2, 'Hello'}

#set2[1] = 'Test' # This does not work

if 'Hello' in set2:
    print('Found')
else:
    print('Not Found')

set3 = {1, 2}
set4 = {2, 3, 4}

print(set3.union(set4)) # {1, 2, 3, 4}
print(set3.intersection(set4)) # {2}
print(set3.difference(set4)) # {1} - if set4 - set3 then { 3, 4 } i.e. elements in set4 not in set3

print(set3 | set4) # {1, 2, 3, 4} - Union
print(set3 & set4) # {2} - Intersection
print(set3 - set4) # {1} - if set4 - set3 then { 3, 4 } i.e. elements in set4 not in set3 - Difference