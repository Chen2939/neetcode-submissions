class ListNode:
    def __init__(self, key=-1, value=-1, nxt=None):
        self.key = key
        self.value = value
        self.nxt = nxt

class MyHashMap:

    def __init__(self):
        self.nodeList = [ListNode()] * 1000

    def put(self, key: int, value: int) -> None:
        cur = self.nodeList[key % len(self.nodeList)]
        while cur.nxt:
            if cur.nxt.key == key:
                cur.nxt.value = value
                return
            cur = cur.nxt
        cur.nxt = ListNode(key, value)

    def get(self, key: int) -> int:
        cur = self.nodeList[key % len(self.nodeList)]
        while cur:
            if cur.key == key: return cur.value
            cur = cur.nxt   
        return -1

    def remove(self, key: int) -> None:
        cur = self.nodeList[key % len(self.nodeList)]
        while cur and cur.nxt:
            if cur.nxt.key == key:
                cur.nxt = cur.nxt.nxt
                return
            cur = cur.nxt
            
            


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)