class TimeMap:

    def __init__(self):
        self.store = {} # key : [List of [value, time]]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = [[value, timestamp]]
        else:
            self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        values = self.store.get(key, [])
        
        # l, r = 0, len(values)-1
        # while l<=r:
        #     mid = (l+r) // 2
        #     if values[mid][1] <= timestamp:
        #         res = values[mid][0]
        #         l = mid + 1
        #     else:
        #         r = mid-1
        for i in range(len(values)-1, -1, -1):
            if values[i][1] > timestamp:
                continue
            else:
                return values[i][0]
        return ""
            


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)