class RecentCounter:
    window=[]
    def __init__(self):
        self.window=[]

    def ping(self, t: int) -> int:
        self.window.append(t)
        i=0
        while self.window[i]<t-3000:
            i+=1
        self.window=self.window[i:]
        return len(self.window)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)