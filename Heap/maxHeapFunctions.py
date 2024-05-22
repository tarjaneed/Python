# Implement Heap: Max Heap common operations: Insert, Delete, Find Max - Recursively for every parent node all of its descendants are <= to the parent node i.e. root has max value

class Heap:
    def __init__(self):
        self.heap = [0] # Since we would start adding the elements from index 1 to maintain the structure property and apply those 3 left, right and parent formulas

    def printMaxHeap(self):
        maxHeap = self.heap.copy()
        maxHeap.pop(0)
        print('Heap =>', maxHeap)

    # TC: O(1) since the max would also be found on the root node in a max-heap
    def findMax(self):
        if len(self.heap) > 1:
            return self.heap[1]
        return None

    # TC: O(logn) - TC is height of the tree and for a balanced BT it is O(logn) and we check and swap at one half only
    # Heapify Up
    def push(self, element):
        # Always append the new element at the next location available or at the end of an array
        self.heap.append(element)

        # Now get the index of the newly added element to use it for swapping during heapify down to fix the order property i.e. to make sure parent is max than its children
        index = len(self.heap) - 1

        # Perform heapify up check newly inserted element with its parent node and if new node is > than parent, swap continue this till all nodes are ordered
        # parent = index // 2 and new element index = index
        while (index > 1 and self.heap[index] > self.heap[(index // 2)]):
            temp = self.heap[(index // 2)]
            self.heap[(index // 2)] = self.heap[index]
            self.heap[index] = temp

            index = index // 2 # Update the index pointer to continue checking till the end until we find max node

    # TC: O(logn) - TC is height of the tree and for a balanced BT it is O(logn) and we check and swap at one half only
    # Removes and return the max element which is always at the top in case of the max heap but also rearranges the elements to maintain structure and order property
    # Heapify Down
    def pop(self):
        # If heap is empty we are checking len of 1 because by default it always has 1 element which is 0
        if len(self.heap) == 1:
            return None

        # If heap has only one element
        if len(self.heap) == 2:
            return self.heap.pop() # or self.heap[1]
        
        # Take the root element for it to be returned
        maximum = self.heap[1]
        # Now take the last element of the tree or an array and keep it at the root
        self.heap[1] = self.heap.pop()

        index = 1 # we start with index 1 since we saved values from that index

        # Continue to loop till we have the left child once we do not find left child we know we have to stop: to check left use 2 * index and compare it with < to len(heap)
        # Perform Heapify down - Check the current index node at root with the right child if its greater than swap it or else check on the left child i.e. 
        # basically replace with max of left & right child

        while ((2 * index) < len(self.heap)):
            left = 2 * index
            right = 2 * (index + 1)

            # Swap with Right Side if there is a: right child; if right is less than left; if right is less than root/parent else move to check on left side
            if (right < len(self.heap) and self.heap[right] > self.heap[left] and self.heap[right] > self.heap[index]):
                temp = self.heap[index]
                self.heap[index] = self.heap[right]
                self.heap[right] = temp

                index = right # Update the index to point to the right side to check further recursively i.e. to index = 2 * (index + 1)

            # Swap with left side - no need to check if left child exists since we already check in while
            elif (self.heap[left] > self.heap[index]):
                temp = self.heap[index]
                self.heap[index] = self.heap[left]
                self.heap[left] = temp

                index = left # Update the index to point to the left side to check further recursively i.e. to index = 2 * index

            # This is when there is no need to swap and the node/element is already in proper place
            # Eg. node is <= left or right (only 1 child exists) or both left and right (if both child exists)
            else:
                break    

        return maximum

maxheap = Heap()
maxheap.printMaxHeap()
print('Maximum =>', maxheap.findMax())
print('Popped Element =>', maxheap.pop())

maxheap.push(7)
maxheap.printMaxHeap()
print('Maximum =>', maxheap.findMax())
print('Popped Element =>', maxheap.pop())

maxheap.push(7)
maxheap.push(2)
maxheap.push(3)
maxheap.push(1)
maxheap.push(9)

maxheap.printMaxHeap()
print('Maximum =>', maxheap.findMax())

print('Popped Element =>', maxheap.pop())
maxheap.printMaxHeap()