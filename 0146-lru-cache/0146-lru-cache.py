class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.left = None
        self.right = None
        
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.right = self.tail
        self.tail.left = self.head
        
    def insert(self, node): 
        previousNode = self.tail.left
        nextNode = self.tail
        previousNode.right = nextNode.left = node
        node.right = nextNode
        node.left = previousNode
    
    def remove(self, node):
        previousNode = node.left
        nextNode = node.right
        previousNode.right = nextNode
        nextNode.left = previousNode

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        
        if len(self.cache) > self.capacity:
            lru = self.head.right
            self.remove(lru)
            del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)