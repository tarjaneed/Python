'''
Print name n times
'''

# TC: O(n)
# SC: O(n)

def printName(i, n):
    # Stop condition / Base condition - we don't print if current index exceeds given input
    if i > n:
        return
    print('Tarjanee')
    printName(i + 1, n)


n = 5
printName(1, n)