from collections import deque

dq = deque([10, 20, 30])


# Add element to the end of the queue - right side
def insertElement(element):
    dq.append(element)

# Add element to the start of the queue - left side
def insertElementAtStart(element):
    dq.appendleft(element)


# Add in the Middle
def insertInMiddle(index, element):
    dq.insert(index, element)

# Update an element
def updateElement(index, element):
    dq[index] = element

# Delete from end - right side
def removeFromEnd():
    dq.pop()

# Delete from front - left side
def removeFromStart():
    dq.popleft()

# Delete element - deletes first occurence
def removeElement(element):
    dq.remove(element)

# Traversal
def printDeque():
  for element in dq:
    print(element)

# Execution

insertElement(40)
print(dq) # [10, 20, 30, 40]

insertElementAtStart(100)
print(dq) # [100, 10, 20, 30, 40]

insertInMiddle(2, 30)
print(dq) # [100, 10, 30, 20, 30, 40]

# Accessing

print(dq[2]) # 30

updateElement(1, 90)
print(dq) # [100, 90, 30, 20, 30, 40]

removeElement(90)
print(dq) # [100, 30, 20, 30, 40]

print(dq.count(30)) # 2

print(len(dq)) # 5

removeFromEnd() # [100, 30, 20, 30]

removeFromStart() # [30, 20, 30]

insertElement(100)
print(dq) # [30, 20, 30, 100]

dq.reverse()
print(dq) # [100, 30, 20, 30]

printDeque()