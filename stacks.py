stack = []

def push(element):
    stack.append(element)

def pop():
    stack.pop()

def top():
    return stack[-1]

def size():
    return len(stack)

def isEmpty():
    return size() == 0


# Execution

print(isEmpty()) # True

push(1)
push(2)
push(3)
push(4)

print(stack) # [1, 2, 3, 4]

print(top()) # 4

pop()

print(stack) # [1, 2, 3]

print(top()) # 3

print(size()) # 3

print(isEmpty()) # False