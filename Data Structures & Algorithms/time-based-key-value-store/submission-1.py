class TimeMap:

    def __init__(self):
        self.res = {} # key: [value, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.res:
            self.res[key] = []
        self.res[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        # bs over values
        values = self.res.get(key, [])
        result = ""

        l, r = 0, len(values)-1
        while l <= r:
            m = (l+r) // 2
            if values[m][1] <= timestamp: # valid timestamp
                result = values[m][0]
                l = m + 1
            else:
                r = m - 1
        
        return result
        

