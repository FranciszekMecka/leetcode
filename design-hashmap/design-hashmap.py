class MyHashMap:

    def __init__(self):
        self.values = {}

    def put(self, key: int, value: int) -> None:
        self.values[key] = value
            

    def get(self, key: int) -> int:
        if key in self.values:
            return self.values[key]
        return -1

    def remove(self, key: int) -> None:
        if key in self.values:
            self.values.pop(key)
        


# Your MyHashMap object will be instantiated and called as such:
key = 16
value = 256
obj = MyHashMap()
obj.put(key,value)
print(obj.values)
param_2 = obj.get(key) 
obj.remove(key)