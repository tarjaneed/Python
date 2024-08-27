# Print N to 1

# TC: O(n)
# SC: O(n)

def printSeq(n):
    if n == 0:
        return
    
    print(n)
    printSeq(n - 1)

n = 5
printSeq(n)