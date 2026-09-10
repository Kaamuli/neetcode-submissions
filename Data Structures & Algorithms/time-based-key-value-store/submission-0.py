class TimeMap:

    def __init__(self):
        self.store = {} #Hashmap has the key : list of [value, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store: #If the key isn't alr in the TimeMap
            self.store[key] = []
        self.store[key].append([value,timestamp]) #List of [value,timestamp]'s

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.store.get(key, [])

        L, R = 0, len(values) - 1

        while L <= R:
            M = L + (R-L)//2

            if values[M][1] <= timestamp:
                res = values[M][0]
                L = M + 1
            else:
                R = M - 1
        
        return res