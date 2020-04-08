"""
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?
"""

# Time Complexity : Lookup, Insert, Delete - O(1)
# Space Complexity : O(m) where m is the capacity of the cache

class Node(object):
    
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.head = Node(-1, -1)
        self.tail = self.head
        self.hash = {}  
        self.length = 0

    def get(self, key):

        if key not in self.hash:
            return -1
        
        node = self.hash[key]
        value = node.value
        
        while node.next:
            node.prev.next = node.next
            node.next.prev = node.prev
            self.tail.next = node
            node.prev = self.tail
            node.next = None
            self.tail = node
        
        return value
            

    def put(self, key, value):

        if key in self.hash:
            node = self.hash[key]
            node.value = value
            
            while node.next:
                node.prev.next = node.next
                node.next.prev = node.prev
                self.tail.next = node
                node.prev = self.tail
                node.next = None
                self.tail = node
        
        else:
            node = Node(key, value)
            self.hash[key] = node
            
            self.tail.next = node
            node.prev = self.tail
            node.next = None
            self.tail = node
            self.length += 1
            
            if self.length > self.capacity:
                remove = self.head.next
                self.head.next = self.head.next.next
                self.head.next.prev = self.head
                del self.hash[remove.key]
                self.length -= 1

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
assert cache.get(1) == 1, "Houston, we have a problem!"         # returns 1
cache.put(3, 3)                                                 # evicts key 2
assert cache.get(2) == -1, "Houston, we have a problem!"        # returns -1 (not found)
cache.put(4, 4)                                                 # evicts key 1
assert cache.get(1) == -1, "Houston, we have a problem!"        # returns -1 (not found)
assert cache.get(3) == 3, "Houston, we have a problem!"         # returns 3
assert cache.get(4) == 4, "Houston, we have a problem!"         # returns 4
print("Success!")
