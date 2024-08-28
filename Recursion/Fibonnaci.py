'''
Print nth fibonnaci number
'''

# TC: O(2 power n) - At every step we call function twice 2 * 2 * 2 .... n = 2 power n
# SC: O(2 power n)

def fibonnaci(n):
    if n <= 1:
        return n
    
    return fibonnaci(n - 1) + fibonnaci(n - 2)

n = 3
print(fibonnaci(n))

n = 5
print(fibonnaci(n))