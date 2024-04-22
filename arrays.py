import array as arr

# Create an array
nums = arr.array('i', [10, 20, 30, 40])

# Insert
def insertAtEnd(element):
  nums.append(element)

def insertAtStart(element):
  nums.insert(0, element)

def insertInMiddle(index, element):
  nums.insert(index, element)

# Update
def updateElement(index, element):
  nums[index] = element

# Accessing
def getElementByIndex(index):
  return nums[index]

# Delete
def removeFromEnd():
  nums.pop()

def removeFromStart():
  nums.pop(0)

def removeFromMiddle(index):
  nums.pop(index)

# Search an element and return its index

def search(element):
  return nums.index(element)

# Traversal
def printArray():
  for num in nums:
    print(num)

# Execution

insertAtEnd(60)
print(nums)  # [10, 20, 30, 40, 60]

insertAtStart(100)
print(nums)  # [100, 10, 20, 30, 40, 60]

insertInMiddle(2, 90)
print(nums)  # [100, 10, 90, 20, 30, 40, 60]

updateElement(4, 80)
print(nums)  # [100, 10, 90, 20, 80, 40, 60]

print(getElementByIndex(2))  # 90

removeFromEnd()
print(nums)  # [100, 10, 90, 20, 80, 40]

removeFromStart()
print(nums)  # [10, 90, 20, 80, 40]

removeFromMiddle(2)
print(nums)  # [10, 90, 80, 40]

print(search(90))  # 1

# Sort an array
nums = sorted(nums)
print(nums)  # [10, 40, 80, 90]

# Sort an array in descending order
nums = sorted(nums, reverse=True)
print(nums)  # [90, 80, 40, 10]

# Reverse an array
nums.reverse()
print(nums)  # [10, 40, 80, 90]

# Slicing an array

print('Slicing')

nums = nums[::-1]
print(nums)  # [90, 80, 40, 10] - Reverses an array

print(nums[1:])  # [80, 40, 10]

print(nums[:2])  # [90, 80]

print(nums[1:3])  # [80, 40]

print(nums[:])  # [90, 80, 40, 10]

print(len(nums)) # 4

# Count

insertAtEnd(10)
print(nums)

print(nums.count(10))  # 2 - Since 10 appears 2 times in the list

printArray()