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
        r = len(self.hashMap[key]) - 1
        if not values:
            return ""
        while l < r:
            mid = (l + r) // 2
            midTime = self.hashMap[key][mid][1]
            if midTime == timestamp or (midTime < timestamp < self.hashMap[key][mid + 1][1]):
                return self.hashMap[key][mid][0]
            elif self.hashMap[key][mid + 1][1] <= timestamp:
                l = mid + 1
            else:
                 r = mid - 1
        if self.hashMap[key][l][1] <= timestamp:
            return self.hashMap[key][l][0]
        return ""

        
        


        
