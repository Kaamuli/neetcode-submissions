class MyHashMap:

    def __init__(self):
        self.hashmap = []

    def put(self, key: int, value: int) -> None:
        for key_value_pair in self.hashmap:
            if key_value_pair[0] == key:
                key_value_pair[1] = value
                return
        self.hashmap.append([key, value])


    def get(self, key: int) -> int:
        for key_value_pair in self.hashmap:
            if key_value_pair[0] == key:
                return key_value_pair[1]
        return -1

    def remove(self, key: int) -> None:
        for key_value_pair in self.hashmap:
            if key_value_pair[0] == key:
                self.hashmap.remove(key_value_pair)

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)