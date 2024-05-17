# Question: https://leetcode.com/problems/time-based-key-value-store/description/

class TimeMap:

    def __init__(self):
        self.keyMap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyMap:
            self.keyMap[key] = []
        self.keyMap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        values = self.keyMap.get(key,[])
        
        def recursion(left, right, res):
            if left > right:
                return res
            mid = left + (right - left) // 2
            if values[mid][1] <= timestamp:
                return recursion(mid + 1, right, values[mid][0])
            else:
                return recursion(left, mid - 1, res)
        
        return recursion(0, len(values) - 1, "")
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)