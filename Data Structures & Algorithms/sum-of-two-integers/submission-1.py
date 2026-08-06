class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff
        while (b & mask) > 0:
            temp = a
            a = a ^ b
            b = (temp & b) << 1
        return (a & mask) if b > 0 else a