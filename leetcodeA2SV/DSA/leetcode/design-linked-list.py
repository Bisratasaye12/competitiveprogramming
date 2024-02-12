class ListNode:
    def __init__(self, val= 0, next=None):
        self.val = val
        self.next = next
        


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.capacity = 0

    def get(self, index: int) -> int:
        if self.head == None or index >= self.capacity:
            return -1
        
        curr = self.head
        
        for i in range(index):
            curr = curr.next
        return curr.val
        
            

    def addAtHead(self, val: int) -> None:
        newNode = ListNode(val)
        if self.head:
            newNode.next = self.head
            self.head = newNode
        else:
            self.head = self.tail = newNode
        self.capacity += 1

    def addAtTail(self, val: int) -> None:
        newNode = ListNode(val)
        if self.head:
            self.tail.next = newNode
            self.tail = newNode
            self.capacity += 1
        else:
            self.addAtHead(val)
        

    def addAtIndex(self, index: int, val: int) -> None:
        newNode = ListNode(val)
        if index == self.capacity:
             self.addAtTail(val)
        elif index < self.capacity:
            curr = self.head
            if index == 0:
                self.addAtHead(val)
            else:
                for i in range(index - 1):
                    curr = curr.next
                newNode.next = curr.next
                curr.next = newNode
                self.capacity += 1
                
        
            
    def deleteAtIndex(self, index: int) -> None:
        if index < self.capacity:
            curr = self.head
            if self.capacity == 1:
                self.head = self.tail = None
            elif index == 0:
                self.head = self.head.next
            else:
                for i in range(index-1):
                    curr = curr.next
                
                curr.next = curr.next.next
                if index == self.capacity - 1:
                    self.tail = curr
            self.capacity -= 1



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)