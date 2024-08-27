# Sum of first N numbers

# TC: O(n) Number of function calls = time complexity
# SC: O(n)

def sum(n):
    if n == 0:
        return 0
    
    return n + sum(n - 1)

n = 3
print(sum(n))

n = 4
print(sum(n))