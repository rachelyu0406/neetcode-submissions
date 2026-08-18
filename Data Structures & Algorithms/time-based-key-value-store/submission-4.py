class TimeMap:
# use hashmap + binary search
# Is mid <= target?
#     yes → mid is valid, save it and look farther right
#     no  → look left

    def __init__(self):
        self.hashMap = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashMap[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        values = self.hashMap[key]
        l = 0
        r = len(values) - 1
        res = ""
        while l <= r:
            mid = (l + r) // 2
            midTime = values[mid][1]
            if midTime <= timestamp:
                res = values[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return res

        
        


        
