'''
Given a string and a pattern, find out if the string contains any permutation of the pattern
Example 1:
Input: String="oidbcaf", Pattern="abc"
Output: true
Explanation: The string contains "bca" which is a permutation of the given pattern.
'''

'''
Approach:

This is a fixed size sliding window problem. Assuming that the string and pattern would always be lowercase.
Window size = size of the pattern to be matched i.e. for eg. 3

- Take the lengths of both string and pattern
- Check if pattern is > string then return False; Only continue if pattern <= string
- Take 2 lists to maintain pattern_count & string_count i.e. S1 and S2 of size 26 and initialize them to 0. 26 since there are 26 alphabets
- Now build the initial window of size eg. 3 (go till length of S2 (0 - 2)) as per the example and build the 2 lists as well.
- Match the 2 lists if they are equal return True meaning the pattern is found.
- If they do not match we slide the window. Starting from S1 (3) and going till S2 (7 - 1 = 6)
    - Here we add the currently visited element to the window and in S2 we increment count for that index
    - We also need to remove the element from the left from the window which would be (i - S1) = (3 - 3) = 0 and so on...
    - We again check 2 lists match and return True
- Once we reach end of the list we know we did not find the pattern otherwise we would have return True already and break hence we return False
'''

def findStringPermutation(S2, S1):
    n1 = len(pattern)
    n2 = len(string)

    if n1 > n2:
        return False
    
    S1_count = [0] * 26 # For Pattern index marking - Each character/letter maps to an array index
    S2_count = [0] * 26 # For String index marking - Each character/letter maps to an array index

    # Build the intial window based on pattern
    for i in range(n1):
        S1_count[ord(S1[i]) - ord('a')] += 1
        S2_count[ord(S2[i]) - ord('a')] += 1

    # Check if lists are equal
    if S1_count == S2_count:
        return True
    
    # Otherwise slide the window to match and update the S2_count list; no need to update the S1_count as the pattern to be matched would be constant and won't change but S2 would 
    # change as it slides till end of S2
    for i in range(n1, n2):
        # Add element to the right
        S2_count[ord(S2[i]) - ord('a')] += 1

        # Remove element from the left; Find the index to be updated
        S2_count[ord(S2[i - n1]) - ord('a')] -= 1

        # Match lists
        if S1_count == S2_count:
            return True

    return False


pattern = 'ab'
string = 'eidbaooo'

print(findStringPermutation(string, pattern))

pattern = 'ab'
string = 'eidboaoo'
print(findStringPermutation(string, pattern))

# SC: O(1) 2 lists of length 26 but it is still a constant
# TC: O(n)
