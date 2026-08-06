class ListNode:
    def __init__(self, key=-1, nxt=None):
        self.key = key
        self.nxt = nxt

class MyHashSet:

    def __init__(self):
        self.nodeList = [ListNode()] * 1000000

    def add(self, key: int) -> None:
        cur = self.nodeList[key % 1000000]
        while cur.nxt:
            if cur.nxt.key == key: return
            cur = cur.nxt
        cur.nxt = ListNode(key)

    def remove(self, key: int) -> None:
        cur = self.nodeList[key % 1000000]
        while cur.nxt:
            if cur.nxt.key == key:
                cur.nxt = cur.nxt.nxt
                return
            cur = cur.nxt

    def contains(self, key: int) -> bool:
        cur = self.nodeList[key % 1000000]
        while cur.nxt:
            if cur.nxt.key == key:
                return True
            cur = cur.nxt

        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)