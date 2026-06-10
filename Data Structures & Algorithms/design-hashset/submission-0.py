class MyHashSet:

    def __init__(self):
        self.table = [[]for _ in range(1000)]

    def add(self, key: int) -> None:
        hash = key % 1000
        if key not in self.table[hash]:
            self.table[hash].append(key)
        

    def remove(self, key: int) -> None:
        hash = key % 1000
        if key  in self.table[hash]:
            self.table[hash].remove(key)
        

    def contains(self, key: int) -> bool:
        hash = key % 1000
        if key in self.table[hash]:
            return True
        else:
            return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)