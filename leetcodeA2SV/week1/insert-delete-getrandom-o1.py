class RandomizedSet:

    def __init__(self):
        self.e = set()

        

    def insert(self, val: int) -> bool:
        if val not in self.e:
            self.e.add(val)
            return True
        else:
            return False

        

    def remove(self, val: int) -> bool:
        if val in self.e:
            self.e.discard(val)
            return True
        else:
            return False


    def getRandom(self) -> int:
        t = tuple(self.e)
        return random.choice(t)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

