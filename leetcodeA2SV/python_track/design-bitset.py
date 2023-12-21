class Bitset:

    def __init__(self, size: int):
        self.size = size
        self.ones = set()
        self.zeroes = {i for i in range(size)}
        

    def fix(self, idx: int) -> None:
        self.zeroes.discard(idx)
        self.ones.add(idx)
        

    def unfix(self, idx: int) -> None:
         self.ones.discard(idx)
         self.zeroes.add(idx)

    def flip(self) -> None:
            self.zeroes, self.ones = self.ones, self.zeroes    

    def all(self) -> bool:
        return len(self.ones) == self.size        

    def one(self) -> bool:
        return len(self.ones) >= 1        

    def count(self) -> int:
        return len(self.ones)
        

    def toString(self) -> str:
        new = ["" for i in range(self.size)]
        for i in self.zeroes:
            new[i]= "0"
        for j in self.ones:
            new[j] = "1"

        return "".join(new)


        


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()