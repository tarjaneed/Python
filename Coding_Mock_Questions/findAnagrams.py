'''
Given a word pat and a text txt. Return the count of the occurences of anagrams of the word in the text.

Example 1:

Input:
txt = forxxorfxdofr
pat = for
Output: 3
Explanation: for, orf and ofr appears in the txt, hence answer is 3.

Example 2:

Input:
txt = aabaabaa
pat = aaba
Output: 4
Explanation: aaba is present 4 times in txt.
'''

'''
Approach:

Here the window size i.e. k = len(pattern)
So we would keep on checking the window size of k in the string and keep sliding it to find the anagrams.

- Initialize result = [] and anagram_count = 0
- Create a hashmap for pattern => {char: count} - a way to keep track and check different possibilties of anagrams of a given string
- Initialize a hash_counter variable to len(pattern_hashmap); this will be useful to determine whether the window we are currently checking when we hit the window k is a anagram or not;
    So, if this hash_counter becomes zero by the time we hit k we know that we found 1 anagram; 
    we need to decrement it everytime we traverse 'j', we check if s[j] is present in the hashmap; if it is we decrement the count of s[j] in hashmap;
    after that we immediately check if s[j] in hashmap became 0; if it becomes 0 we decrement the hash_counter indicating we found all the quantity of letter in s[j] as needed. For. eg
    3 a's found.
- Initialize i = 0 and j = 0
- Loop j till end of the string length:
    Calculations Part for every jth element we are traversing: Checks 2 things: 1) Same no. of letters/characters (length) 2) Same quantity of characters eg. b -> 2 times, a -> 1 time.
        First check if s[j] is present in the hash_counter; Decrement hash_counter[s[j]] everytime we traverse 'j', we check if s[j] is present in the hashmap; 
        if it is we decrement the count of s[j] in hashmap;
        after that we immediately check if s[j] in hashmap became 0; if it becomes 0 we decrement the hash_counter indicating we found all the quantity of letter in s[j] as needed. For. eg
        3 a's found.

    Check window size
    if current_window_size we are checking i.e. (j - i + 1) < k:
        we increment j till it becomes equal to k (given window size)

    elif current_window_size we are checking i.e. (j - i + 1) = becomes equal to k
        we find answer from the calculations we did so far
            here, we check the hash_counter: if it is 0 we know we found one anagram; increment anagram_count by 1 and push it to the result

        Then we slide the window i.e move both i and j
        but before moving i we need to remove its calculations too
            check if the ith element i.e. s[i] is present in the hashmap_pattern; if it is increment its count in hashmap by 1 because during calculations we decremented so we reverse:
                hashmap_pattern[s[i]] += 1
            Then check if this hashmap_pattern[s[i]] became = 1 or > 0? if it did increment the hash_counter too => hash_counter++
            Then move i and j
'''

# TC: O(n) SC: O(n) in worst case if length of pattern is same as the length of input but all the characters are different

def findAnagrams(s, p):
    result = []
    anagram_count = 0

    pattern_hash = {}

    for i in range(0, len(p)):
        if p[i] not in pattern_hash:
            pattern_hash[p[i]] = 1
        else:
            pattern_hash[p[i]] += 1

    hash_counter = len(pattern_hash)

    i = 0
    j = 0
    k = len(p)

    while j < len(s):
        if s[j] in pattern_hash:
            pattern_hash[s[j]] -= 1

            if pattern_hash[s[j]] == 0:
                hash_counter -= 1

        if j - i + 1 < k:
            j += 1
        elif j - i + 1 == k:
            if hash_counter == 0:
                anagram_count += 1
                result.append(anagram_count)
            
            # Slide the window and remove i from the calculations

            if s[i] in pattern_hash:
                pattern_hash[s[i]] += 1

                if pattern_hash[s[i]] > 0:
                    hash_counter += 1

            i += 1
            j += 1

    return result

txt = 'ppqp'
pat = 'pq'
print(findAnagrams(txt, pat))

txt = 'aabaabaa'
pat = 'aaba'
print(findAnagrams(txt, pat))

txt = 'forxxorfxdofr'
pat = 'for'
print(findAnagrams(txt, pat))