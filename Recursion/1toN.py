# Print 1 to N

# TC: O(n)
# SC: O(n)

def printSeq(i, n):

    if i > n:
        return
    
    print(i)
    printSeq(i + 1, n)

n = 5
printSeq(1, n)