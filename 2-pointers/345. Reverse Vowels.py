'''
345. Reverse Vowels of a String

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once. 

Example 1:
Input: s = "IceCreAm"
Output: "AceCreIm"

Explanation:
The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:
Input: s = "leetcode"
Output: "leotcede"
'''

'''
TC: O(n) - Reversed vowels in a single pass
SC: O(1)
'''

'''
Approach:

Take 2 pointers i and j
i = 0 and j = n - 1

We continue till i < j because if i and j crosses each other we know we have checked the entire list str
if we do not find a vowel at nums[i] we do i++
if we do not find a vowel at nums[j] we do j--

if i and j both points to vowels we swap them and then do i++ and j--
'''

def isVowel(char):
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u' or char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U':
        return True

    return False

def reverseVowels(s):
    i = 0
    j = len(s) - 1

    s = list(s)

    while i < j:
        if not isVowel(s[i]):
            i += 1
        elif not isVowel(s[j]):
            j -= 1
        else: 
            # Both i and j points to vowels
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

    s = "".join(s)
    return "".join(s)

s = "IceCreAm"
print(reverseVowels(s))

s = "leetcode"
print(reverseVowels(s))