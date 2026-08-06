class ListNode:
    def __init__(self, key=0, val=0, prev=None, next=None):
        self.key = key
        self.value = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capa = capacity
        self.left = ListNode()
        self.right = ListNode()
        self.left.next, self.right.prev = self.right, self.left
    
    def insert(self, node):
        prev = self.right.prev
        node.next = self.right
        node.prev = prev
        prev.next = node
        self.right.prev = node

    def remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        self.cache[key] = ListNode(key=key, val=value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capa:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
