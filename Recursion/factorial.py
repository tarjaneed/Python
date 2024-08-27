# Factorial of N numbers

# TC: O(n) Number of function calls = time complexity
# SC: O(n)

def factorial(n):
    if n == 1:
        return 1
    
    return n * factorial(n - 1)

n = 3
print(factorial(n))

n = 4
print(factorial(n))