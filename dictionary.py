'''
- Ordered collection of key-value pairs i.e. maintains the order or sequence in which the elements are stored
- Allows duplicate values but not keys
- Mutable
'''

dict1 = {} # Empty Dictionary
user = {'name': 'John', 'age': 25, 'city': 'NYC'}

print(dict1)
print(user)

print(user['name']) # Access dictionary value

key = 'name'
if key in user.keys():
    print(f'{key} Found')
else:
    print(f'{key} not found')

key = 'age'
if key in user:
    print(f'{key} Found')
else:
    print(f'{key} not found')

print(user.items()) # Returns Tuples of Key Value Pairs
print(user.keys()) # Returns list of keys
print(user.values()) # Returns list of values

user['gender'] = 'male' # Adding data to the dictinary
print(user)

user['age'] = 40 # Updating data in the dictionary
print(user)

print(user.get('name')) # Get value for the given key

del user['age'] # Deleting key/data from the dictionary
print(user)

user.pop('name')
print(user)

count = {'1': 2, '2': 1, '3': 5}

# Sort count dictionary in reverse order based on count value - Lambda Function
sorted_dict = sorted(count.items(), key = lambda item: item[1], reverse=True)
print(sorted_dict)