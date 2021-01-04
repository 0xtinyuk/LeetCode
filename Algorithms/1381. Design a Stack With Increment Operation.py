class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = [0 for i in range(maxSize)]
        self.incr = [0 for i in range(maxSize)]
        self.p = -1

    def push(self, x: int) -> None:
        if self.p+1<self.maxSize:
            self.p+=1
            self.stack[self.p]=x
            self.incr[self.p]=0

    def pop(self) -> int:
        if self.p>=0:
            x = self.stack[self.p]+self.incr[self.p]
            if self.p>=1:
                self.incr[self.p-1]+=self.incr[self.p]
            self.p-=1
            return x
        return -1

    def increment(self, k: int, val: int) -> None:
        if self.p==-1:
            return
        self.incr[min(self.p,k-1)]+=val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)