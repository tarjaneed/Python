# Print N to 1

# TC: O(n)
# SC: O(n)

# Print statement executes once we reach base case and function returns to previous. Printing happens during backtrack - going back.

def printSeq(i, n):
    if i > n:
        return

    printSeq(i + 1, n)
    print(i)

n = 5
printSeq(1, n)