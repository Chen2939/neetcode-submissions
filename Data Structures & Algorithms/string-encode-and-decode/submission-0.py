class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0 # i is pointer of index

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            # length tells how many following characters we have to read after j 
            length = int(s[i:j])
            # String to read
            res.append(s[j+1 : j+1+length])
            # After readed string
            i = j + 1 + length
        return res