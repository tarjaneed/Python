'''
Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.

int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache.

If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

Example 1:

Input:
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"] 
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]

Output:
[null, null, null, 1, null, -1, null, -1, 3, 4]
'''

# TC: O(1) - get and put since we use hashtable so unless collision it will be O(1)
# SC: Hashmap: O(n)

class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cache = {}

    def size(self):
        print(len(self.cache))

    def get(self, key):
        if key not in self.cache:
            return -1
        else:
            self.removeNode(self.cache[key]) # Remove existing node
            node = Node(self.cache[key].key, self.cache[key].data) # Need to send value while creating an instance of node
            self.addNode(node) # Create a new node with the same value and place it at the front of the DLL - to maintain most frequently used element
            del self.cache[key]
            self.cache[key] = node # Saves reference / address of the node as the value we get actual value from the linked list's node.data by going to that address and accessing it
            return (self.cache[key]).data
        
    def put(self, key, value):
        if key not in self.cache:
            if len(self.cache) < self.capacity:
                node = Node(key, value)
                self.cache[key] = node
                self.addNode(node)
            else:
                # Remove least recently used; create a new node with value and add at the front of DLL
                lru_node = self.tail.prev # Prev node of the tail node would be the one that is recently used since most recently used is at the front next to head i.e the 2nd node
                self.removeNode(lru_node)
                del self.cache[lru_node.key]
                node = Node(key, value)
                self.addNode(node)
                self.cache[key] = node
        else:
            # Remove least recently used; create a new node with value and add at the front of DLL
            lru_node = self.tail.prev # Prev node of the tail node would be the one that is recently used since most recently used is at the front next to head i.e the 2nd node
            self.removeNode(lru_node)
            del self.cache[key]
            node = Node(key, value)
            self.addNode(node)
            self.cache[key] = node

    def addNode(self, newNode):
        temp = self.head.next
        self.head.next = newNode
        newNode.prev = self.head
        newNode.next = temp
        temp.prev = newNode

    def removeNode(self, node):
        l = node.prev
        r = node.next
        l.next = r
        r.prev = l

lru = LRUCache(2)
lru.put(1, 1)
lru.put(2, 2)
print(lru.get(1))
lru.put(3, 3)
print(lru.get(2))
lru.put(4, 4)
print(lru.get(1))
print(lru.get(3))
print(lru.get(4))

# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"] 
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# [null, null, null, 1, null, -1, null, -1, 3, 4]