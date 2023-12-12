class OrderedStream:

    def __init__(self, n: int):
        self.values = [0 for i in range(n)]
        self.n = n
        self.pointer = 0
        

    def insert(self, idKey: int, value: str) -> List[str]:
        self.values[idKey-1] = value
        
        temp = []
        while self.pointer < self.n and self.values[self.pointer] != 0:
            temp.append(self.values[self.pointer])
            self.pointer += 1
        return temp

        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)