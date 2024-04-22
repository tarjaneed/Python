list1 = [10, 20, 30, 40]


# Insert at End
def insertAtEnd(element):
  list1.append(element)


# Insert at Start
def insertAtStart(element):
  list1.insert(0, element)


# Insert in Middle
def insertInMiddle(index, element):
  list1.insert(index, element)


# Update an element
def updateElement(index, element):
  list1[index] = element


# Find the element and return its index
def searchElement(element):
  return list1.index(element)


# Remove from End
def removeFromEnd():
  list1.pop()


# Remove from Start
def removeFromStart():
  list1.pop(0)


# Remove Element
def removeElement(element):
  index = list1.index(element)
  list1.pop(index)

# Traversal
def printList():
  for element in list1:
    print(element)

# Execution
insertAtEnd(50)
print(list1)  # [10, 20, 30, 40, 50]

print(len(list1))  # 5

insertAtStart(30)
print(list1)  # [30, 10, 20, 30, 40, 50]

insertInMiddle(2, 100)
print(list1)  # [30, 10, 100, 20, 30, 40, 50]

# Accessing an element
print(list1[2])  # 100

print(searchElement(40))  # 5

updateElement(3, 90)
print(list1)  # [30, 10, 100, 90, 30, 40, 50]

removeFromEnd()
print(list1)  # [30, 10, 100, 90, 30, 40]

removeFromStart()
print(list1)  # [10, 100, 90, 30, 40]

removeElement(100)
print(list1)  # [10, 90, 30, 40]

list1.sort()
print(list1)  # [10, 30, 40, 90]

list1.sort(reverse=True)
print(list1)  # [90, 40, 30, 10]

list1.reverse()
print(list1)  # [10, 30, 40, 90]

# Slicing

print(list1[::-1])  # [90, 40, 30, 10] - Reverses the list

print(list1[:3])  # [10, 30, 40]

print(list1[1:3])  # [30, 40]

# Count

insertAtEnd(30)
print(list1)

print(list1.count(30))  # 2 - Since 30 appears 2 times in the list

printList()