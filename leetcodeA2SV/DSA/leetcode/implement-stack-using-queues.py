"""class Queue:
    def __init__(self):
        self.lst =[]
        self.size = 0

    def push(self, val):
        self.lst.append(val)
        self.size += 1

    def peak(self):
        if self.size == 0:
            return -1
        return self.lst[0]
    def pop(self):
        if self.size == 0:
            return -1
        self.size -= 1
        return self.lst.pop(0)
    def is_empty(self):
        return self.size == 0


class MyStack:
   
    def __init__(self):
         self.p = Queue()
         self.q = Queue()
         self.size = self.q.size
         self.temp = []

    def push(self, x: int) -> None:
        self.temp.insert(0,x)
        self.p.push(x)
        
        self.q = Queue()
        for i in self.temp:
            self.q.push(i)
        self.size += 1 

    def pop(self) -> int:      
        self.size -= 1
        return self.q.pop()
            
    def top(self) -> int:    
        return self.q.peak()

    def empty(self) -> bool:
        return self.size == 0"""
class MyStack:
    def __init__(self):
        self.q1 = []
        self.q2 = []
        self.top_val = None

    def push(self, x):
        self.q1.append(x)
        self.top_val = x

    def pop(self):
        if not self.q1:
            return None
        while len(self.q1) > 1:
            self.top_val = self.q1.pop(0)
            self.q2.append(self.top_val)
        val = self.q1.pop(0)
        self.q1, self.q2 = self.q2, self.q1
        return val

    def top(self):
        if not self.q1:
            return None
        return self.top_val

    def empty(self):
        return len(self.q1) == 0


        

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()