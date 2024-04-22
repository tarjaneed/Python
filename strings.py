str = 'Hello World!'

print(str[0]) # H

print(len(str)) # 12

print(str[2:6]) # ll0 (Excludes 6th index - includes till 5 only)

print(str[::-1]) # !dlroW olleH - Reverses the string

# Traversal

for char in str:
    print(char)

print(str.replace('H', 'J')) # Jello World!

print(str.upper()) # HELLO WORLD!

print(str.split(' ')) # ['Hello', 'World!']

print(str.find('Hello')) # 0

print(str.index('e')) # 1

print(str.count('l')) # 3

print(str.count('World')) # 1