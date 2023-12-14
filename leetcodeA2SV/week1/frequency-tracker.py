class FrequencyTracker:

    def __init__(self):
        self.elements = defaultdict(int)
        self.f = defaultdict(int)

    def add(self, number: int) -> None:
        
        if self.f[self.elements[number]] > 0:
            self.f[self.elements[number]] -= 1
        else:
            del self.f[self.elements[number]]

        self.elements[number] += 1
        self.f[self.elements[number]] += 1
        

    def deleteOne(self, number: int) -> None:
        if number in self.elements:
            if self.f[self.elements[number]] > 0:
                self.f[self.elements[number]] -= 1
            else:
                del self.f[self.elements[number]]

            
            if self.elements[number] > 1:
                self.elements[number] -= 1
            else:
                self.elements.pop(number)

            self.f[self.elements[number]] += 1
        

    def hasFrequency(self, frequency: int) -> bool:
        #print(self.f, self.elements)
        return frequency in self.f and self.f[frequency] > 0

# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)