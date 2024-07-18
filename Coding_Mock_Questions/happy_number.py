'''
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

Example 1:

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

Example 2:

Input: n = 2
Output: false
'''

# If we find a number in set it means its already seen so not a happy number else if we reach 1 we know that the number is a happy number and that it is also not seen.

# TC: O(logn) since it depends on time it takes to do sumOfSquareOfDigits - everytime we keep dividing it by 10 SC: O(1)

def isHappyNumberLL(num):
    slow = num
    fast = sumOfSquareofNums(num)

    # Continue till slow != fast i.e. if slow == fast loop breaks and that we found a cycle so number is not a happy number or we reached 1 i.e. fast is moving ahead so if it reaches 1 we know 
    # we found a happy number and the loop breaks
    # slow moves by 1 and fast moves by 2
    while fast != 1 and slow != fast:
        slow = sumOfSquareofNums(slow)
        fast = sumOfSquareofNums(sumOfSquareofNums(fast))

    return fast == 1

def isHappyNumber(num):
    visited = set()

    while num not in visited:
        visited.add(num)

        if num == 1:
            return True

        num = sumOfSquareofNums(num)

    return False

def sumOfSquareofNums(num):

    totalSum = 0
    while num > 0:
        digit = num % 10 # One's place value
        digit = digit ** 2 # Square it ** is for power 2
        totalSum += digit
        num = num // 10 # Update the n for next digit square and addition to the total sum

    return totalSum

print(isHappyNumberLL(19))
print(isHappyNumberLL(2))