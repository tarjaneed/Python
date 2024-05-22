# heapq - built in python data structure which helps in creating a heap or priority queue

import heapq

list1 = [2, 3, 4]

# Converting a list into a heap - O(n)
heapq.heapify(list1) # Default Min-heap
print('Heap from List:', list1)

heapq.heappush(list1, 1) # O(logn)
print(list1)

popped_element = heapq.heappop(list1) # O(logn) - Removes and returns the smallest element from the min heap
print('The popped element is the smallest element from min-heap:', popped_element)

print(list1)

print(list1[0]) # To find minimum value of heap - O(1)

largest = heapq.nlargest(2, list1) # O(nlogk) - n total no of elements and k is the k-largest
print(largest)

smallest = heapq.nsmallest(2, list1) # O(nlogk) - n total no of elements and k is the k-smallest
print(smallest)