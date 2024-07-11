'''
Given an array of unsorted numbers, find all unique triplets in it that add up to zero.

Example 1:
Input: [-3, 0, 1, 2, -1, 1, -2]
Output: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
Explanation: There are four unique triplets whose sum is equal to zero.
'''

'''
Approach:

n1 + n2 + n3 = 0
We need to find 3 numbers whose sum is equal to 0.
n2 + n3 = -(n1)
2Sum        Target

- Sort
- Remove Duplicates to avoid duplicate triplets
- While fixing n1 number, as well remove duplicates to avoid duplicate triplets
- then on the remaning array perform 2 Sum to find n2 and n3 and target must be -(n1). i.e.

- Sort the given input since we need to return the numbers in the triplet and not indexes.
- Loop through the input array to find triplets:
    fix n1 but before that check if it has been already considered
    do not consider if it has already been considered

    if nums[i] == nums[i - 1]:
        continue; consider next i as an element to be fixed

    n1 = nums[i]
    target = -(n1)

    Perform 2 sum on the remaning elements:
    
    2Sum(target, nums, i + 1(start), len(nums) - 1(end)):
        i = 0
        j = end

        while i < j:
            sum = nums[i] + nums[j]

            if sum > target:
                j--;
            elif sum < target:
                i++;
            elif sum == target:
                # Check duplicates to avoid duplicate triplets
                while nums[i] == nums[i + 1]
                    i++;
                while nums[j] == nums[j - 1]
                    j--

                # Once we get triplet we always move i and j
                result.add(-target, i, j)
                i++
                j--
'''

'''
TC: O(nlogn) + O(n^2) = O(n^2)
SC: O(1) => Sorting is in-place
'''

def twoSum(target, nums, i, j, result):
    while i < j:
        sum = nums[i] + nums[j]
        if sum > target:
            j -= 1
        elif sum < target:
            i += 1
        else:
            # Check & remove duplicates to avoid duplicate triplets
            # i < j is stopping condition to avoid infinite loop since we need to stop moving pointers in case i crosses j which means we saw all the elements already
            while i < j and nums[i] == nums[i + 1]:
                i += 1
            while i < j and nums[j] == nums[j - 1]:
                j -= 1

            result.append([-target, nums[i], nums[j]]) # Remember we need to return number and not indexes
            # Once we get triplet we always move i and j
            i += 1
            j -= 1

# O(nlogn) + O(n^2)
def threeSum(nums):
    n = len(nums)

    # For triplet to be returned input array should have atleast 3 elements; if not we return []
    if n < 3:
        return []

    nums.sort() # O(nlogn)
    result = []
    print(nums)

    for i in range(0, n): # O(n)
        # Check Duplicate whether this n1 is already seen before to avoid duplicates
        # Also check i > 0 else i - 1 would be -1
        if i > 0 and nums[i] == nums[i - 1]: # While not needed since sorted so cannot be ahead to check for same again
            continue

        n1 = nums[i] # Fix n1
        # Perform 2Sum on the rest of the array
        twoSum(-(n1), nums, i + 1, n - 1, result) # This would give us n2 and n3 - O(n)

    return result

nums = [-3, 0, 1, 2, -1, 1, -2]
print(threeSum(nums))