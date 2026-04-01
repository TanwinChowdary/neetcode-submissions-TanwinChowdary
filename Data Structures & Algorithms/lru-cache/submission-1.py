class Node:
    def __init__(self,key,val, next=None, prev=None):
        self.val = val
        self.key = key
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.head =  self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self,node):
        prev, nxt = self.tail.prev, self.tail
        prev.next = nxt.prev = node
        node.next , node.prev = nxt, prev
    
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.head.next
            self.remove(lru)
            del self.cache[lru.key]
        
