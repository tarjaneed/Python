class Item:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class Hashing:
    def __init__(self):
        self.hashMap = []
        self.capacity = 7

    def put(self, item):
        index = self.hash(item.key)
        self.hashMap.insert(index, item)

    def remove(self, item):
        index = self.hash(item.key)
        self.hashMap.pop(index)

    def search(self, item):
        try:
            index = self.hash(item.key)
            val = self.hashMap[index]
            print(f'{item.key} is at index {index}')
        except:
            print(f'{item.key} not found')

    # Converts each character of the key into an integer -> Sums it and then mod by array length
    def hash(self, key):
        sum = 0

        for char in key:
            sum += ord(char)

        return sum % self.capacity
    
    def printHashMap(self):
        key_value_pairs = [f'{item.key, item.value}' for item in self.hashMap]
        print(key_value_pairs)

item1 = Item("Alice", "NYC")
item2 = Item("Bob", "CA")
item3 = Item("John", "LA")

hashing = Hashing()
hashing.put(item1)
hashing.put(item2)
hashing.put(item3)
hashing.printHashMap()

hashing.search(item3)
hashing.search(Item("Jack", "CA"))

hashing.remove(item3)
hashing.printHashMap()