'''
Check if a given string is palindrome

Input: "madam"
Output: True

Input: "madsm"
Output: False
'''

def is_palindrome(str, l, r):

    if l >= r: # We scanned the entire string and reached the mid and all characters matched thus Palindrome
        return True

    if str[l] != str[r]:
        return False
    
    # else
    return is_palindrome(str, l + 1, r - 1)

s = "madam"
print(is_palindrome(s, 0, len(s) - 1))

s = "madsm"
print(is_palindrome(s, 0, len(s) - 1))