from collections import OrderedDict
class LRUCache():
    def __init__(self, capacity):
        self.memory = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.memory:
            return - 1
        self.memory.move_to_end(key)
        return self.memory[key]

    def put(self, key, value):
        if key in self.memory:
            self.memory.move_to_end(key)
        self.memory[key] = value
        if len(self.memory) > self.capacity:
            self.memory.popitem(last = False)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)