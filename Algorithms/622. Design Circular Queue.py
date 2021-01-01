class MyCircularQueue:

    def __init__(self, k: int):
        self.q=[[] for i in range(k)]
        self.k=k
        self.length = 0
        self.l=0
        self.r=-1

    def enQueue(self, value: int) -> bool:
        if (self.length>=len(self.q)):
            return False
        self.length+=1
        self.r=(self.r+1)%self.k
        self.q[self.r]=value
        return True

    def deQueue(self) -> bool:
        if (self.length==0):
            return False
        self.length-=1
        self.l = (self.l+1)%self.k
        return True

    def Front(self) -> int:
        if self.length==0:
            return -1
        return self.q[self.l]

    def Rear(self) -> int:
        if self.length==0:
            return -1
        return self.q[self.r]

    def isEmpty(self) -> bool:
        return self.length==0

    def isFull(self) -> bool:
        return self.length==self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()