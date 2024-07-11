'''
Given a string s, find the length of the longest substring without repeating characters.
Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
'''

'''
Approach:

Intialize the longest_substring with some min value.

Start i and j at 0

Loop till j < len(s):
    Create a hash that stores the {char: count} of the jth element we are traversing

    Now here condition is that all characters in the window we check must be unique.

    hashmap size gives us number of unique characters that we match with the current window size (j - i + 1)

    if hashmap_size == (j - i + 1): # Means we found a window that could be the answer
        here update longest_substring
        longest_substring = max(longest_substring, j - i + 1)
        j++
    
    else if hashmap_size < (j - i + 1) # that if the window size is > that hashmap size (that gives us unique character)
    we know that window has duplicate characters
        so we loop till hashmap_size becomes equal to window size
        while hashmap_size < (j - i + 1):
            # We remove ith element and update the count in hashmap
            hashmap[S[i]]--
            if (hashmap[S[i]] == 0)
                delete hashmap[S[i]]
            i++
    j++
'''

def findLongestSubstring(s):
    longest_string = 0

    i = 0
    j = 0
    hashmap = {}

    while j < len(s):
        if s[j] in hashmap:
            hashmap[s[j]] += 1
        else:
            hashmap[s[j]] = 1

        if len(hashmap) == (j - i + 1):
           longest_string = max(longest_string, j - i + 1)
           j += 1

        elif len(hashmap) < j - i + 1:
            while len(hashmap) < j - i + 1:
                hashmap[s[i]] -= 1

                if hashmap[s[i]] == 0:
                    del hashmap[s[i]]
                i += 1
            j += 1

    return longest_string

print(findLongestSubstring('abcabcbb'))
print(findLongestSubstring('aaa'))

# TC: O(n) SC: O(n)