''' Problem 1: Implement a function that merges two sorted list of m and n elements respectively, into another sorted list.

Using 2 pointers approach

Implement a function that merges two sorted list of m and n elements respectively, into another sorted list.

Using 2 pointers approach - TC: O(n)

Question: TC would be O(m + n) or O(n) '''

list1 = [1, 1, 2, 5, 8]
list2 = [3, 4, 6]
list3 = []
i = 0
j = 0

while i < len(list1) and j < len(list2):
  if list1[i] < list2[j]:
    list3.append(list1[i])
    i += 1
  else:
    list3.append(list2[j])
    j += 1

for k in range(i, len(list1)):
  list3.append(list1[k])

for k in range(j, len(list2)):
  list3.append(list2[k])

print(list3)