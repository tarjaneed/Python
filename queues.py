queue = []

def enqueue(element):
    queue.append(element)

def dequeue():
    queue.pop(0)

def front():
    return queue[0]

def rear():
    return queue[-1]

def size():
    return len(queue)

def isEmpty():
    return size() == 0


print(isEmpty()) # True

enqueue(1)
enqueue(10)
enqueue(20)
enqueue(100)

print(queue) # [1, 10, 20, 100]

print(front()) # 1

print(rear()) # 100

dequeue() # [10, 20, 100]

print(queue)

print(front()) # 10

print(isEmpty()) # False
