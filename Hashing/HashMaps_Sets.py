''' Hash Maps or Sets does not allow duplicates
Time Complexiy:
    Creating a Hash Map - O(n) Space Complexity - O(n)
    Insert - O(1) Avg. Case.
    Remove - O(1) Avg. Case.
    Search - O(1) Avg. Case.

If the hash function is not good it these operations can take O(n) in worst case

Hash Maps are not ordered, so if we want to iterate through all the keys first we need to sort them O(logn) and then traverse it O(nlogn)
'''

names = ["Alice", "Bob", "Alice", "John", "Lily"]
frequencyHash = {}

print('Before:', frequencyHash)

for name in names:
    if name not in frequencyHash:
        frequencyHash[name] = 1
    else:
        frequencyHash[name] += 1

print('After:', frequencyHash)